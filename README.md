# MeeMarg (మీమార్గ్)
## AI Navigator for Telangana Government Services

**🏆 Production-Ready | ✅ Fully Automated | 🌐 Live Demo**

Instant access to 30+ Telangana government services with intelligent fuzzy search, bilingual support, and self-healing automation.

[![Live Demo](https://img.shields.io/badge/Live-Demo-brightgreen)](https://meemarg.vercel.app)
[![Auto-Update](https://img.shields.io/badge/Auto--Update-Daily-blue)](#automation)

---

## 🚀 Quick Start

```bash
# Install and run
npm install
npm run dev

# Build for production
npm run build
```

Visit `http://localhost:5173`

---

## ✨ Key Features

### 🔍 Intelligent Search
- **Fuzzy search** with typo tolerance (Fuse.js)
- Search across English + Telugu (తెలుగు)
- Department filtering and smart dropdown

### 📋 Service Cards
- **30+ services** across Revenue, Municipal, Police, Transport, Civil Supplies
- Current fees (April 2026): Category A (₹62), B (₹80), E-Pass (₹35)
- Required documents, processing times, submission modes
- **Smart alerts** for ₹2 Court Stamp requirements

### 🤖 Self-Healing Automation
- **Daily auto-updates** at 2:00 AM IST via GitHub Actions
- Scout Agent monitors Telangana portals for changes
- Auto-commits → Vercel auto-deploys
- Zero manual maintenance

### 📱 User Experience
- Responsive design (desktop, tablet, mobile)
- Bilingual interface (English + Telugu)
- Direct portal links for online submission
- Clear Online vs MeeSeva guidance

---

## 🏗️ Architecture

```
React + Tailwind Frontend
    ↓
services.json (Single Source of Truth)
    ↓
Scout Agent (Daily Monitoring)
    ↓
GitHub Actions → Vercel Auto-Deploy
```

---

## 📁 Project Structure

```
MeeMarg/
├── src/
│   ├── components/
│   │   ├── SearchBar.jsx      # Fuzzy search + filters
│   │   └── ServiceCard.jsx    # Readiness cards
│   ├── App.jsx                # Main logic
│   └── index.css              # Tailwind styles
├── public/
│   └── services.json          # Service database
├── scripts/
│   └── scout_agent.py         # Auto-update agent
├── .github/workflows/
│   └── update-data.yml        # Daily automation
└── docs/                      # Detailed documentation
```

---

## 🚀 Deployment

### Vercel (Recommended)
1. Push to GitHub
2. Import repo on [vercel.com](https://vercel.com)
3. Framework: **Vite** | Build: `npm run build` | Output: `dist`
4. Deploy - GitHub Actions handles daily updates

### Manual Build
```bash
npm run build
# Deploy dist/ folder to any static host
```

---

## 🤖 Automation

**Daily Workflow (2:00 AM IST):**
1. Scout Agent scans Telangana portals
2. Detects fee/document changes (85% confidence)
3. Updates `services.json`
4. Auto-commits to GitHub
5. Vercel deploys (2-3 minutes)

**Manual Trigger:**
```bash
cd scripts
python scout_agent.py
```

---

## 🛠️ Tech Stack

- **Frontend**: React 18, Vite, Tailwind CSS
- **Search**: Fuse.js (fuzzy matching)
- **Icons**: Lucide React
- **Automation**: Python, GitHub Actions
- **Deployment**: Vercel
- **Built with**: IBM watsonx Code Assistant

---

## 📊 Service Coverage

| Department | Services | Examples |
|------------|----------|----------|
| Revenue | 10 | Birth Certificate, Encumbrance Certificate |
| Municipal | 8 | Property Tax, Trade License |
| Police | 4 | Character Certificate, Passport Verification |
| Transport | 5 | Driving License, Vehicle Registration |
| Civil Supplies | 3 | Ration Card, LPG Connection |

**Total**: 30+ services (scalable to 400+)

---

## 📚 Documentation

- [`ARCHITECTURE.md`](ARCHITECTURE.md) - System design
- [`DEMO_SCRIPT.md`](DEMO_SCRIPT.md) - 3-minute demo guide
- [`AUTO_UPDATE_SETUP.md`](AUTO_UPDATE_SETUP.md) - Automation details
- [`DEPLOYMENT_INSTRUCTIONS.md`](DEPLOYMENT_INSTRUCTIONS.md) - Deploy guide
- [`docs/`](docs/) - Phase summaries and guides

---

## 🤝 Built With IBM watsonx Code Assistant

This project was architected, developed, and automated with IBM watsonx Code Assistant (Bob):
- Architecture design and data schema
- React components and fuzzy search
- Scout Agent and GitHub Actions
- Comprehensive documentation

---

## 📄 License

MIT License - Built for Telangana citizens with ❤️

---

## 🏆 Status

**Version**: 1.0.0  
**Updated**: May 2026  
**Status**: ✅ Production Ready - All Phases Complete  
**Live**: [meemarg.vercel.app](https://meemarg.vercel.app)

---

**Made with ❤️ for Telangana | Powered by IBM watsonx Code Assistant**
