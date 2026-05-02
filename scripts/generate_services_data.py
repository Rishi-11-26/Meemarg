#!/usr/bin/env python3
"""
Generate master_services.json with TOP 30 Telangana Government Services
This script creates the complete service data following the schema requirements.
"""

import json
from datetime import datetime

def generate_master_services():
    """Generate the complete master services data structure"""
    
    data = {
        "metadata": {
            "version": "1.0.0",
            "last_updated": datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
            "total_services": 30,
            "rate_revision_date": "2026-04-01",
            "data_source": "Telangana State Portal & Official Gazette"
        },
        "services": [],
        "change_log": []
    }
    
    # Revenue Services (10 services - Priority 1-10)
    revenue_services = [
        {
            "service_id": "REV-001",
            "name": {"en": "Encumbrance Certificate", "te": "భారము లేని ధృవీకరణ పత్రం"},
            "department": "Revenue",
            "category": "A",
            "keywords": ["EC", "encumbrance", "property", "land", "certificate", "no dues", "భారము", "సర్టిఫికేట్"],
            "fee": 62,
            "required_documents": [
                {"name": {"en": "Property Document", "te": "ఆస్తి పత్రం"}, "type": "copy", "mandatory": True},
                {"name": {"en": "Applicant ID Proof", "te": "దరఖాస్తుదారు గుర్తింపు రుజువు"}, "type": "self_attested", "mandatory": True}
            ],
            "processing_time": "Instant",
            "is_revenue": True,
            "description_simple": {
                "en": "Certificate showing property is free from legal or monetary liabilities. Required for property transactions.",
                "te": "ఆస్తి చట్టపరమైన లేదా ద్రవ్య బాధ్యతల నుండి విముక్తమని చూపించే ధృవీకరణ పత్రం. ఆస్తి లావాదేవీలకు అవసరం."
            },
            "submission_modes": {
                "online": {"available": True, "portal_url": "https://registration.telangana.gov.in", "requires_digital_signature": False},
                "meeseva_center": {"available": True, "requires_stamp": True, "stamp_value": 2}
            },
            "priority_rank": 1,
            "related_services": ["REV-002", "REV-003"]
        },
        {
            "service_id": "REV-002",
            "name": {"en": "Land Conversion Certificate", "te": "భూమి మార్పిడి ధృవీకరణ పత్రం"},
            "department": "Revenue",
            "category": "B",
            "keywords": ["land conversion", "agricultural to non-agricultural", "LRS", "layout", "భూమి మార్పిడి"],
            "fee": 80,
            "required_documents": [
                {"name": {"en": "Land Ownership Documents", "te": "భూమి యాజమాన్య పత్రాలు"}, "type": "original", "mandatory": True},
                {"name": {"en": "Survey Map", "te": "సర్వే మ్యాప్"}, "type": "copy", "mandatory": True},
                {"name": {"en": "Pattadar Passbook", "te": "పట్టాదార్ పాస్‌బుక్"}, "type": "copy", "mandatory": True}
            ],
            "processing_time": "7-15 Days",
            "is_revenue": True,
            "description_simple": {
                "en": "Permission to convert agricultural land to non-agricultural use for construction or commercial purposes.",
                "te": "నిర్మాణం లేదా వాణిజ్య ప్రయోజనాల కోసం వ్యవసాయ భూమిని వ్యవసాయేతర వినియోగానికి మార్చడానికి అనుమతి."
            },
            "submission_modes": {
                "online": {"available": True, "portal_url": "https://dharani.telangana.gov.in", "requires_digital_signature": False},
                "meeseva_center": {"available": True, "requires_stamp": True, "stamp_value": 2}
            },
            "priority_rank": 2,
            "related_services": ["REV-001", "REV-004"]
        },
        {
            "service_id": "REV-003",
            "name": {"en": "Caste Certificate", "te": "కులం ధృవీకరణ పత్రం"},
            "department": "Revenue",
            "category": "A",
            "keywords": ["caste", "SC", "ST", "BC", "OBC", "reservation", "కులం", "కుల ధృవీకరణ"],
            "fee": 62,
            "required_documents": [
                {"name": {"en": "Ration Card", "te": "రేషన్ కార్డు"}, "type": "copy", "mandatory": True},
                {"name": {"en": "Aadhar Card", "te": "ఆధార్ కార్డు"}, "type": "self_attested", "mandatory": True},
                {"name": {"en": "Parent's Caste Certificate (if available)", "te": "తల్లిదండ్రుల కుల ధృవీకరణ పత్రం (అందుబాటులో ఉంటే)"}, "type": "copy", "mandatory": False}
            ],
            "processing_time": "3-7 Days",
            "is_revenue": True,
            "description_simple": {
                "en": "Official certificate verifying caste status for educational admissions, government jobs, and reservations.",
                "te": "విద్యా ప్రవేశాలు, ప్రభుత్వ ఉద్యోగాలు మరియు రిజర్వేషన్ల కోసం కుల స్థితిని ధృవీకరించే అధికారిక ధృవీకరణ పత్రం."
            },
            "submission_modes": {
                "online": {"available": True, "portal_url": "https://meeseva.telangana.gov.in", "requires_digital_signature": False},
                "meeseva_center": {"available": True, "requires_stamp": True, "stamp_value": 2}
            },
            "priority_rank": 3,
            "related_services": ["REV-005", "REV-006"]
        },
        {
            "service_id": "REV-004",
            "name": {"en": "Income Certificate", "te": "ఆదాయ ధృవీకరణ పత్రం"},
            "department": "Revenue",
            "category": "A",
            "keywords": ["income", "salary", "annual income", "EWS", "scholarship", "ఆదాయం", "జీతం"],
            "fee": 62,
            "required_documents": [
                {"name": {"en": "Salary Slips / Income Proof", "te": "జీతం స్లిప్‌లు / ఆదాయ రుజువు"}, "type": "copy", "mandatory": True},
                {"name": {"en": "Ration Card", "te": "రేషన్ కార్డు"}, "type": "copy", "mandatory": True},
                {"name": {"en": "Aadhar Card", "te": "ఆధార్ కార్డు"}, "type": "self_attested", "mandatory": True}
            ],
            "processing_time": "3-5 Days",
            "is_revenue": True,
            "description_simple": {
                "en": "Certificate stating annual family income for scholarships, fee concessions, and government schemes.",
                "te": "స్కాలర్‌షిప్‌లు, ఫీజు రాయితీలు మరియు ప్రభుత్వ పథకాల కోసం వార్షిక కుటుంబ ఆదాయాన్ని తెలిపే ధృవీకరణ పత్రం."
            },
            "submission_modes": {
                "online": {"available": True, "portal_url": "https://meeseva.telangana.gov.in", "requires_digital_signature": False},
                "meeseva_center": {"available": True, "requires_stamp": True, "stamp_value": 2}
            },
            "priority_rank": 4,
            "related_services": ["REV-003", "REV-005"]
        },
        {
            "service_id": "REV-005",
            "name": {"en": "Residence Certificate", "te": "నివాస ధృవీకరణ పత్రం"},
            "department": "Revenue",
            "category": "A",
            "keywords": ["residence", "domicile", "address proof", "bonafide", "నివాసం", "చిరునామా"],
            "fee": 62,
            "required_documents": [
                {"name": {"en": "Electricity Bill / Water Bill", "te": "విద్యుత్ బిల్లు / నీటి బిల్లు"}, "type": "copy", "mandatory": True},
                {"name": {"en": "Ration Card", "te": "రేషన్ కార్డు"}, "type": "copy", "mandatory": True},
                {"name": {"en": "Aadhar Card", "te": "ఆధార్ కార్డు"}, "type": "self_attested", "mandatory": True}
            ],
            "processing_time": "3-5 Days",
            "is_revenue": True,
            "description_simple": {
                "en": "Certificate proving residence in Telangana for admissions, jobs, and government benefits.",
                "te": "ప్రవేశాలు, ఉద్యోగాలు మరియు ప్రభుత్వ ప్రయోజనాల కోసం తెలంగాణలో నివాసాన్ని రుజువు చేసే ధృవీకరణ పత్రం."
            },
            "submission_modes": {
                "online": {"available": True, "portal_url": "https://meeseva.telangana.gov.in", "requires_digital_signature": False},
                "meeseva_center": {"available": True, "requires_stamp": True, "stamp_value": 2}
            },
            "priority_rank": 5,
            "related_services": ["REV-003", "REV-004"]
        },
        {
            "service_id": "REV-006",
            "name": {"en": "Birth Certificate", "te": "జనన ధృవీకరణ పత్రం"},
            "department": "Revenue",
            "category": "A",
            "keywords": ["birth", "birth certificate", "newborn", "registration", "జననం", "పుట్టిన తేదీ"],
            "fee": 62,
            "required_documents": [
                {"name": {"en": "Hospital Discharge Summary", "te": "ఆసుపత్రి డిశ్చార్జ్ సారాంశం"}, "type": "original", "mandatory": True},
                {"name": {"en": "Parents' Aadhar Cards", "te": "తల్లిదండ్రుల ఆధార్ కార్డులు"}, "type": "copy", "mandatory": True}
            ],
            "processing_time": "1-3 Days",
            "is_revenue": True,
            "description_simple": {
                "en": "Official birth registration certificate required for school admissions and passport applications.",
                "te": "పాఠశాల ప్రవేశాలు మరియు పాస్‌పోర్ట్ దరఖాస్తుల కోసం అవసరమైన అధికారిక జనన నమోదు ధృవీకరణ పత్రం."
            },
            "submission_modes": {
                "online": {"available": True, "portal_url": "https://meeseva.telangana.gov.in", "requires_digital_signature": False},
                "meeseva_center": {"available": True, "requires_stamp": True, "stamp_value": 2}
            },
            "priority_rank": 6,
            "related_services": ["REV-007"]
        },
        {
            "service_id": "REV-007",
            "name": {"en": "Death Certificate", "te": "మరణ ధృవీకరణ పత్రం"},
            "department": "Revenue",
            "category": "A",
            "keywords": ["death", "death certificate", "deceased", "మరణం", "మరణించిన"],
            "fee": 62,
            "required_documents": [
                {"name": {"en": "Hospital Death Summary / Medical Certificate", "te": "ఆసుపత్రి మరణ సారాంశం / వైద్య ధృవీకరణ పత్రం"}, "type": "original", "mandatory": True},
                {"name": {"en": "Deceased's Aadhar Card", "te": "మరణించిన వ్యక్తి ఆధార్ కార్డు"}, "type": "copy", "mandatory": True}
            ],
            "processing_time": "1-3 Days",
            "is_revenue": True,
            "description_simple": {
                "en": "Official death registration certificate required for legal and property matters.",
                "te": "చట్టపరమైన మరియు ఆస్తి విషయాల కోసం అవసరమైన అధికారిక మరణ నమోదు ధృవీకరణ పత్రం."
            },
            "submission_modes": {
                "online": {"available": True, "portal_url": "https://meeseva.telangana.gov.in", "requires_digital_signature": False},
                "meeseva_center": {"available": True, "requires_stamp": True, "stamp_value": 2}
            },
            "priority_rank": 7,
            "related_services": ["REV-006"]
        },
        {
            "service_id": "REV-008",
            "name": {"en": "Pattadar Passbook", "te": "పట్టాదార్ పాస్‌బుక్"},
            "department": "Revenue",
            "category": "A",
            "keywords": ["pattadar", "passbook", "land records", "pahani", "పట్టాదార్", "భూ రికార్డులు"],
            "fee": 62,
            "required_documents": [
                {"name": {"en": "Survey Number Details", "te": "సర్వే నంబర్ వివరాలు"}, "type": "copy", "mandatory": True},
                {"name": {"en": "Applicant ID Proof", "te": "దరఖాస్తుదారు గుర్తింపు రుజువు"}, "type": "self_attested", "mandatory": True}
            ],
            "processing_time": "3-7 Days",
            "is_revenue": True,
            "description_simple": {
                "en": "Land ownership record book containing details of agricultural land holdings.",
                "te": "వ్యవసాయ భూ హోల్డింగ్‌ల వివరాలను కలిగి ఉన్న భూ యాజమాన్య రికార్డు పుస్తకం."
            },
            "submission_modes": {
                "online": {"available": True, "portal_url": "https://dharani.telangana.gov.in", "requires_digital_signature": False},
                "meeseva_center": {"available": True, "requires_stamp": True, "stamp_value": 2}
            },
            "priority_rank": 8,
            "related_services": ["REV-001", "REV-002"]
        },
        {
            "service_id": "REV-009",
            "name": {"en": "Mutation of Land Records", "te": "భూ రికార్డుల మార్పు"},
            "department": "Revenue",
            "category": "B",
            "keywords": ["mutation", "land transfer", "name change", "property transfer", "మ్యుటేషన్", "భూ బదిలీ"],
            "fee": 80,
            "required_documents": [
                {"name": {"en": "Sale Deed / Gift Deed", "te": "అమ్మకపు పత్రం / బహుమతి పత్రం"}, "type": "original", "mandatory": True},
                {"name": {"en": "Previous Pattadar Passbook", "te": "మునుపటి పట్టాదార్ పాస్‌బుక్"}, "type": "copy", "mandatory": True},
                {"name": {"en": "Encumbrance Certificate", "te": "భారము లేని ధృవీకరణ పత్రం"}, "type": "copy", "mandatory": True}
            ],
            "processing_time": "7-15 Days",
            "is_revenue": True,
            "description_simple": {
                "en": "Transfer of land ownership records from seller to buyer after property transaction.",
                "te": "ఆస్తి లావాదేవీ తర్వాత విక్రేత నుండి కొనుగోలుదారుకు భూ యాజమాన్య రికార్డుల బదిలీ."
            },
            "submission_modes": {
                "online": {"available": True, "portal_url": "https://dharani.telangana.gov.in", "requires_digital_signature": False},
                "meeseva_center": {"available": True, "requires_stamp": True, "stamp_value": 2}
            },
            "priority_rank": 9,
            "related_services": ["REV-001", "REV-008"]
        },
        {
            "service_id": "REV-010",
            "name": {"en": "Agricultural Land Loan Eligibility Certificate", "te": "వ్యవసాయ భూ రుణ అర్హత ధృవీకరణ పత్రం"},
            "department": "Revenue",
            "category": "A",
            "keywords": ["loan", "agricultural loan", "kisan credit", "crop loan", "రుణం", "వ్యవసాయ రుణం"],
            "fee": 62,
            "required_documents": [
                {"name": {"en": "Pattadar Passbook", "te": "పట్టాదార్ పాస్‌బుక్"}, "type": "copy", "mandatory": True},
                {"name": {"en": "Aadhar Card", "te": "ఆధార్ కార్డు"}, "type": "self_attested", "mandatory": True},
                {"name": {"en": "Bank Account Details", "te": "బ్యాంక్ ఖాతా వివరాలు"}, "type": "copy", "mandatory": True}
            ],
            "processing_time": "3-5 Days",
            "is_revenue": True,
            "description_simple": {
                "en": "Certificate verifying land ownership for obtaining agricultural loans from banks.",
                "te": "బ్యాంకుల నుండి వ్యవసాయ రుణాలు పొందడానికి భూ యాజమాన్యాన్ని ధృవీకరించే ధృవీకరణ పత్రం."
            },
            "submission_modes": {
                "online": {"available": True, "portal_url": "https://meeseva.telangana.gov.in", "requires_digital_signature": False},
                "meeseva_center": {"available": True, "requires_stamp": True, "stamp_value": 2}
            },
            "priority_rank": 10,
            "related_services": ["REV-008"]
        }
    ]
    
    # Municipal Services (8 services - Priority 11-18)
    municipal_services = [
        {
            "service_id": "MUN-001",
            "name": {"en": "Property Tax Payment", "te": "ఆస్తి పన్ను చెల్లింపు"},
            "department": "Municipal",
            "category": "A",
            "keywords": ["property tax", "house tax", "municipal tax", "GHMC", "ఆస్తి పన్ను", "ఇల్లు పన్ను"],
            "fee": 62,
            "required_documents": [
                {"name": {"en": "Property Tax Assessment Number", "te": "ఆస్తి పన్ను అంచనా సంఖ్య"}, "type": "digital", "mandatory": True},
                {"name": {"en": "Property Ownership Proof", "te": "ఆస్తి యాజమాన్య రుజువు"}, "type": "copy", "mandatory": False}
            ],
            "processing_time": "Instant",
            "is_revenue": False,
            "description_simple": {
                "en": "Annual property tax payment for residential and commercial properties in municipal limits.",
                "te": "మునిసిపల్ పరిమితుల్లో నివాస మరియు వాణిజ్య ఆస్తుల కోసం వార్షిక ఆస్తి పన్ను చెల్లింపు."
            },
            "submission_modes": {
                "online": {"available": True, "portal_url": "https://ghmc.gov.in/propertytax", "requires_digital_signature": False},
                "meeseva_center": {"available": True, "requires_stamp": False, "stamp_value": 0}
            },
            "priority_rank": 11,
            "related_services": ["MUN-002"]
        },
        {
            "service_id": "MUN-002",
            "name": {"en": "Building Permission", "te": "భవన అనుమతి"},
            "department": "Municipal",
            "category": "B",
            "keywords": ["building permission", "construction approval", "plan approval", "GHMC approval", "భవన అనుమతి"],
            "fee": 80,
            "required_documents": [
                {"name": {"en": "Site Plan", "te": "సైట్ ప్లాన్"}, "type": "original", "mandatory": True},
                {"name": {"en": "Structural Design", "te": "నిర్మాణ రూపకల్పన"}, "type": "original", "mandatory": True},
                {"name": {"en": "Land Ownership Documents", "te": "భూమి యాజమాన్య పత్రాలు"}, "type": "copy", "mandatory": True},
                {"name": {"en": "NOC from Fire Department", "te": "అగ్నిమాపక విభాగం నుండి NOC"}, "type": "original", "mandatory": True}
            ],
            "processing_time": "30-45 Days",
            "is_revenue": False,
            "description_simple": {
                "en": "Official approval required before starting construction of residential or commercial buildings.",
                "te": "నివాస లేదా వాణిజ్య భవనాల నిర్మాణం ప్రారంభించే ముందు అవసరమైన అధికారిక ఆమోదం."
            },
            "submission_modes": {
                "online": {"available": True, "portal_url": "https://bpass.telangana.gov.in", "requires_digital_signature": True},
                "meeseva_center": {"available": True, "requires_stamp": False, "stamp_value": 0}
            },
            "priority_rank": 12,
            "related_services": ["MUN-003"]
        },
        {
            "service_id": "MUN-003",
            "name": {"en": "Trade License", "te": "వాణిజ్య లైసెన్స్"},
            "department": "Municipal",
            "category": "A",
            "keywords": ["trade license", "business license", "shop license", "commercial license", "వాణిజ్య లైసెన్స్"],
            "fee": 62,
            "required_documents": [
                {"name": {"en": "Shop/Establishment Proof", "te": "దుకాణం/స్థాపన రుజువు"}, "type": "copy", "mandatory": True},
                {"name": {"en": "Owner ID Proof", "te": "యజమాని గుర్తింపు రుజువు"}, "type": "self_attested", "mandatory": True},
                {"name": {"en": "Fire Safety Certificate", "te": "అగ్ని భద్రత ధృవీకరణ పత్రం"}, "type": "copy", "mandatory": False}
            ],
            "processing_time": "7-10 Days",
            "is_revenue": False,
            "description_simple": {
                "en": "License required to operate commercial establishments, shops, and businesses in municipal areas.",
                "te": "మునిసిపల్ ప్రాంతాల్లో వాణిజ్య స్థాపనలు, దుకాణాలు మరియు వ్యాపారాలను నిర్వహించడానికి అవసరమైన లైసెన్స్."
            },
            "submission_modes": {
                "online": {"available": True, "portal_url": "https://ghmc.gov.in/tradelicense", "requires_digital_signature": False},
                "meeseva_center": {"available": True, "requires_stamp": False, "stamp_value": 0}
            },
            "priority_rank": 13,
            "related_services": ["MUN-002"]
        },
        {
            "service_id": "MUN-004",
            "name": {"en": "Water Connection", "te": "నీటి కనెక్షన్"},
            "department": "Municipal",
            "category": "A",
            "keywords": ["water connection", "water supply", "HMWS&SB", "tap connection", "నీటి కనెక్షన్"],
            "fee": 62,
            "required_documents": [
                {"name": {"en": "Property Ownership Proof", "te": "ఆస్తి యాజమాన్య రుజువు"}, "type": "copy", "mandatory": True},
                {"name": {"en": "Aadhar Card", "te": "ఆధార్ కార్డు"}, "type": "self_attested", "mandatory": True},
                {"name": {"en": "Site Plan", "te": "సైట్ ప్లాన్"}, "type": "copy", "mandatory": True}
            ],
            "processing_time": "10-15 Days",
            "is_revenue": False,
            "description_simple": {
                "en": "New water supply connection for residential and commercial properties.",
                "te": "నివాస మరియు వాణిజ్య ఆస్తుల కోసం కొత్త నీటి సరఫరా కనెక్షన్."
            },
            "submission_modes": {
                "online": {"available": True, "portal_url": "https://hmwssb.telangana.gov.in", "requires_digital_signature": False},
                "meeseva_center": {"available": True, "requires_stamp": False, "stamp_value": 0}
            },
            "priority_rank": 14,
            "related_services": ["MUN-005"]
        },
        {
            "service_id": "MUN-005",
            "name": {"en": "Sewerage Connection", "te": "మురుగునీటి కనెక్షన్"},
            "department": "Municipal",
            "category": "A",
            "keywords": ["sewerage", "drainage", "sanitation", "మురుగునీరు", "పారుదల"],
            "fee": 62,
            "required_documents": [
                {"name": {"en": "Property Ownership Proof", "te": "ఆస్తి యాజమాన్య రుజువు"}, "type": "copy", "mandatory": True},
                {"name": {"en": "Water Connection Proof", "te": "నీటి కనెక్షన్ రుజువు"}, "type": "copy", "mandatory": True},
                {"name": {"en": "Site Plan", "te": "సైట్ ప్లాన్"}, "type": "copy", "mandatory": True}
            ],
            "processing_time": "10-15 Days",
            "is_revenue": False,
            "description_simple": {
                "en": "Sewerage connection for proper waste water disposal from residential and commercial properties.",
                "te": "నివాస మరియు వాణిజ్య ఆస్తుల నుండి సరైన వ్యర్థ నీటి పారవేయడం కోసం మురుగునీటి కనెక్షన్."
            },
            "submission_modes": {
                "online": {"available": True, "portal_url": "https://hmwssb.telangana.gov.in", "requires_digital_signature": False},
                "meeseva_center": {"available": True, "requires_stamp": False, "stamp_value": 0}
            },
            "priority_rank": 15,
            "related_services": ["MUN-004"]
        },
        {
            "service_id": "MUN-006",
            "name": {"en": "Birth Certificate Correction", "te": "జనన ధృవీకరణ పత్రం దిద్దుబాటు"},
            "department": "Municipal",
            "category": "A",
            "keywords": ["birth correction", "name change", "date correction", "జనన దిద్దుబాటు"],
            "fee": 62,
            "required_documents": [
                {"name": {"en": "Original Birth Certificate", "te": "అసలు జనన ధృవీకరణ పత్రం"}, "type": "original", "mandatory": True},
                {"name": {"en": "Affidavit for Correction", "te": "దిద్దుబాటు కోసం అఫిడవిట్"}, "type": "original", "mandatory": True},
                {"name": {"en": "Supporting Documents", "te": "సహాయక పత్రాలు"}, "type": "copy", "mandatory": True}
            ],
            "processing_time": "7-10 Days",
            "is_revenue": False,
            "description_simple": {
                "en": "Correction of errors in birth certificate such as name spelling, date of birth, or parent names.",
                "te": "పేరు స్పెల్లింగ్, పుట్టిన తేదీ లేదా తల్లిదండ్రుల పేర్లు వంటి జనన ధృవీకరణ పత్రంలో లోపాల దిద్దుబాటు."
            },
            "submission_modes": {
                "online": {"available": True, "portal_url": "https://meeseva.telangana.gov.in", "requires_digital_signature": False},
                "meeseva_center": {"available": True, "requires_stamp": False, "stamp_value": 0}
            },
            "priority_rank": 16,
            "related_services": ["REV-006"]
        },
        {
            "service_id": "MUN-007",
            "name": {"en": "Death Certificate Correction", "te": "మరణ ధృవీకరణ పత్రం దిద్దుబాటు"},
            "department": "Municipal",
            "category": "A",
            "keywords": ["death correction", "name change", "date correction", "మరణ దిద్దుబాటు"],
            "fee": 62,
            "required_documents": [
                {"name": {"en": "Original Death Certificate", "te": "అసలు మరణ ధృవీకరణ పత్రం"}, "type": "original", "mandatory": True},
                {"name": {"en": "Affidavit for Correction", "te": "దిద్దుబాటు కోసం అఫిడవిట్"}, "type": "original", "mandatory": True},
                {"name": {"en": "Supporting Documents", "te": "సహాయక పత్రాలు"}, "type": "copy", "mandatory": True}
            ],
            "processing_time": "7-10 Days",
            "is_revenue": False,
            "description_simple": {
                "en": "Correction of errors in death certificate such as name spelling, date of death, or cause of death.",
                "te": "పేరు స్పెల్లింగ్, మరణ తేదీ లేదా మరణ కారణం వంటి మరణ ధృవీకరణ పత్రంలో లోపాల దిద్దుబాటు."
            },
            "submission_modes": {
                "online": {"available": True, "portal_url": "https://meeseva.telangana.gov.in", "requires_digital_signature": False},
                "meeseva_center": {"available": True, "requires_stamp": False, "stamp_value": 0}
            },
            "priority_rank": 17,
            "related_services": ["REV-007"]
        },
        {
            "service_id": "MUN-008",
            "name": {"en": "Street Light Complaint", "te": "వీధి దీపం ఫిర్యాదు"},
            "department": "Municipal",
            "category": "E-Pass",
            "keywords": ["street light", "lamp post", "lighting", "వీధి దీపం", "లైటింగ్"],
            "fee": 35,
            "required_documents": [
                {"name": {"en": "Location Details", "te": "స్థాన వివరాలు"}, "type": "digital", "mandatory": True},
                {"name": {"en": "Photo of Issue (optional)", "te": "సమస్య ఫోటో (ఐచ్ఛికం)"}, "type": "digital", "mandatory": False}
            ],
            "processing_time": "1-3 Days",
            "is_revenue": False,
            "description_simple": {
                "en": "Report non-functional street lights for repair and maintenance.",
                "te": "మరమ్మత్తు మరియు నిర్వహణ కోసం పనిచేయని వీధి దీపాలను నివేదించండి."
            },
            "submission_modes": {
                "online": {"available": True, "portal_url": "https://ghmc.gov.in/complaints", "requires_digital_signature": False},
                "meeseva_center": {"available": True, "requires_stamp": False, "stamp_value": 0}
            },
            "priority_rank": 18,
            "related_services": []
        }
    ]
    
    # Police Services (4 services - Priority 19-22)
    police_services = [
    # Generate the data
    services_data = generate_master_services()
    
    # Write to file with proper formatting
    output_path = "../data/master_services.json"
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(services_data, f, ensure_ascii=False, indent=2)
    
    print(f"✅ Generated {services_data['metadata']['total_services']} services")
    print(f"📁 Output: {output_path}")
    print(f"📊 File size: {len(json.dumps(services_data, ensure_ascii=False))} bytes")

# Made with Bob

    
    # Police Services (4 services - Priority 19-22)
    police_services = [
        {
            "service_id": "POL-001",
            "name": {"en": "Police Clearance Certificate", "te": "పోలీసు క్లియరెన్స్ ధృవీకరణ పత్రం"},
            "department": "Police",
            "category": "A",
            "keywords": ["police clearance", "character certificate", "PCC", "passport", "పోలీసు క్లియరెన్స్"],
            "fee": 62,
            "required_documents": [
                {"name": {"en": "Aadhar Card", "te": "ఆధార్ కార్డు"}, "type": "self_attested", "mandatory": True},
                {"name": {"en": "Address Proof", "te": "చిరునామా రుజువు"}, "type": "copy", "mandatory": True},
                {"name": {"en": "Passport Copy (if applicable)", "te": "పాస్‌పోర్ట్ కాపీ (వర్తించినట్లయితే)"}, "type": "copy", "mandatory": False}
            ],
            "processing_time": "7-15 Days",
            "is_revenue": False,
            "description_simple": {
                "en": "Certificate verifying no criminal record, required for passport, visa, and employment abroad.",
                "te": "పాస్‌పోర్ట్, వీసా మరియు విదేశాల్లో ఉద్యోగం కోసం అవసరమైన నేర రికార్డు లేదని ధృవీకరించే ధృవీకరణ పత్రం."
            },
            "submission_modes": {
                "online": {"available": True, "portal_url": "https://tspolice.gov.in", "requires_digital_signature": False},
                "meeseva_center": {"available": True, "requires_stamp": False, "stamp_value": 0}
            },
            "priority_rank": 19,
            "related_services": []
        },
        {
            "service_id": "POL-002",
            "name": {"en": "Passport Verification", "te": "పాస్‌పోర్ట్ ధృవీకరణ"},
            "department": "Police",
            "category": "A",
            "keywords": ["passport verification", "police verification", "పాస్‌పోర్ట్ ధృవీకరణ"],
            "fee": 62,
            "required_documents": [
                {"name": {"en": "Passport Application Copy", "te": "పాస్‌పోర్ట్ దరఖాస్తు కాపీ"}, "type": "copy", "mandatory": True},
                {"name": {"en": "Address Proof", "te": "చిరునామా రుజువు"}, "type": "copy", "mandatory": True},
                {"name": {"en": "Aadhar Card", "te": "ఆధార్ కార్డు"}, "type": "self_attested", "mandatory": True}
            ],
            "processing_time": "7-10 Days",
            "is_revenue": False,
            "description_simple": {
                "en": "Police verification of address and background for passport issuance.",
                "te": "పాస్‌పోర్ట్ జారీ కోసం చిరునామా మరియు నేపథ్యం యొక్క పోలీసు ధృవీకరణ."
            },
            "submission_modes": {
                "online": {"available": True, "portal_url": "https://tspolice.gov.in", "requires_digital_signature": False},
                "meeseva_center": {"available": True, "requires_stamp": False, "stamp_value": 0}
            },
            "priority_rank": 20,
            "related_services": ["POL-001"]
        },
        {
            "service_id": "POL-003",
            "name": {"en": "FIR Copy", "te": "FIR కాపీ"},
            "department": "Police",
            "category": "E-Pass",
            "keywords": ["FIR", "first information report", "complaint copy", "FIR కాపీ"],
            "fee": 35,
            "required_documents": [
                {"name": {"en": "FIR Number", "te": "FIR నంబర్"}, "type": "digital", "mandatory": True},
                {"name": {"en": "Applicant ID Proof", "te": "దరఖాస్తుదారు గుర్తింపు రుజువు"}, "type": "self_attested", "mandatory": True}
            ],
            "processing_time": "1-3 Days",
            "is_revenue": False,
            "description_simple": {
                "en": "Copy of First Information Report filed at police station for legal and insurance purposes.",
                "te": "చట్టపరమైన మరియు బీమా ప్రయోజనాల కోసం పోలీసు స్టేషన్‌లో దాఖలు చేసిన మొదటి సమాచార నివేదిక కాపీ."
            },
            "submission_modes": {
                "online": {"available": True, "portal_url": "https://tspolice.gov.in", "requires_digital_signature": False},
                "meeseva_center": {"available": True, "requires_stamp": False, "stamp_value": 0}
            },
            "priority_rank": 21,
            "related_services": []
        },
        {
            "service_id": "POL-004",
            "name": {"en": "Vehicle NOC for Transfer", "te": "బదిలీ కోసం వాహన NOC"},
            "department": "Police",
            "category": "A",
            "keywords": ["vehicle NOC", "no objection certificate", "vehicle transfer", "వాహన NOC"],
            "fee": 62,
            "required_documents": [
                {"name": {"en": "Vehicle Registration Certificate", "te": "వాహన నమోదు ధృవీకరణ పత్రం"}, "type": "copy", "mandatory": True},
                {"name": {"en": "Insurance Certificate", "te": "బీమా ధృవీకరణ పత్రం"}, "type": "copy", "mandatory": True},
                {"name": {"en": "Owner ID Proof", "te": "యజమాని గుర్తింపు రుజువు"}, "type": "self_attested", "mandatory": True}
            ],
            "processing_time": "3-5 Days",
            "is_revenue": False,
            "description_simple": {
                "en": "No Objection Certificate from police for transferring vehicle ownership to another state.",
                "te": "వాహన యాజమాన్యాన్ని మరొక రాష్ట్రానికి బదిలీ చేయడానికి పోలీసుల నుండి అభ్యంతరం లేదు ధృవీకరణ పత్రం."
            },
            "submission_modes": {
                "online": {"available": True, "portal_url": "https://tspolice.gov.in", "requires_digital_signature": False},
                "meeseva_center": {"available": True, "requires_stamp": False, "stamp_value": 0}
            },
            "priority_rank": 22,
            "related_services": ["TRA-001"]
        }
    ]
    
    # Transport Services (5 services - Priority 23-27)
    transport_services = [
        {
            "service_id": "TRA-001",
            "name": {"en": "Driving License Renewal", "te": "డ్రైవింగ్ లైసెన్స్ పునరుద్ధరణ"},
            "department": "Transport",
            "category": "A",
            "keywords": ["driving license", "DL renewal", "license renewal", "డ్రైవింగ్ లైసెన్స్", "పునరుద్ధరణ"],
            "fee": 62,
            "required_documents": [
                {"name": {"en": "Existing Driving License", "te": "ఇప్పటికే ఉన్న డ్రైవింగ్ లైసెన్స్"}, "type": "original", "mandatory": True},
                {"name": {"en": "Medical Certificate", "te": "వైద్య ధృవీకరణ పత్రం"}, "type": "original", "mandatory": True},
                {"name": {"en": "Aadhar Card", "te": "ఆధార్ కార్డు"}, "type": "self_attested", "mandatory": True}
            ],
            "processing_time": "7-10 Days",
            "is_revenue": False,
            "description_simple": {
                "en": "Renewal of expired or expiring driving license for continued legal driving.",
                "te": "నిరంతర చట్టబద్ధ డ్రైవింగ్ కోసం గడువు ముగిసిన లేదా గడువు ముగియబోతున్న డ్రైవింగ్ లైసెన్స్ పునరుద్ధరణ."
            },
            "submission_modes": {
                "online": {"available": True, "portal_url": "https://parivahan.gov.in/parivahan", "requires_digital_signature": False},
                "meeseva_center": {"available": True, "requires_stamp": False, "stamp_value": 0}
            },
            "priority_rank": 23,
            "related_services": ["TRA-002"]
        },
        {
            "service_id": "TRA-002",
            "name": {"en": "Learner's License", "te": "లెర్నర్స్ లైసెన్స్"},
            "department": "Transport",
            "category": "A",
            "keywords": ["learner license", "LL", "learning license", "లెర్నర్స్ లైసెన్స్"],
            "fee": 62,
            "required_documents": [
                {"name": {"en": "Age Proof (Birth Certificate/School Certificate)", "te": "వయస్సు రుజువు (జనన ధృవీకరణ పత్రం/పాఠశాల ధృవీకరణ పత్రం)"}, "type": "copy", "mandatory": True},
                {"name": {"en": "Address Proof", "te": "చిరునామా రుజువు"}, "type": "copy", "mandatory": True},
                {"name": {"en": "Medical Certificate", "te": "వైద్య ధృవీకరణ పత్రం"}, "type": "original", "mandatory": True}
            ],
            "processing_time": "3-5 Days",
            "is_revenue": False,
            "description_simple": {
                "en": "Temporary license for learning to drive, valid for 6 months before permanent license test.",
                "te": "శాశ్వత లైసెన్స్ పరీక్షకు ముందు 6 నెలల వరకు చెల్లుబాటు అయ్యే డ్రైవింగ్ నేర్చుకోవడానికి తాత్కాలిక లైసెన్స్."
            },
            "submission_modes": {
                "online": {"available": True, "portal_url": "https://parivahan.gov.in/parivahan", "requires_digital_signature": False},
                "meeseva_center": {"available": True, "requires_stamp": False, "stamp_value": 0}
            },
            "priority_rank": 24,
            "related_services": ["TRA-001"]
        },
        {
            "service_id": "TRA-003",
            "name": {"en": "Vehicle Registration", "te": "వాహన నమోదు"},
            "department": "Transport",
            "category": "B",
            "keywords": ["vehicle registration", "RC", "registration certificate", "వాహన నమోదు"],
            "fee": 80,
            "required_documents": [
                {"name": {"en": "Invoice/Bill of Sale", "te": "ఇన్‌వాయిస్/అమ్మకపు బిల్లు"}, "type": "original", "mandatory": True},
                {"name": {"en": "Insurance Certificate", "te": "బీమా ధృవీకరణ పత్రం"}, "type": "original", "mandatory": True},
                {"name": {"en": "PUC Certificate", "te": "PUC ధృవీకరణ పత్రం"}, "type": "original", "mandatory": True},
                {"name": {"en": "Address Proof", "te": "చిరునామా రుజువు"}, "type": "copy", "mandatory": True}
            ],
            "processing_time": "7-15 Days",
            "is_revenue": False,
            "description_simple": {
                "en": "Registration of new vehicle with RTO for legal ownership and road use.",
                "te": "చట్టబద్ధ యాజమాన్యం మరియు రహదారి వినియోగం కోసం RTO తో కొత్త వాహన నమోదు."
            },
            "submission_modes": {
                "online": {"available": True, "portal_url": "https://parivahan.gov.in/parivahan", "requires_digital_signature": False},
                "meeseva_center": {"available": True, "requires_stamp": False, "stamp_value": 0}
            },
            "priority_rank": 25,
            "related_services": ["TRA-004"]
        },
        {
            "service_id": "TRA-004",
            "name": {"en": "Vehicle Transfer of Ownership", "te": "వాహన యాజమాన్య బదిలీ"},
            "department": "Transport",
            "category": "A",
            "keywords": ["vehicle transfer", "ownership transfer", "RC transfer", "వాహన బదిలీ"],
            "fee": 62,
            "required_documents": [
                {"name": {"en": "Original Registration Certificate", "te": "అసలు నమోదు ధృవీకరణ పత్రం"}, "type": "original", "mandatory": True},
                {"name": {"en": "Sale Agreement", "te": "అమ్మకపు ఒప్పందం"}, "type": "original", "mandatory": True},
                {"name": {"en": "Insurance Transfer", "te": "బీమా బదిలీ"}, "type": "copy", "mandatory": True},
                {"name": {"en": "NOC from Financier (if applicable)", "te": "ఫైనాన్సియర్ నుండి NOC (వర్తించినట్లయితే)"}, "type": "original", "mandatory": False}
            ],
            "processing_time": "7-10 Days",
            "is_revenue": False,
            "description_simple": {
                "en": "Transfer of vehicle ownership from seller to buyer with RTO records update.",
                "te": "RTO రికార్డుల నవీకరణతో విక్రేత నుండి కొనుగోలుదారుకు వాహన యాజమాన్య బదిలీ."
            },
            "submission_modes": {
                "online": {"available": True, "portal_url": "https://parivahan.gov.in/parivahan", "requires_digital_signature": False},
                "meeseva_center": {"available": True, "requires_stamp": False, "stamp_value": 0}
            },
            "priority_rank": 26,
            "related_services": ["TRA-003", "POL-004"]
        },
        {
            "service_id": "TRA-005",
            "name": {"en": "Duplicate Driving License", "te": "డూప్లికేట్ డ్రైవింగ్ లైసెన్స్"},
            "department": "Transport",
            "category": "A",
            "keywords": ["duplicate DL", "lost license", "damaged license", "డూప్లికేట్ లైసెన్స్"],
            "fee": 62,
            "required_documents": [
                {"name": {"en": "FIR Copy (for lost license)", "te": "FIR కాపీ (కోల్పోయిన లైసెన్స్ కోసం)"}, "type": "copy", "mandatory": False},
                {"name": {"en": "Damaged License (if applicable)", "te": "దెబ్బతిన్న లైసెన్స్ (వర్తించినట్లయితే)"}, "type": "original", "mandatory": False},
                {"name": {"en": "Aadhar Card", "te": "ఆధార్ కార్డు"}, "type": "self_attested", "mandatory": True}
            ],
            "processing_time": "5-7 Days",
            "is_revenue": False,
            "description_simple": {
                "en": "Issuance of duplicate driving license for lost, stolen, or damaged original license.",
                "te": "కోల్పోయిన, దొంగిలించబడిన లేదా దెబ్బతిన్న అసలు లైసెన్స్ కోసం డూప్లికేట్ డ్రైవింగ్ లైసెన్స్ జారీ."
            },
            "submission_modes": {
                "online": {"available": True, "portal_url": "https://parivahan.gov.in/parivahan", "requires_digital_signature": False},
                "meeseva_center": {"available": True, "requires_stamp": False, "stamp_value": 0}
            },
            "priority_rank": 27,
            "related_services": ["TRA-001"]
        }
    ]
    
    # Civil Supplies Services (3 services - Priority 28-30)
    civil_supplies_services = [
        {
            "service_id": "CIV-001",
            "name": {"en": "Ration Card - New Application", "te": "రేషన్ కార్డు - కొత్త దరఖాస్తు"},
            "department": "Civil Supplies",
            "category": "A",
            "keywords": ["ration card", "food security", "PDS", "రేషన్ కార్డు", "ఆహార భద్రత"],
            "fee": 62,
            "required_documents": [
                {"name": {"en": "Aadhar Card (all family members)", "te": "ఆధార్ కార్డు (కుటుంబ సభ్యులందరూ)"}, "type": "self_attested", "mandatory": True},
                {"name": {"en": "Address Proof", "te": "చిరునామా రుజువు"}, "type": "copy", "mandatory": True},
                {"name": {"en": "Income Certificate", "te": "ఆదాయ ధృవీకరణ పత్రం"}, "type": "copy", "mandatory": True},
                {"name": {"en": "Family Photo", "te": "కుటుంబ ఫోటో"}, "type": "digital", "mandatory": True}
            ],
            "processing_time": "15-30 Days",
            "is_revenue": False,
            "description_simple": {
                "en": "New ration card for accessing subsidized food grains through Public Distribution System.",
                "te": "పబ్లిక్ డిస్ట్రిబ్యూషన్ సిస్టమ్ ద్వారా రాయితీ ధాన్యాలను పొందడానికి కొత్త రేషన్ కార్డు."
            },
            "submission_modes": {
                "online": {"available": True, "portal_url": "https://epds.telangana.gov.in", "requires_digital_signature": False},
                "meeseva_center": {"available": True, "requires_stamp": False, "stamp_value": 0}
            },
            "priority_rank": 28,
            "related_services": ["CIV-002"]
        },
        {
            "service_id": "CIV-002",
            "name": {"en": "Ration Card - Add/Delete Member", "te": "రేషన్ కార్డు - సభ్యుడిని జోడించు/తొలగించు"},
            "department": "Civil Supplies",
            "category": "A",
            "keywords": ["ration card update", "add member", "delete member", "రేషన్ కార్డు నవీకరణ"],
            "fee": 62,
            "required_documents": [
                {"name": {"en": "Existing Ration Card", "te": "ఇప్పటికే ఉన్న రేషన్ కార్డు"}, "type": "copy", "mandatory": True},
                {"name": {"en": "Aadhar Card (of member to be added/deleted)", "te": "ఆధార్ కార్డు (జోడించాల్సిన/తొలగించాల్సిన సభ్యుడి)"}, "type": "self_attested", "mandatory": True},
                {"name": {"en": "Supporting Documents (Birth/Death/Marriage Certificate)", "te": "సహాయక పత్రాలు (జనన/మరణ/వివాహ ధృవీకరణ పత్రం)"}, "type": "copy", "mandatory": True}
            ],
            "processing_time": "10-15 Days",
            "is_revenue": False,
            "description_simple": {
                "en": "Update ration card by adding new family members or removing deceased/separated members.",
                "te": "కొత్త కుటుంబ సభ్యులను జోడించడం లేదా మరణించిన/విడిపోయిన సభ్యులను తొలగించడం ద్వారా రేషన్ కార్డును నవీకరించండి."
            },
            "submission_modes": {
                "online": {"available": True, "portal_url": "https://epds.telangana.gov.in", "requires_digital_signature": False},
                "meeseva_center": {"available": True, "requires_stamp": False, "stamp_value": 0}
            },
            "priority_rank": 29,
            "related_services": ["CIV-001"]
        },
        {
            "service_id": "CIV-003",
            "name": {"en": "LPG Gas Connection", "te": "LPG గ్యాస్ కనెక్షన్"},
            "department": "Civil Supplies",
            "category": "A",
            "keywords": ["LPG", "gas connection", "cooking gas", "Ujjwala", "గ్యాస్ కనెక్షన్"],
            "fee": 62,
            "required_documents": [
                {"name": {"en": "Aadhar Card", "te": "ఆధార్ కార్డు"}, "type": "self_attested", "mandatory": True},
                {"name": {"en": "Address Proof", "te": "చిరునామా రుజువు"}, "type": "copy", "mandatory": True},
                {"name": {"en": "Ration Card", "te": "రేషన్ కార్డు"}, "type": "copy", "mandatory": True},
                {"name": {"en": "Bank Account Details", "te": "బ్యాంక్ ఖాతా వివరాలు"}, "type": "copy", "mandatory": True}
            ],
            "processing_time": "7-15 Days",
            "is_revenue": False,
            "description_simple": {
                "en": "New LPG gas connection for domestic cooking purposes with subsidy benefits.",
                "te": "రాయితీ ప్రయోజనాలతో గృహ వంట ప్రయోజనాల కోసం కొత్త LPG గ్యాస్ కనెక్షన్."
            },
            "submission_modes": {
                "online": {"available": True, "portal_url": "https://www.bharatgas.gov.in", "requires_digital_signature": False},
                "meeseva_center": {"available": True, "requires_stamp": False, "stamp_value": 0}
            },
            "priority_rank": 30,
            "related_services": ["CIV-001"]
        }
    ]
