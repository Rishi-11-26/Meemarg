# MeeMarg (మీమార్గ్)
## Agentic AI Navigator for Telangana Government Services

A high-performance, citizen-centric web application providing instant access to 30+ Telangana government services with intelligent search and bilingual support.

---

## 🚀 Quick Start

### Prerequisites
- Node.js 18+ 
- npm or yarn

### Installation

```bash
# Install dependencies
npm install

# Start development server
npm run dev

# Build for production
npm run build
```

The app will be available at `http://localhost:3000`

---

## ✨ Features

### Phase 1: Architecture & Data (✅ Complete)
- **Comprehensive Service Database**: 30 most-used Telangana services
- **Bilingual Support**: Full English + Telugu (తెలుగు) interface
- **Smart Categorization**: Services organized by department and priority
- **April 2026 Fee Structure**: Category A (₹62), B (₹80), E-Pass (₹35)

### Phase 2: UI Implementation (✅ Complete)
- **⚡ Lightspeed Fuzzy Search**: Instant results as you type using Fuse.js
- **📋 Dynamic Dropdown**: Browse services by department when search is empty
- **🎯 Readiness Cards**: Clear distinction between Online vs MeeSeva submission
- **⚠️ Smart Alerts**: Automatic ₹2 Court Stamp notifications for Revenue services
- **📱 Responsive Design**: Works seamlessly on desktop, tablet, and mobile

### Phase 3: Self-Healing Agent (🔄 Planned)
- AI-powered monitoring of Telangana State Portal
- Automatic detection of fee changes and new requirements
- JSON schema updates with change logging

---

## 🏗️ Architecture

```
┌─────────────────────────────────────┐
│     React + Tailwind Frontend       │
│  (Fuzzy Search + Dynamic Filters)   │
└─────────────────────────────────────┘
              ↓
┌─────────────────────────────────────┐
│      master_services.json           │
│   (Single Source of Truth - 30+)    │
└─────────────────────────────────────┘
              ↓
┌─────────────────────────────────────┐
│       scout_agent.py (Phase 3)      │
│  (Portal Monitoring & Auto-Update)  │
└─────────────────────────────────────┘
```

---

## 📁 Project Structure

```
MeeMarg/
├── src/
│   ├── components/
│   │   ├── SearchBar.jsx       # Fuzzy search + department filter
│   │   └── ServiceCard.jsx     # Readiness card with submission modes
│   ├── App.jsx                 # Main application logic
│   ├── main.jsx                # React entry point
│   └── index.css               # Tailwind styles
├── data/
│   ├── master_services.json    # Service database
│   └── schema/
│       └── service_schema.json # JSON Schema validation
├── docs/
│   └── PHASE1_SUMMARY.md       # Phase 1 documentation
├── scripts/
│   └── generate_services_data.py # Data generation script
├── ARCHITECTURE.md             # System design document
└── package.json                # Dependencies
```

---

## 🎨 Key Components

### SearchBar Component
- **Fuzzy Search**: Searches across service names (EN/TE), keywords, and departments
- **Department Filter**: Quick filtering by government department
- **Dynamic Dropdown**: Shows all departments when search is empty
- **Debounced Input**: Optimized for performance

### ServiceCard Component (Readiness Card)
- **Submission Modes**: Visual indicators for Online vs MeeSeva availability
- **Revenue Alerts**: Automatic ₹2 stamp notifications
- **Document Checklist**: Required documents with mandatory flags
- **Direct Links**: One-click access to online portals
- **Bilingual Display**: Service names and descriptions in both languages

---

## 📊 Service Coverage

| Department | Services | Priority Range |
|------------|----------|----------------|
| Revenue | 10 | 1-10 |
| Municipal | 8 | 11-18 |
| Police | 4 | 19-22 |
| Transport | 5 | 23-27 |
| Civil Supplies | 3 | 28-30 |

---

## 🔧 Technology Stack

- **Frontend**: React 18, Vite
- **Styling**: Tailwind CSS 3.4
- **Search**: Fuse.js (fuzzy search)
- **Icons**: Lucide React
- **Data**: JSON-based service database

---

## 🎯 Data Guardrails

### Fee Structure (April 2026 Revision)
```javascript
Category A: ₹62
Category B: ₹80
E-Pass: ₹35
```

### Revenue Service Logic
```javascript
if (service.is_revenue && service.submission_modes.meeseva_center.requires_stamp) {
  // Display: "⚠️ ₹2 Court Stamp required for MeeSeva submission"
}
```

---

## 🚀 Deployment

### Build for Production
```bash
npm run build
```

### Preview Production Build
```bash
npm run preview
```

The build output will be in the `dist/` directory, ready for deployment to any static hosting service (Vercel, Netlify, GitHub Pages, etc.).

---

## 📝 Service Schema

Each service in `master_services.json` contains:

```json
{
  "service_id": "REV-001",
  "name": { "en": "...", "te": "..." },
  "department": "Revenue",
  "category": "A",
  "keywords": ["..."],
  "fee": 62,
  "required_documents": [...],
  "processing_time": "Instant",
  "is_revenue": true,
  "description_simple": { "en": "...", "te": "..." },
  "submission_modes": {
    "online": { "available": true, "portal_url": "..." },
    "meeseva_center": { "available": true, "requires_stamp": true }
  },
  "priority_rank": 1
}
```

---

## 🔮 Roadmap

### Phase 3: Self-Healing Agent (Next)
- [ ] Implement `scout_agent.py`
- [ ] Portal scraping for fee changes
- [ ] Gazette monitoring for policy updates
- [ ] Automatic JSON updates with change logs
- [ ] Email notifications for critical changes

### Future Enhancements
- [ ] Multi-language support (Hindi, Urdu)
- [ ] Voice search capability
- [ ] Mobile app (React Native)
- [ ] Chatbot integration
- [ ] Service status tracking
- [ ] Document upload assistance

---

## 📄 License

Built for the citizens of Telangana with ❤️

---

## 👥 Contributing

This is a government service navigator. For suggestions or improvements, please contact the development team.

---

**Version**: 1.0.0  
**Last Updated**: May 2026  
**Status**: Phase 2 Complete ✅