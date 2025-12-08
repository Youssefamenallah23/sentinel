import sqlite3
import os
from datetime import datetime
from pydantic import BaseModel
from typing import Optional

# 1. Define Data Models (Professional Practice)
class Incident(BaseModel):
    error_type: str
    error_message: str
    stack_trace: str

class Solution(BaseModel):
    error_type: str
    fix_explanation: str
    code_snippet: Optional[str] = None

# 2. Database Manager Class
class KnowledgeBase:
    def __init__(self, db_path="database/knowledge_base.db"):
        # Ensure the directory exists
        os.makedirs(os.path.dirname(db_path), exist_ok=True)
        self.db_path = db_path
        self._initialize_db()

    def _get_connection(self):
        return sqlite3.connect(self.db_path)

    def _initialize_db(self):
        """Runs the SQL schema to create tables if they don't exist."""
        try:
            # We assume db_schema.sql is in the same folder as this script
            base_dir = os.path.dirname(os.path.abspath(__file__))
            schema_path = os.path.join(base_dir, "db_schema.sql")
            
            with open(schema_path, 'r') as f:
                schema = f.read()
            
            conn = self._get_connection()
            conn.executescript(schema)
            conn.close()
            print("✅ Database initialized successfully.")
        except Exception as e:
            print(f"❌ Database Init Error: {e}")

    def log_incident(self, incident: Incident):
        """Saves a new crash report."""
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO incidents (error_type, error_message, stack_trace)
            VALUES (?, ?, ?)
        """, (incident.error_type, incident.error_message, incident.stack_trace))
        conn.commit()
        conn.close()
        print(f"📝 Logged incident: {incident.error_type}")

    def get_known_solution(self, error_type: str):
        """Checks if we already know how to fix this error."""
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT fix_explanation, code_snippet FROM solutions WHERE error_type = ?", (error_type,))
        row = cursor.fetchone()
        conn.close()
        
        if row:
            return {"found": True, "explanation": row[0], "code": row[1]}
        return {"found": False}

    def save_solution(self, solution: Solution):
        """Saves a new solution discovered by the AI."""
        conn = self._get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("""
                INSERT OR REPLACE INTO solutions (error_type, fix_explanation, code_snippet)
                VALUES (?, ?, ?)
            """, (solution.error_type, solution.fix_explanation, solution.code_snippet))
            conn.commit()
            print(f"💡 Saved solution for: {solution.error_type}")
        except Exception as e:
            print(f"❌ Error saving solution: {e}")
        finally:
            conn.close()