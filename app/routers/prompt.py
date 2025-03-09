from fastapi import APIRouter, HTTPException
from typing import List
from app.schemas.prompt import PromptCreate, PromptResponse
from app.dependencies.database import save_prompt, get_all_prompts

router = APIRouter(prefix="/prompts", tags=["prompts"])

@router.post("/", response_model=PromptResponse)
async def save_prompt_route(prompt_data: PromptCreate) -> PromptResponse:
    try:
        saved_prompt = await save_prompt(prompt_data.name, prompt_data.content)
        return PromptResponse(**saved_prompt)
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error saving prompt: {str(e)}"
        )

@router.get("/", response_model=List[PromptResponse])
async def get_all_prompts_route() -> List[PromptResponse]:
    try:
        prompts = await get_all_prompts()
        return [PromptResponse(**prompt) for prompt in prompts]
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error retrieving prompts: {str(e)}"
        ) 