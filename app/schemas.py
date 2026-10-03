from typing import List, Literal, Optional
from pydantic import BaseModel, Field


class PropertyInput(BaseModel):
    listing_text: str = Field(min_length=20)
    source_url: Optional[str] = None


class Evidence(BaseModel):
    claim: str
    evidence: str
    confidence: Literal["high", "medium", "low"]


class BuyerHypothesis(BaseModel):
    buyer_type: str
    why_it_may_fit: str
    needs_to_know: List[str]
    claims_to_verify: List[str]


class MarketingOpportunity(BaseModel):
    opportunity: str
    reasoning: str
    supporting_evidence: List[str]
    risk_or_unknown: Optional[str] = None


class PropertyIntelligence(BaseModel):
    property_summary: str
    verified_facts: List[Evidence]
    missing_information: List[str]
    buyer_hypotheses: List[BuyerHypothesis]
    marketing_opportunities: List[MarketingOpportunity]
    campaign_angles: List[str]
    compliance_warnings: List[str]
    next_best_action: str
