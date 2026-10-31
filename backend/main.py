from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Dict
from backend.config import PORTFOLIO_TICKERS, AD_HOC_RESEARCH_TICKERS
from backend.services.concall_auditor import ConcallAuditor
import json

app = FastAPI(
    title="FINN Financial Investment Agent API",
    description="High-density filtering and primary-source verification engine for institutional investors.",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def health_check():
    return {"status": "online", "system": "FINN Agent Core", "version": "1.0.0"}

@app.get("/api/portfolio")
def get_portfolio():
    return {"portfolio": PORTFOLIO_TICKERS, "ad_hoc_tickers": AD_HOC_RESEARCH_TICKERS}

@app.get("/api/push/triggers")
def get_triggered_alerts(vol_mult: float = 2.0, price_shift: float = 4.0):
    return [
        {
            "id": "a1",
            "ticker": "KAYNES.NS",
            "tag": "UNUSUAL VOLUME",
            "headline": f"Volume surge 3.4x over 20-Day Average",
            "detail": "Closing at ₹4,820 (+5.8%). Heavy institutional block participation (~420k shares vs ~125k daily run rate).",
            "timestamp": "14:25 IST"
        },
        {
            "id": "a2",
            "ticker": "HDFCBANK.NS",
            "tag": "MANAGEMENT CHANGE",
            "headline": "Head of Wholesale Banking Resigns",
            "detail": "Incoming: K. Venkat (Ex-Standard Chartered, 18 yrs in Corporate Credit & Structured Finance).",
            "timestamp": "11:10 IST"
        }
    ]

@app.get("/api/push/digest")
def get_windowed_digest(window: str = Query("24h", enum=["6h", "24h", "7d"])):
    return {
        "window": window,
        "items": [
            {
                "id": "d1",
                "ticker": "TRENT.NS",
                "title": "Q2 FY25 Headline Financial Results",
                "tier": 1,
                "time": "Today, 12:45 IST",
                "hasTable": True,
                "table": {
                    "revenue": {"val": "₹4,156 Cr", "qoq": "+4.2%", "yoy": "+39.4%"},
                    "ebitda": {"val": "₹610 Cr", "qoq": "-1.8%", "yoy": "+41.2%"},
                    "pbt": {"val": "₹510 Cr", "qoq": "-2.1%", "yoy": "+38.5%"},
                    "pat": {"val": "₹374 Cr", "qoq": "-3.0%", "yoy": "+44.2%"}
                },
                "insight": "Growth powered by 41 net Zudio openings. Operating margin stood at 14.7%, slightly down QoQ due to supply chain scale-up costs."
            },
            {
                "id": "d2",
                "ticker": "TATAMOTORS.NS",
                "title": "Credit Rating Reaffirmation & Outlook Upgrade",
                "tier": 2,
                "time": "Yesterday, 18:20 IST",
                "hasTable": False,
                "insight": "CRISIL upgrades long-term debt rating to AAA (Stable). Cites significant deleveraging in JLR operations."
            },
            {
                "id": "d3",
                "ticker": "TCS.NS",
                "title": "Trading Window Closure for Q3 Board Meeting",
                "tier": 3,
                "time": "Yesterday, 09:15 IST",
                "hasTable": False,
                "insight": "Statutory compliance notification under SEBI (Prohibition of Insider Trading) Regulations."
            }
        ]
    }

@app.get("/api/pull/audit/{ticker}")
def get_concall_audit(ticker: str):
    records = ConcallAuditor.get_audit(ticker)
    return {
        "ticker": ticker.upper(),
        "source": "Primary Earnings Call Transcripts + Audited Exchange Filings",
        "audit_records": records,
        "cash_conversion": {
            "cfo_ebitda_pct": 92.4,
            "working_capital_days": 34,
            "wc_change_yoy": -3
        },
        "thesis": {
            "bull": [
                "Zudio unit economics hold in Tier 3/4 towns with <18 month payback.",
                "Negative working capital in flagship fast-fashion formats."
            ],
            "bear": [
                "Same-store sales growth (SSSG) moderation risk as store density increases.",
                "Valuation multiple leaves minimal margin of safety for supply disruptions."
            ]
        }
    }
