from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from app.main import analyze_property
from app.schemas import PropertyIntelligence

app = FastAPI(title="GrowthVector Property Intelligence")


class ListingRequest(BaseModel):
    listing: str = Field(min_length=20, max_length=5000)


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/analyze", response_model=PropertyIntelligence)
def analyze(req: ListingRequest):
    try:
        return analyze_property(req.listing)
    except Exception as e:
        raise HTTPException(
            status_code=502, detail=f"Analysis failed: {type(e).__name__}"
        )
