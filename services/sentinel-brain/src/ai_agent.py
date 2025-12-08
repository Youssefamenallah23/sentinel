import google.generativeai as genai
import os
import json
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure the API
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("❌ API Key not found! Check your .env file.")

genai.configure(api_key=api_key)

# Initialize the Model (Using Flash for speed)
model = genai.GenerativeModel(
    model_name="gemini-2.5-flash",
    generation_config={"response_mime_type": "application/json"}
)

def analyze_error_with_ai(error_type: str, stack_trace: str):
    """
    Sends the stack trace to Gemini and asks for a fix.
    """
    
    prompt = f"""
    You are a Senior Site Reliability Engineer (SRE). 
    Analyze the following Python error log and provide a solution.
    
    ERROR TYPE: {error_type}
    STACK TRACE:
    {stack_trace}
    
    Your response must be a JSON object with this exact structure:
    {{
        "fix_explanation": "A short, clear explanation of why this happened (max 2 sentences).",
        "code_snippet": "The corrected python code block to fix the issue."
    }}
    """

    try:
        response = model.generate_content(prompt)
        # Parse the JSON string into a Python Dictionary
        return json.loads(response.text)
    except Exception as e:
        print(f"❌ AI Generation Error: {e}")
        # Fallback response if AI fails
        return {
            "fix_explanation": "AI analysis failed. Please check logs manually.",
            "code_snippet": "# Manual intervention required"
        }