from typing import List, Dict
from pydantic import BaseModel

class ConcallAuditRecord(BaseModel):
    id: str
    metric: str
    guidance: str
    actual: str
    verdict: str  # "DELIVERED" | "MISSED" | "REFRAMED"
    status: str   # "success" | "warning" | "danger"

class ConcallAuditor:
    DATABASE = {
        "TRENT.NS": [
            ConcallAuditRecord(
                id="t1",
                metric="Westside Operating Margin",
                guidance="Q3 FY24 Concall: 'Expect ~11% EBIT margin as domestic supply chains normalize.'",
                actual="Q2 FY25 Audited: Delivered 11.4% EBIT margin.",
                verdict="DELIVERED",
                status="success"
            ),
            ConcallAuditRecord(
                id="t2",
                metric="Star Bazaar Store-Level Breakeven",
                guidance="Q4 FY24 Concall: 'Star Bazaar JV to achieve store-level EBITDA neutrality by mid-FY25.'",
                actual="Q2 FY25 Audited: Target shifted to late FY26 citing store clustering investments.",
                verdict="REFRAMED",
                status="warning"
            ),
            ConcallAuditRecord(
                id="t3",
                metric="Zudio Store Additions",
                guidance="Q1 FY25 Concall: 'Targeting 35-40 gross store additions next quarter.'",
                actual="Q2 FY25 Audited: Added 41 net new retail locations.",
                verdict="DELIVERED",
                status="success"
            )
        ],
        "KAYNES.NS": [
            ConcallAuditRecord(
                id="k1",
                metric="Working Capital Cycle",
                guidance="Q4 FY24 Concall: 'Working capital days targeted to reduce from 125 to sub-100 by Q2 FY25.'",
                actual="Q2 FY25 Audited: Working capital days stood at 112 days.",
                verdict="MISSED",
                status="danger"
            ),
            ConcallAuditRecord(
                id="k2",
                metric="Order Book Inflow Growth",
                guidance="Q1 FY25 Concall: 'Guided >35% YoY order book expansion in EMS and aerospace segments.'",
                actual="Q2 FY25 Audited: Order intake grew 42% YoY to ₹5,400+ Cr.",
                verdict="DELIVERED",
                status="success"
            )
        ]
    }

    @classmethod
    def get_audit(cls, ticker: str) -> List[ConcallAuditRecord]:
        return cls.DATABASE.get(ticker.upper(), [
            ConcallAuditRecord(
                id="gen1",
                metric="Revenue Growth Guidance",
                guidance="Q4 FY24 Concall: 'Targeting 15-18% revenue CAGR over the medium term.'",
                actual="Audited Results: Delivered 16.2% top-line growth.",
                verdict="DELIVERED",
                status="success"
            )
        ])
