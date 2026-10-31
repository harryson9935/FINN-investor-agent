# FINN: Executive Covering Note
**Challenge Submission:** ENAM Holdings Pvt. Ltd. — Mobile-First Financial Investment Agent

---

### 1. The Core Philosophy: Filtering, Not Aggregating
Every financial terminal aggregates data. The true bottleneck for modern portfolio managers and research analysts is cognitive bandwidth: distinguishing market noise from structural corporate inflection points. FINN was designed from first principles to enforce a disciplined attention hierarchy:
- **Tier 1 (Material Events):** Earnings releases, C-suite changes, forensic notices, and large capital allocations are surfaced proactively. Routine disclosures (trading window closures, loss of share certificates, investor presentation uploads) are suppressed into a collapsible drawer.
- **Contextual Enrichment:** When a CFO resigns, FINN parses the incoming appointee's historical background. When quarterly results land, FINN computes QoQ and YoY delta grids across Revenue, EBITDA, PBT, and PAT instead of dumping a 90-page PDF.

### 2. The Core Differentiator: Primary-Source "Narrative vs. Numbers"
Most retail AI tools generate generic summaries by ingesting secondary blogs or news commentary. FINN's Pull Engine enforces a strict primary-source discipline: **Audited Annual Reports & Earnings Call Transcripts only.**

Our flagship audit engine tracks multi-quarter executive promises:
- Extracts explicit management guidance from historic transcripts (margin targets, capex cycles, breakeven milestones).
- Cross-references each statement against subsequent audited statutory disclosures.
- Classifies the management track record as **DELIVERED**, **MISSED**, or **REFRAMED**.

### 3. Architecture & Cost Optimization
To deliver high performance within free-tier compute boundaries:
- **Deterministic Pre-filtering:** Rule-based regex handles 80%+ of routine NSE/BSE announcements with zero model invocation cost.
- **Two-Tier LLM Routing:** Compact models (e.g. Claude 3.5 Haiku / GPT-4o-mini) extract metric matrices; frontier reasoning models are reserved strictly for concall cross-examination.
- **Immutable Caching:** Historical transcripts and audited annual filings are immutable; their processed embeddings and audit trees are stored permanently in local DuckDB/SQLite cache, avoiding redundant token spend.
