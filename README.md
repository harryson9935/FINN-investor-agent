# FINN-investor-agent
# FINN — Mobile-First Institutional Investment Agent
*Filter ruthlessly. Surface what matters. Cross-examine primary sources.*

FINN is an intelligent financial investment agent built for institutional workflows. It addresses the core problem equity analysts face: information overload across filings, market movements, concalls, and earnings releases.

## Core Interaction Modes
1. **Push (Filtered Radar & Digest):**
   - **Threshold Triggers:** EOD price deviations (±4%) and volume surges (>=2.0x 20-day MA).
   - **Windowed Digest (6h / 24h / 7d):** Disclosures ranked into Tier 1 (Critical), Tier 2 (Operational), and Tier 3 (Boilerplate - collapsed by default).
   - **Enriched Summaries:** Management changes enriched with executive background; results parsed into QoQ & YoY headline tables (Revenue, EBITDA, PBT, PAT).
2. **Pull (Primary-Source Research Desk):**
   - **Narrative vs. Numbers:** Multi-quarter audit engine matching concall commitments to subsequent statutory delivery (Delivered, Missed, Reframed).
   - **Cash Quality:** Operating cash flow (CFO) to EBITDA conversion ratio and working capital cycle checks.
   - **Bull vs. Bear:** Primary-evidence-backed investment theses.

---

## Repository Structure
```
finn-investor-agent/
├── README.md                      # Setup instructions & architectural design
├── COVERING_NOTE.md               # 1-page institutional evaluation note
├── Dockerfile                     # Containerized backend deployment
├── docker-compose.yml             # Single-command local dev environment
├── requirements.txt               # Backend Python dependencies
├── package.json                   # Frontend dependencies (React + Tailwind)
├── backend/
│   ├── main.py                    # FastAPI REST application
│   ├── config.py                  # Configurable thresholds & ticker universe
│   ├── services/
│   │   ├── market_data.py         # YFinance EOD & volume anomaly detection
│   │   ├── filings_classifier.py  # Regulatory filing tiering & parser
│   │   └── concall_auditor.py     # Narrative vs. Numbers comparison engine
│   └── mock_data/                 # Pre-cached primary filings & concall audits
└── frontend/
    ├── index.html                 # Mobile-first standalone prototype
    ├── vite.config.js             # Vite configuration
    ├── tailwind.config.js         # Tailwind styling setup
    └── src/
        ├── App.jsx                # React Mobile Shell
        ├── main.jsx               # Application entry point
        └── index.css              # Custom utility styling
```

---

## Quickstart (Under 2 Minutes)

### Option 1: Standalone Instant Preview
Open `frontend/index.html` directly in Google Chrome, Safari, or Brave. Toggle Device Emulation (`Cmd + Shift + M` / `Ctrl + Shift + M`) to iPhone 15 Pro / Pixel 8.

### Option 2: Docker Compose
```bash
docker-compose up --build
```
Access backend API at `http://localhost:8000/docs` and mobile web at `http://localhost:3000`.

### Option 3: Local Python & Node Setup
**Backend:**
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r ../requirements.txt
uvicorn main:app --reload --port 8000
```

**Frontend:**
```bash
cd frontend
npm install
npm run dev
```

---

## Research Universe
- **Portfolio (18 NSE Equities):** `HDFCBANK.NS`, `ICICIBANK.NS`, `CREDITACC.NS`, `TCS.NS`, `KPITTECH.NS`, `TITAN.NS`, `TRENT.NS`, `VARUN.NS`, `LT.NS`, `KAYNES.NS`, `AIAENG.NS`, `SUNPHARMA.NS`, `DIVISLAB.NS`, `PIIND.NS`, `TATAMOTORS.NS`, `SONACOMS.NS`, `RELIANCE.NS`, `TATASTEEL.NS`.
- **Ad-Hoc / Generalization Tickers:** `DIXON.NS`, `ZOMATO.NS`, `SUZLON.NS`, `POLYCAB.NS`.
