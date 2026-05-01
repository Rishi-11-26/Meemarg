# MeeMarg - Agentic AI Navigator for Telangana Government Services
## Phase 1: Architecture & Data Blueprint

### Executive Summary
MeeMarg is designed as a high-performance, AI-native citizen service navigator that provides instant access to Telangana government services with intelligent search, real-time updates, and self-healing capabilities.

---

## 1. System Architecture Overview

```
┌─────────────────────────────────────────────────────────────┐
│                    CITIZEN INTERFACE LAYER                   │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐      │
│  │ Fuzzy Search │  │   Dropdown   │  │ Readiness    │      │
│  │   Engine     │  │  Navigator   │  │   Cards      │      │
│  └──────────────┘  └──────────────┘  └──────────────┘      │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│                    DATA ORCHESTRATION LAYER                  │
│  ┌──────────────────────────────────────────────────────┐   │
│  │         master_services.json (Single Source of       │   │
│  │              Truth - 30 → 400+ services)             │   │
│  └──────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│                   SELF-HEALING AGENT LAYER                   │
│  ┌──────────────────────────────────────────────────────┐   │
│  │  scout_agent.py - AI-Native Monitoring & Updates    │   │
│  │  • Portal Scraper  • Gazette Watcher  • JSON Patcher│   │
│  └──────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────┘
```

---

## 2. Data Schema Design: master_services.json

### Schema Philosophy
- **Single Source of Truth**: All service metadata in one structured file
- **Scalability**: Designed to grow from 30 to 400+ services seamlessly
- **Bilingual Support**: English + Telugu for citizen accessibility
- **Revenue Intelligence**: Built-in logic for stamp duty requirements

### Core Schema Structure

```json
{
  "metadata": {
    "version": "1.0.0",
    "last_updated": "2026-05-01T11:30:00Z",
    "total_services": 30,
    "rate_revision_date": "2026-04-01",
    "data_source": "Telangana State Portal & Official Gazette"
  },
  "services": [...]
}
```

### Service Object Schema

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `service_id` | string | ✓ | Unique identifier (e.g., "REV-001", "MUN-001") |
| `name` | object | ✓ | Service name in English and Telugu |
| `department` | string | ✓ | Parent department (Revenue, Municipal, Police, etc.) |
| `category` | string | ✓ | Fee category: "A" or "B" |
| `keywords` | array | ✓ | Search terms for fuzzy matching |
| `fee` | number | ✓ | Service fee in INR (₹) |
| `required_documents` | array | ✓ | List of documents needed |
| `processing_time` | string | ✓ | Expected turnaround time |
| `is_revenue` | boolean | ✓ | Triggers ₹2 Court Stamp alert if true |
| `description_simple` | object | ✓ | Plain-language description (English + Telugu) |
| `submission_modes` | object | ✓ | Online vs MeeSeva center details |
| `priority_rank` | number | ✓ | Usage frequency ranking (1-30) |

---

## 3. Data Guardrails & Business Rules

### April 2026 Revised Fee Structure
```
Category A Services: ₹62
Category B Services: ₹80
E-Pass Services: ₹35
```

### Revenue Service Logic
```javascript
if (service.is_revenue === true && service.submission_modes.meeseva_center === true) {
  alert_citizen("⚠️ Additional ₹2 Court Stamp required for MeeSeva Center submission");
}
```

### Document Validation Rules
- All `required_documents` must be from approved list
- Documents marked as "original" require physical verification
- Digital submissions accept scanned copies (PDF, max 5MB per file)

### Processing Time Standards
- **Instant**: Real-time digital certificates (e.g., Encumbrance Certificate)
- **1-3 Days**: Standard services with verification
- **7-15 Days**: Services requiring field inspection
- **30+ Days**: Complex approvals (building permits, etc.)

---

## 4. Scalability Design

### From 30 to 400+ Services
The schema is designed for horizontal scaling:

1. **Modular Structure**: Each service is self-contained
2. **Department Grouping**: Easy to add new departments
3. **Category System**: Extensible beyond A/B (can add C, D, etc.)
4. **Keyword Indexing**: Supports unlimited search terms per service

### Performance Optimization
- **Client-Side Filtering**: All 400 services load once, filter in-memory
- **Lazy Loading**: Readiness Cards render on-demand
- **Search Debouncing**: 300ms delay to reduce re-renders
- **JSON Compression**: Gzip reduces payload by ~70%

---

## 5. Top 30 Services Selection Criteria

Services selected based on:
1. **Citizen Usage Volume** (MeeSeva transaction data)
2. **Revenue Impact** (high-fee services prioritized)
3. **Digital Readiness** (services with online submission capability)
4. **Cross-Department Coverage** (balanced representation)

### Department Distribution
- Revenue: 10 services (33%)
- Municipal: 8 services (27%)
- Transport: 5 services (17%)
- Police: 4 services (13%)
- Civil Supplies: 3 services (10%)

---

## 6. Integration Points

### Phase 2 (UI) Dependencies
- React 18+ with TypeScript
- Tailwind CSS 3.4+
- Fuse.js for fuzzy search
- React Query for state management

### Phase 3 (Agent) Dependencies
- Python 3.11+
- BeautifulSoup4 for scraping
- OpenAI API for change detection
- JSON Schema validation

---

## 7. Security & Compliance

### Data Privacy
- No PII stored in master_services.json
- Document requirements are generic (no citizen-specific data)
- Fee information is public domain

### Update Audit Trail
```json
{
  "change_log": [
    {
      "timestamp": "2026-05-01T10:00:00Z",
      "service_id": "REV-001",
      "field_changed": "fee",
      "old_value": 50,
      "new_value": 62,
      "source": "scout_agent.py",
      "verified_by": "admin"
    }
  ]
}
```

---

## Next Steps

✅ **Phase 1 Complete**: Schema design and architecture documented  
⏳ **Awaiting Approval**: Review schema before generating sample data  
🔜 **Phase 2**: Build React UI with fuzzy search and dynamic dropdown  
🔜 **Phase 3**: Develop self-healing scout_agent.py

---

**Document Version**: 1.0  
**Last Updated**: 2026-05-01  
**Author**: Senior Full-Stack Architect & Data Engineer