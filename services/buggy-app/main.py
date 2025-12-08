import time
import random
import requests
import traceback
import os
import logging
from datetime import datetime

# Setup Logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Configuration
# Default to localhost for testing, but Docker will override this
N8N_WEBHOOK_URL = os.getenv("N8N_WEBHOOK_URL", "http://localhost:5678/webhook/log-ingest")
INTERVAL = int(os.getenv("ERROR_INTERVAL", "10")) # Seconds between errors

def cause_zero_division():
    x = 10
    y = 0
    return x / y

def cause_index_error():
    data = [1, 2, 3]
    return data[10]

def cause_type_error():
    return "number" + 5

def cause_connection_error():
    raise ConnectionError("Database Connection Refused: 5432 is unreachable")

def simulate_app_activity():
    """Simulates normal activity, then randomly crashes."""
    actions = [
        cause_zero_division,
        cause_index_error,
        cause_type_error,
        cause_connection_error
    ]
    
    # Pick a random disaster
    selected_action = random.choice(actions)
    logger.info(f"Simulating operation: {selected_action.__name__}...")
    selected_action()

def send_alert_to_n8n(error_type, error_msg, stack_trace):
    """Sends the crash report to the Orchestrator (n8n)."""
    payload = {
        "service": "buggy-app-v1",
        "timestamp": datetime.utcnow().isoformat(),
        "error_type": error_type,
        "error_message": error_msg,
        "stack_trace": stack_trace,
        "severity": "HIGH"
    }

    try:
        response = requests.post(N8N_WEBHOOK_URL, json=payload, timeout=5)
        if response.status_code == 200:
            logger.info("✅ Alert sent to n8n successfully.")
        else:
            logger.warning(f"⚠️ n8n received alert but returned {response.status_code}")
    except requests.exceptions.RequestException as e:
        # This is expected if n8n isn't running yet
        logger.error(f"❌ Failed to send alert to n8n: {e}")

if __name__ == "__main__":
    logger.info("🚀 Chaos Generator Started. Waiting to break things...")
    
    while True:
        try:
            simulate_app_activity()
        except Exception as e:
            # 1. Capture the crash details
            error_type = type(e).__name__
            error_msg = str(e)
            stack_trace = traceback.format_exc()
            
            logger.error(f"💥 Application Crashed: {error_type}")
            
            # 2. Send to Sentinel System
            send_alert_to_n8n(error_type, error_msg, stack_trace)

        # 3. Wait before breaking again
        time.sleep(INTERVAL)