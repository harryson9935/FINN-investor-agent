from typing import Dict, List
from pydantic import BaseModel

class FilingItem(BaseModel):
    id: str
    ticker: str
    category: str
    headline: str
    tier: int
    published_at: str
    table_data: Dict = {}
    takeaway: str

class FilingClassifier:
    TIER_1_PATTERNS = [
        "financial results", "quarterly results", "resignation of cfo",
        "resignation of ceo", "appointment", "merger", "scheme of arrangement", "forensic"
    ]
    TIER_3_PATTERNS = [
        "trading window", "loss of share", "duplicate share", "newspaper", "esop allotment"
    ]

    @classmethod
    def classify(cls, ticker: str, headline: str) -> int:
        h = headline.lower()
        for p in cls.TIER_1_PATTERNS:
            if p in h:
                return 1
        for p in cls.TIER_3_PATTERNS:
            if p in h:
                return 3
        return 2
