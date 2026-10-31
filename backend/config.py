from typing import List, Dict

PRICE_MOVE_THRESHOLD_PCT: float = 4.0
VOLUME_SURGE_RATIO: float = 2.0

PORTFOLIO_TICKERS: List[Dict[str, str]] = [
    {"ticker": "HDFCBANK.NS", "sector": "Banking", "tier": "Large Cap"},
    {"ticker": "ICICIBANK.NS", "sector": "Banking", "tier": "Large Cap"},
    {"ticker": "CREDITACC.NS", "sector": "NBFC/Microfinance", "tier": "Mid Cap"},
    {"ticker": "TCS.NS", "sector": "IT Services", "tier": "Large Cap"},
    {"ticker": "KPITTECH.NS", "sector": "Auto Tech", "tier": "Mid Cap"},
    {"ticker": "TITAN.NS", "sector": "Consumer", "tier": "Large Cap"},
    {"ticker": "TRENT.NS", "sector": "Retail", "tier": "Large Cap"},
    {"ticker": "VARUN.NS", "sector": "Beverages", "tier": "Large Cap"},
    {"ticker": "LT.NS", "sector": "Capital Goods", "tier": "Large Cap"},
    {"ticker": "KAYNES.NS", "sector": "EMS", "tier": "Mid Cap"},
    {"ticker": "AIAENG.NS", "sector": "Industrial", "tier": "Mid Cap"},
    {"ticker": "SUNPHARMA.NS", "sector": "Pharma", "tier": "Large Cap"},
    {"ticker": "DIVISLAB.NS", "sector": "API/Pharma", "tier": "Large Cap"},
    {"ticker": "PIIND.NS", "sector": "Agrochem CSM", "tier": "Mid Cap"},
    {"ticker": "TATAMOTORS.NS", "sector": "Automotive", "tier": "Large Cap"},
    {"ticker": "SONACOMS.NS", "sector": "Auto Ancillary", "tier": "Mid Cap"},
    {"ticker": "RELIANCE.NS", "sector": "Conglomerate", "tier": "Mega Cap"},
    {"ticker": "TATASTEEL.NS", "sector": "Metals", "tier": "Large Cap"}
]

AD_HOC_RESEARCH_TICKERS: List[str] = [
    "DIXON.NS", "ZOMATO.NS", "SUZLON.NS", "POLYCAB.NS"
]
