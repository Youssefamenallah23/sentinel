from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from .database import KnowledgeBase, Incident, Solution
from .ai_agent import analyze_error_with_ai

# Initialize App & DB
app = FastAPI(title="Sentinel Brain API", version="1.0")
kb = KnowledgeBase()

# --- Data Models ---
class ErrorLogRequest(BaseModel):
    service_name: str
    error_type: str
    error_message: str
    stack_trace: str

# --- Endpoints ---

@app.get("/")
def health_check():
    return {"status": "operational", "system": "Sentinel Brain"}

@app.post("/analyze")
def analyze_log(request: ErrorLogRequest):
    print(f"📥 Received alert: {request.error_type} from {request.service_name}")

    # 1. Log the incident in history
    incident = Incident(
        error_type=request.error_type,
        error_message=request.error_message,
        stack_trace=request.stack_trace
    )
    kb.log_incident(incident)

    # 2. Check Memory (RAG - Retrieval Augmented Generation)
    known_fix = kb.get_known_solution(request.error_type)
    
    if known_fix["found"]:
        print("✅ Found solution in Database!")
        return {
            "source": "knowledge_base",
            "fix_explanation": known_fix["explanation"],
            "code_snippet": known_fix["code"]
        }

    # 3. If Unknown, Ask Gemini (The Agent)
    print("🤖 Unknown error. Asking Gemini...")
    ai_solution = analyze_error_with_ai(request.error_type, request.stack_trace)

    # 4. Save the new knowledge for next time (Write-Back)
    new_solution = Solution(
        error_type=request.error_type,
        fix_explanation=ai_solution["fix_explanation"],
        code_snippet=ai_solution["code_snippet"]
    )
    kb.save_solution(new_solution)

    return {
        "source": "ai_generated",
        "fix_explanation": ai_solution["fix_explanation"],
        "code_snippet": ai_solution["code_snippet"]
    }