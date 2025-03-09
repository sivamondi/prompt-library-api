import json
from typing import Dict, Any, List
from pathlib import Path

# Define storage directory
STORAGE_DIR = Path("/Users/sivaramaraomondi/IdeaProjects/prompt-library-api/data")

def ensure_storage_exists() -> None:
    """Ensure storage directory exists"""
    STORAGE_DIR.mkdir(parents=True, exist_ok=True)

async def init_db() -> None:
    """Initialize storage"""
    ensure_storage_exists()

async def close_db_connection() -> None:
    """No-op for file storage"""
    pass

async def save_prompt(name: str, content: Dict[str, Any]) -> Dict[str, Any]:
    """Save prompt to a JSON file"""
    file_path = STORAGE_DIR / f"{name}.json"
    file_path.write_text(json.dumps(content, indent=2))
    return {
        "name": name,
        "content": content
    }

async def get_all_prompts() -> List[Dict[str, Any]]:
    """Read all JSON files from the prompts directory"""
    prompts = []
    for file_path in STORAGE_DIR.glob("*.json"):
        try:
            content = json.loads(file_path.read_text())
            prompts.append({
                "name": file_path.stem,
                "content": content
            })
        except json.JSONDecodeError:
            # Skip invalid JSON files
            continue
    return prompts 