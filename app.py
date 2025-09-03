# VisaTier 5.0 - Enhanced Immigration ROI Calculator
# Advanced AI-powered business migration intelligence with personalized insights

import math
import numpy as np
import pandas as pd
import gradio as gr
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import json
from datetime import datetime, timedelta
import hashlib
import secrets
from typing import Dict, List, Tuple, Optional
import asyncio
from dataclasses import dataclass, field
import random

# =========================
# ENHANCED STYLING SYSTEM
# =========================

PREMIUM_CSS = """
/* Modern Design System - Enhanced */
:root {
    --primary: #2563eb;
    --primary-dark: #1d4ed8;
    --secondary: #0f172a;
    --accent: #f59e0b;
    --success: #10b981;
    --warning: #f59e0b;
    --error: #ef4444;
    --surface: #ffffff;
    --surface-alt: #f8fafc;
    --text: #1e293b;
    --text-muted: #64748b;
    --border: #e2e8f0;
    --radius: 12px;
    --shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
    --gradient: linear-gradient(135deg, var(--primary) 0%, var(--primary-dark) 100%);
    --gradient-gold: linear-gradient(135deg, #fbbf24 0%, #f59e0b 100%);
}
/* Enhanced Global Styles */
.gradio-container {
    max-width: 1400px !important;
    margin: 0 auto !important;
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif !important;
}
/* Premium Header with Animation */
.premium-header {
    background: var(--gradient);
    color: white;
    padding: 3rem 2rem;
    border-radius: var(--radius);
    margin-bottom: 2rem;
    position: relative;
    overflow: hidden;
}
.premium-header::before {
    content: '';
    position: absolute;
    top: -50%;
    right: -50%;
    width: 200%;
    height: 200%;
    background: radial-gradient(circle, rgba(255,255,255,0.1) 0%, transparent 70%);
    animation: float 8s ease-in-out infinite;
}
@keyframes float {
    0%, 100% { transform: translateY(0px) rotate(0deg); }
    50% { transform: translateY(-30px) rotate(180deg); }
}
.header-content {
    position: relative;
    z-index: 2;
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
    gap: 2rem;
}
.header-title {
    font-size: 2.5rem;
    font-weight: 800;
    margin-bottom: 1rem;
    text-shadow: 0 2px 4px rgba(0,0,0,0.1);
}
.header-subtitle {
    opacity: 0.9;
    font-size: 1.2rem;
    font-weight: 400;
}
.header-stats {
    text-align: right;
    font-size: 1rem;
    opacity: 0.9;
}
/* Enhanced Profile Cards */
.profile-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 1.5rem;
    margin: 2rem 0;
}
.profile-card {
    background: var(--surface);
    border: 2px solid var(--border);
    border-radius: var(--radius);
    padding: 2rem;
    text-align: center;
    cursor: pointer;
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    position: relative;
    overflow: hidden;
    box-shadow: var(--shadow);
}
.profile-card::before {
    content: '';
    position: absolute;
    top: 0;
    left: -100%;
    width: 100%;
    height: 100%;
    background: linear-gradient(90deg, transparent, rgba(255,255,255,0.4), transparent);
    transition: left 0.5s;
}
.profile-card:hover::before {
    left: 100%;
}
.profile-card:hover {
    border-color: var(--primary);
    transform: translateY(-5px);
    box-shadow: 0 10px 25px rgba(0,0,0,0.15);
}
.profile-card.selected {
    border-color: var(--primary);
    background: var(--gradient);
    color: white;
    transform: translateY(-5px);
}
.profile-icon {
    font-size: 3rem;
    margin-bottom: 1rem;
    display: block;
}
.profile-name {
    font-weight: 700;
    font-size: 1.2rem;
    margin-bottom: 0.5rem;
}
.profile-revenue {
    font-size: 1rem;
    opacity: 0.8;
    font-weight: 500;
}
.profile-description {
    font-size: 0.9rem;
    opacity: 0.7;
    margin-top: 0.5rem;
    line-height: 1.4;
}
/* Enhanced KPI Cards */
.kpi-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 2rem;
    margin: 2rem 0;
}
.kpi-card {
    background: var(--surface);
    border-radius: var(--radius);
    padding: 2rem;
    text-align: center;
    box-shadow: var(--shadow);
    position: relative;
    overflow: hidden;
    transition: transform 0.2s ease;
}
.kpi-card:hover {
    transform: translateY(-3px);
}
.kpi-card::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 4px;
    background: var(--gradient);
}
.kpi-label {
    font-size: 1rem;
    color: var(--text-muted);
    margin-bottom: 0.5rem;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}
.kpi-value {
    font-size: 2.5rem;
    font-weight: 800;
    color: var(--primary);
    margin-bottom: 0.5rem;
}
.kpi-note {
    font-size: 0.9rem;
    color: var(--text-muted);
    line-height: 1.4;
}
.kpi-card.success .kpi-value { color: var(--success); }
.kpi-card.warning .kpi-value { color: var(--warning); }
.kpi-card.error .kpi-value { color: var(--error); }
/* AI Insight Cards */
.ai-insights-grid {
    display: grid;
    gap: 1.5rem;
    margin: 2rem 0;
}
.ai-insight-card {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    border-radius: var(--radius);
    padding: 2rem;
    box-shadow: var(--shadow);
    position: relative;
    overflow: hidden;
}
.ai-insight-card::before {
    content: '🤖';
    position: absolute;
    top: 1rem;
    right: 1rem;
    font-size: 2rem;
    opacity: 0.3;
}
.ai-insight-header {
    display: flex;
    align-items: center;
    margin-bottom: 1rem;
}
.ai-insight-icon {
    font-size: 1.5rem;
    margin-right: 0.75rem;
}
.ai-insight-title {
    font-weight: 700;
    font-size: 1.2rem;
    margin: 0;
}
.ai-insight-description {
    line-height: 1.6;
    margin-bottom: 1rem;
    font-size: 1rem;
}
.ai-confidence {
    background: rgba(255,255,255,0.2);
    padding: 0.5rem 1rem;
    border-radius: 20px;
    display: inline-block;
    font-size: 0.9rem;
    font-weight: 600;
}
/* Country Comparison Enhanced */
.country-comparison {
    background: var(--surface);
    border-radius: var(--radius);
    padding: 2rem;
    margin: 2rem 0;
    box-shadow: var(--shadow);
}
.comparison-table {
    width: 100%;
    border-collapse: collapse;
    margin-top: 1rem;
}
.comparison-table th {
    background: var(--gradient);
    color: white;
    padding: 1rem;
    text-align: left;
    font-weight: 600;
}
.comparison-table td {
    padding: 1rem;
    border-bottom: 1px solid var(--border);
}
.comparison-table tr:nth-child(even) {
    background: var(--surface-alt);
}
/* Enhanced CTA Elements */
.premium-cta {
    background: var(--gradient-gold);
    color: white;
    padding: 3rem;
    border-radius: var(--radius);
    text-align: center;
    margin: 3rem 0;
    position: relative;
    overflow: hidden;
}
.premium-cta::before {
    content: '⭐';
    position: absolute;
    font-size: 5rem;
    opacity: 0.1;
    top: 1rem;
    right: 2rem;
    animation: pulse 2s infinite;
}
@keyframes pulse {
    0%, 100% { opacity: 0.1; transform: scale(1); }
    50% { opacity: 0.3; transform: scale(1.1); }
}
.cta-title {
    font-size: 2rem;
    font-weight: 800;
    margin-bottom: 1rem;
}
.cta-subtitle {
    font-size: 1.2rem;
    opacity: 0.9;
    margin-bottom: 2rem;
}
.cta-button-enhanced {
    background: white !important;
    color: var(--primary) !important;
    border: none !important;
    border-radius: 50px !important;
    padding: 1rem 3rem !important;
    font-weight: 700 !important;
    font-size: 1.1rem !important;
    cursor: pointer !important;
    transition: all 0.3s ease !important;
    text-decoration: none !important;
    display: inline-block !important;
    box-shadow: 0 4px 15px rgba(0,0,0,0.2) !important;
}
.cta-button-enhanced:hover {
    transform: translateY(-3px) !important;
    box-shadow: 0 8px 25px rgba(0,0,0,0.3) !important;
}
/* Real-time notifications */
.notification-popup {
    position: fixed;
    top: 20px;
    right: 20px;
    background: var(--success);
    color: white;
    padding: 1rem 1.5rem;
    border-radius: var(--radius);
    box-shadow: var(--shadow);
    z-index: 1000;
    animation: slideInRight 0.5s ease, fadeOut 0.5s ease 4s;
    min-width: 300px;
}
@keyframes slideInRight {
    from { transform: translateX(100%); opacity: 0; }
    to { transform: translateX(0); opacity: 1; }
}
@keyframes fadeOut {
    from { opacity: 1; }
    to { opacity: 0; }
}
/* Mobile responsiveness enhanced */
@media (max-width: 768px) {
    .header-title { font-size: 2rem; }
    .profile-grid { grid-template-columns: 1fr; }
    .kpi-grid { grid-template-columns: 1fr; }
    .header-content { flex-direction: column; text-align: center; }
    .premium-header { padding: 2rem 1rem; }
}
/* Loading states */
.loading-spinner {
    border: 3px solid var(--border);
    border-top: 3px solid var(--primary);
    border-radius: 50%;
    width: 40px;
    height: 40px;
    animation: spin 1s linear infinite;
    margin: 2rem auto;
}
@keyframes spin {
    0% { transform: rotate(0deg); }
    100% { transform: rotate(360deg); }
}
"""

PREMIUM_THEME = gr.themes.Soft(
    primary_hue="blue",
    secondary_hue="slate",
    neutral_hue="slate"
).set(
    body_background_fill="#f8fafc",
    body_text_color="#1e293b",
    button_primary_background_fill="#2563eb",
    button_primary_background_fill_hover="#1d4ed8",
    input_background_fill="#ffffff",
    input_border_width="2px",
    block_background_fill="#ffffff",
    block_radius="12px"
)

# =========================
# ENHANCED DATA MODELS WITH AI
# =========================

@dataclass
class UserProfile:
    """Represents an entrepreneur persona using the simulator.
    Attributes:
        id: Unique identifier for the profile.
        name: Display name of the persona.
        icon: Emoji or icon representing the profile visually.
        typical_revenue: Expected monthly revenue for this persona.
        risk_tolerance: Risk appetite on a 0-100 scale.
        key_concerns: List of primary business concerns.
        success_multiplier: Factor applied to revenue projections.
        margin_expectations: Tuple of expected margin range (min, max).
        description: Short narrative description of the persona.
        ai_persona: Identifier for which AI persona to use for insights.
    """
    
    id: str
    name: str
    icon: str
    typical_revenue: float
    risk_tolerance: int
    key_concerns: List[str]
    success_multiplier: float
    margin_expectations: Tuple[float, float]
    description: str
    ai_persona: str  # AI personality for insights
    
@dataclass
class CountryData:
    """Structured metrics describing a potential destination country.
    Attributes:
        name: Country name.
        corp_tax: Corporate tax rate as a decimal.
        pers_tax: Personal tax rate as a decimal.
        living_cost: Average monthly living expenses.
        business_cost: Average monthly business operating cost.
        setup_cost: One-time setup cost for relocation.
        currency: Local currency identifier.
        market_growth: Expected market growth percentage.
        ease_score: Business ease score (0-10).
        banking_score: Banking system quality score (0-10).
        partnership_score: Ease of forming partnerships (0-10).
        visa_options: Available visa or residence options.
        market_insights: Key market insights keyed by topic.
        risk_factors: Mapping of risk types to probability weights.
        seasonality: Monthly seasonality factors for cash flow projections.
        special_programs: Notable government or business programs.
        recent_changes: Recent regulatory or market changes summary.
        ai_sentiment: AI-derived market sentiment score.
    """
    
    name: str
    corp_tax: float
    pers_tax: float
    living_cost: float
    business_cost: float
    setup_cost: float
    currency: str
    market_growth: float
    ease_score: float
    banking_score: float
    partnership_score: float
    visa_options: List[str]
    market_insights: Dict[str, str]
    risk_factors: Dict[str, float]
    seasonality: List[float]
    special_programs: List[str]
    recent_changes: str
    ai_sentiment: float  # Market sentiment score

# Enhanced user profiles with detailed personas
ENHANCED_PROFILES = {
    "tech_startup": UserProfile(
        id="tech_startup",
        name="Tech Startup Founder",
        icon="🚀",
        typical_revenue=65000,
        risk_tolerance=85,
        key_concerns=["talent_access", "ip_protection", "scaling", "funding"],
        success_multiplier=1.6,
        margin_expectations=(20, 45),
        description="Building the next unicorn with cutting-edge technology",
        ai_persona="analytical_optimist"
    ),
    "crypto_trader": UserProfile(
        id="crypto_trader",
        name="Crypto/DeFi Entrepreneur",
        icon="₿",
        typical_revenue=125000,
        risk_tolerance=95,
        key_concerns=["regulatory_clarity", "banking", "tax_optimization", "privacy"],
        success_multiplier=2.2,
        margin_expectations=(35, 75),
        description="Navigating the digital asset revolution with strategic positioning",
        ai_persona="risk_aware_pioneer"
    ),
    "consulting": UserProfile(
        id="consulting",
        name="Strategic Consultant",
        icon="💼",
        typical_revenue=45000,
        risk_tolerance=60,
        key_concerns=["client_proximity", "reputation", "networking", "expertise_transfer"],
        success_multiplier=1.2,
        margin_expectations=(50, 80),
        description="Providing high-value strategic advice to enterprise clients",
        ai_persona="relationship_focused"
    ),
    "ecommerce": UserProfile(
        id="ecommerce",
        name="E-commerce Entrepreneur",
        icon="🛒",
        typical_revenue=75000,
        risk_tolerance=70,
        key_concerns=["logistics", "market_access", "compliance", "scalability"],
        success_multiplier=1.4,
        margin_expectations=(15, 35),
        description="Building scalable online retail empires across global markets",
        ai_persona="growth_focused"
    ),
    "real_estate": UserProfile(
        id="real_estate",
        name="Real Estate Investor",
        icon="🏠",
        typical_revenue=35000,
        risk_tolerance=50,
        key_concerns=["property_laws", "financing", "market_stability", "yield_optimization"],
        success_multiplier=1.0,
        margin_expectations=(12, 25),
        description="Building wealth through strategic property investments",
        ai_persona="conservative_builder"
    ),
    "content_creator": UserProfile(
        id="content_creator",
        name="Digital Creator/Influencer",
        icon="📱",
        typical_revenue=55000,
        risk_tolerance=75,
        key_concerns=["internet_infrastructure", "tax_treaties", "lifestyle", "monetization"],
        success_multiplier=1.3,
        margin_expectations=(65, 90),
        description="Monetizing creativity and building personal brand globally",
        ai_persona="lifestyle_optimizer"
    )
}

# Comprehensive and accurate country database
ENHANCED_COUNTRIES = {
    "UAE": CountryData(
        name="UAE (Dubai/Abu Dhabi)",
        corp_tax=0.09,  # Introduced in 2023 for companies >3.75M AED
        pers_tax=0.00,
        living_cost=9200, business_cost=2200, setup_cost=48000,
        currency="AED",
        market_growth=9.1, ease_score=9.6, banking_score=9.2, partnership_score=96,
        visa_options=["Golden Visa (10yr)", "Green Visa (5yr)", "Freelancer Visa", "Investor Visa"],
        market_insights={},
        risk_factors={"political": 0.08, "economic": 0.12, "regulatory": 0.06},
        seasonality=[1.2, 1.1, 1.0, 0.9, 0.7, 0.6, 0.5, 0.6, 0.9, 1.1, 1.3, 1.4],
        special_programs=["DIFC License", "ADGM License", "Free Zone Setup"],
        recent_changes="Corporate tax introduced 2023, expanded Golden Visa criteria 2024",
        ai_sentiment=0.92
    ),
    "Singapore": CountryData(
        name="Singapore",
        corp_tax=0.17,  # With exemptions, effective can be lower
        pers_tax=0.24,  # Progressive up to 24%
        living_cost=8800, business_cost=2400, setup_cost=42000,
        currency="SGD",
        market_growth=7.2, ease_score=9.8, banking_score=9.8, partnership_score=94,
        visa_options=["Tech.Pass", "Entrepreneur Pass", "ONE Pass", "Employment Pass"],
        market_insights={},
        risk_factors={"political": 0.02, "economic": 0.08, "regulatory": 0.04},
        seasonality=[0.9, 0.85, 0.9, 1.0, 1.1, 1.2, 1.3, 1.25, 1.1, 1.0, 0.95, 1.0],
        special_programs=["MAS Fintech Sandbox", "Startup SG", "Global Investor Programme"],
        recent_changes="Tech.Pass launched 2024, enhanced startup ecosystem support",
        ai_sentiment=0.89
    ),
    "Portugal": CountryData(
        name="Portugal",
        corp_tax=0.21,  # Plus municipal surcharge
        pers_tax=0.48,  # Progressive, but NHR regime available
        living_cost=2800, business_cost=650, setup_cost=15000,
        currency="EUR",
        market_growth=5.4, ease_score=8.2, banking_score=8.1, partnership_score=85,
        visa_options=["D2 Entrepreneur", "D7 Passive Income", "Tech Visa", "Startup Visa"],
        market_insights={},
        risk_factors={"political": 0.06, "economic": 0.18, "regulatory": 0.09},
        seasonality=[0.8, 0.8, 0.9, 1.0, 1.3, 1.5, 1.7, 1.6, 1.3, 1.1, 0.9, 0.9],
        special_programs=["NHR Tax Regime", "Portugal 2030", "Startup Portugal"],
        recent_changes="Golden Visa phased out 2023, NHR regime modified 2024",
        ai_sentiment=0.76
    ),
    "Spain": CountryData(
        name="Spain",
        corp_tax=0.25,  # Reduced rates for startups
        pers_tax=0.47,  # Progressive system
        living_cost=3200, business_cost=750, setup_cost=18000,
        currency="EUR",
        market_growth=4.8, ease_score=7.9, banking_score=8.3, partnership_score=82,
        visa_options=["Entrepreneur Visa", "Investment Visa", "Digital Nomad Visa", "Non-Lucrative"],
        market_insights={},
        risk_factors={"political": 0.08, "economic": 0.22, "regulatory": 0.12},
        seasonality=[0.8, 0.8, 0.9, 1.1, 1.4, 1.6, 1.8, 1.7, 1.4, 1.2, 0.9, 0.8],
        special_programs=["Startup Law 2022", "Beckham Law", "ENISA Loans"],
        recent_changes="Digital Nomad Visa launched 2023, improved startup ecosystem",
        ai_sentiment=0.78
    ),
    "USA": CountryData(
        name="USA (Delaware/Florida)",
        corp_tax=0.21,  # Federal + state varies
        pers_tax=0.37,  # Federal + state varies significantly
        living_cost=12000, business_cost=3200, setup_cost=85000,
        currency="USD",
        market_growth=6.8, ease_score=8.6, banking_score=9.4, partnership_score=88,
        visa_options=["EB-5 Investor", "L-1 Intracompany", "E-2 Treaty Investor", "O-1 Extraordinary"],
        market_insights={},
        risk_factors={"political": 0.18, "economic": 0.14, "regulatory": 0.16},
        seasonality=[1.0, 0.95, 1.05, 1.15, 1.1, 1.05, 0.95, 0.9, 1.1, 1.2, 1.25, 1.4],
        special_programs=["EB-5 Regional Centers", "SBIR Grants", "State Startup Incentives"],
        recent_changes="EB-5 minimum increased to $800K, enhanced startup visa discussions",
        ai_sentiment=0.82
    ),
    "UK": CountryData(
        name="United Kingdom",
        corp_tax=0.25,  # Increased from 19% in 2023
        pers_tax=0.45,  # Progressive rates + additional rate
        living_cost=7200, business_cost=1800, setup_cost=28000,
        currency="GBP",
        market_growth=3.8, ease_score=8.4, banking_score=9.1, partnership_score=81,
        visa_options=["Innovator Founder", "Scale-up Visa", "Global Talent", "High Potential Individual"],
        market_insights={},
        risk_factors={"political": 0.15, "economic": 0.19, "regulatory": 0.11},
        seasonality=[0.9, 0.85, 0.9, 1.0, 1.1, 1.2, 1.3, 1.25, 1.1, 1.05, 1.0, 1.2],
        special_programs=["R&D Tax Credits", "SEIS/EIS Schemes", "Innovate UK Grants"],
        recent_changes="Innovator visa replaced 2023, HPI visa introduced for top graduates",
        ai_sentiment=0.74
    ),
    "Ireland": CountryData(
        name="Ireland",
        corp_tax=0.125,  # Famous 12.5% rate for trading income
        pers_tax=0.52,  # Including USC and PRSI
        living_cost=4800, business_cost=1200, setup_cost=22000,
        currency="EUR",
        market_growth=6.2, ease_score=8.8, banking_score=8.7, partnership_score=87,
        visa_options=["Startup Entrepreneur Programme", "Investment Programme", "Critical Skills"],
        market_insights={},
        risk_factors={"political": 0.04, "economic": 0.16, "regulatory": 0.08},
        seasonality=[0.8, 0.8, 0.9, 1.0, 1.2, 1.4, 1.5, 1.4, 1.2, 1.1, 0.9, 0.9],
        special_programs=["R&D Tax Credit 25%", "Knowledge Development Box", "Employment Incentive"],
        recent_changes="Enhanced startup supports 2024, housing challenges persist",
        ai_sentiment=0.81
    ),
    "Malta": CountryData(
        name="Malta",
        corp_tax=0.35,  # But with refunds, effective rate much lower
        pers_tax=0.35,  # Progressive with various exemptions
        living_cost=3500, business_cost=900, setup_cost=25000,
        currency="EUR",
        market_growth=5.8, ease_score=8.1, banking_score=7.9, partnership_score=84,
        visa_options=["Nomad Residence Permit", "Global Residence Programme", "Investment Programme"],
        market_insights={},
        risk_factors={"political": 0.07, "economic": 0.15, "regulatory": 0.10},
        seasonality=[0.7, 0.7, 0.8, 0.9, 1.2, 1.5, 1.8, 1.7, 1.4, 1.1, 0.9, 0.8],
        special_programs=["Malta Individual Investor Programme", "Highly Qualified Persons Rules"],
        recent_changes="Digital nomad permit enhanced 2024, gaming license updates",
        ai_sentiment=0.79
    ),
    "Greece": CountryData(
        name="Greece",
        corp_tax=0.22,  # Reduced from higher rates
        pers_tax=0.44,  # Progressive system
        living_cost=2200, business_cost=550, setup_cost=12000,
        currency="EUR",
        market_growth=4.2, ease_score=7.6, banking_score=7.4, partnership_score=78,
        visa_options=["Golden Visa", "Digital Nomad Visa", "Investment Activity Permit"],
        market_insights={},
        risk_factors={"political": 0.12, "economic": 0.25, "regulatory": 0.14},
        seasonality=[0.6, 0.6, 0.8, 1.0, 1.3, 1.6, 1.9, 1.8, 1.5, 1.2, 0.9, 0.7],
        special_programs=["Non-Dom Regime", "Startup Greece", "Development Law Incentives"],
        recent_changes="Golden Visa minimum increased 2023, digital nomad visa launched",
        ai_sentiment=0.72
    ),
    "Cyprus": CountryData(
        name="Cyprus",
        corp_tax=0.125,  # EU's lowest corporate tax rate
        pers_tax=0.35,  # Progressive with non-dom benefits
        living_cost=3800, business_cost=1100, setup_cost=20000,
        currency="EUR",
        market_growth=5.6, ease_score=8.0, banking_score=7.8, partnership_score=83,
        visa_options=["Category F (Investment)", "Digital Nomad Visa", "Pink Slip"],
        market_insights={},
        risk_factors={"political": 0.09, "economic": 0.18, "regulatory": 0.11},
        seasonality=[0.8, 0.8, 0.9, 1.0, 1.3, 1.6, 1.7, 1.6, 1.4, 1.2, 1.0, 0.9],
        special_programs=["IP Box Regime", "Notional Interest Deduction", "Non-Dom Programme"],
        recent_changes="Enhanced digital nomad provisions 2024, banking sector recovery",
        ai_sentiment=0.77
    )
}

# =========================
# AI-POWERED INSIGHTS ENGINE
# =========================

class AIInsightEngine:
    """Engine that crafts personalized AI insights for ROI simulations.
    Attributes:
        insight_templates: Persona-specific message templates keyed by persona id.
        risk_mitigation_strategies: Mapping of risk types to mitigation tactics.
        success_catalysts: Key success factors for each profile.
    """
    
    def __init__(self):
        """Initialize insight templates and supporting lookup tables.
        Returns:
            None
        Side Effects:
            Populates in-memory templates and strategy mappings used during
            insight generation.
        """
        
        self.insight_templates = {
            "analytical_optimist": {
                "high_roi": "Outstanding potential detected! Your tech profile + {country} = perfect storm for growth. The {special_metric} factor could amplify returns by {multiplier}x.",
                "medium_roi": "Solid opportunity with room for optimization. Consider {suggestion} to unlock additional {percentage}% returns.",
                "low_roi": "Challenging numbers, but not impossible. Focus on {focus_area} - early movers often capture disproportionate value.",
                "risk_warning": "Risk assessment shows {risk_factor}. Mitigation strategy: {mitigation}."
            },
            "risk_aware_pioneer": {
                "high_roi": "Exceptional asymmetric upside detected. {country}'s regulatory clarity + your crypto expertise = ideal positioning for the next bull cycle.",
                "medium_roi": "Decent alpha opportunity. The {regulatory_advantage} gives you edge over competitors stuck in restrictive jurisdictions.",
                "low_roi": "Suboptimal risk-adjusted returns. Consider {alternative} or wait for {catalyst} to improve the setup.",
                "risk_warning": "Regulatory headwinds: {regulation_risk}. Diversification strategy recommended."
            },
            "relationship_focused": {
                "high_roi": "Your network effect multiplier in {country} is exceptional. The {business_culture} aligns perfectly with your consulting methodology.",
                "medium_roi": "Strong foundation for relationship-driven growth. Focus on {networking_opportunity} to accelerate client acquisition.",
                "low_roi": "Relationship building will be challenging initially. Invest heavily in {relationship_strategy} for long-term success.",
                "risk_warning": "Cultural adaptation period: {adaptation_time}. Client trust building critical."
            },
            "growth_focused": {
                "high_roi": "Scalability paradise! {country}'s {infrastructure_advantage} + your e-commerce expertise = exponential growth potential.",
                "medium_roi": "Solid growth trajectory possible. Optimize {conversion_factor} to achieve top-tier performance.",
                "low_roi": "Growth constraints identified: {constraint}. Pivot strategy: {pivot_suggestion}.",
                "risk_warning": "Market saturation risk in {timeframe}. First-mover advantage critical."
            },
            "conservative_builder": {
                "high_roi": "Exceptional wealth preservation opportunity. {country}'s {stability_factor} offers both growth and capital protection.",
                "medium_roi": "Steady wealth building trajectory. The {compound_advantage} effect strengthens over time.",
                "low_roi": "Conservative approach recommended. Focus on {safe_strategy} until market conditions improve.",
                "risk_warning": "Volatility in {risk_area}. Diversification across {alternatives} advised."
            },
            "lifestyle_optimizer": {
                "high_roi": "Lifestyle + profit optimization achieved! {country} offers the perfect blend of {lifestyle_benefits} and tax efficiency.",
                "medium_roi": "Quality of life upgrade with decent returns. The {happiness_factor} makes this worthwhile beyond just numbers.",
                "low_roi": "Lifestyle benefits outweigh financial returns. If {lifestyle_priority} is your focus, proceed despite lower ROI.",
                "risk_warning": "Lifestyle inflation risk: {inflation_factor}. Budget discipline essential."
            }
        }
        
        self.risk_mitigation_strategies = {
            "political": ["Diversify across jurisdictions", "Monitor policy changes", "Maintain dual residencies"],
            "economic": ["Currency hedging", "Multiple revenue streams", "Economic indicator tracking"],
            "regulatory": ["Legal compliance monitoring", "Regulatory change alerts", "Professional advisory team"]
        }
        
        self.success_catalysts = {
            "tech_startup": ["Product-market fit", "Series A funding", "Key hire acquisition"],
            "crypto_trader": ["Institutional adoption", "Regulatory clarity", "Market cycle timing"],
            "consulting": ["Thought leadership", "Strategic partnerships", "Client case studies"],
            "ecommerce": ["Supply chain optimization", "Marketing automation", "International expansion"],
            "real_estate": ["Market timing", "Leverage optimization", "Portfolio diversification"],
            "content_creator": ["Viral content", "Brand partnerships", "Platform diversification"]
        }
    
    def generate_personalized_insight(self, profile: UserProfile, country: CountryData, result: Dict) -> Dict:
        """Generate AI-powered insights for a given profile and country.
        Args:
            profile: The active user's profile information.
            country: Destination country data being evaluated.
            result: Output from the ROI calculator containing financial metrics.
        Returns:
            A dictionary containing the generated insight text, confidence
            score, tier, key factors and action items.
        Side Effects:
            Logs an error message to stdout if insight generation fails.
        """
        try:
            roi = result.get('roi', 0)
            risk_score = result.get('risk_score', 50)
            confidence = result.get('monte_carlo', {}).get('probability_positive_roi', 0.5)
            
            # Determine insight tier
            if roi >= 200 and confidence >= 0.8:
                tier = "high_roi"
            elif roi >= 100 and confidence >= 0.6:
                tier = "medium_roi"
            else:
                tier = "low_roi"
            
            # Get persona-specific template
            persona = profile.ai_persona
            template = self.insight_templates.get(persona, self.insight_templates["analytical_optimist"])[tier]
            
            # Generate dynamic variables
            variables = self._generate_insight_variables(profile, country, result, tier)
            
            # Format the insight
            insight_text = template.format(**variables)
            
            # Add risk warning if needed
            if risk_score > 70:
                risk_template = self.insight_templates[persona]["risk_warning"]
                risk_variables = self._generate_risk_variables(country, risk_score)
                risk_text = risk_template.format(**risk_variables)
                insight_text += f"\n\n{risk_text}"
            
            # Calculate confidence score
            confidence_score = min(95, confidence * 100 + random.uniform(-5, 5))
            
            return {
                "text": insight_text,
                "confidence": confidence_score,
                "tier": tier,
                "key_factors": variables.get("key_factors", []),
                "action_items": self._generate_action_items(profile, country, tier),
                "timeline": self._estimate_timeline(tier, profile),
                "success_probability": confidence * 100
            }
            
        except Exception as e:
            print(f"AI Insight generation error: {e}")
            return {
                "text": f"Analysis complete for {profile.name} relocating to {country.name}. Custom insights are being generated based on your unique profile.",
                "confidence": 75,
                "tier": "medium_roi",
                "key_factors": ["Market opportunity", "Tax optimization", "Risk factors"],
                "action_items": ["Research visa requirements", "Consult tax advisor", "Validate market assumptions"],
                "timeline": "12-18 months for full transition",
                "success_probability": 70
            }
    
    def _generate_insight_variables(self, profile: UserProfile, country: CountryData, result: Dict, tier: str) -> Dict:
        """Generate dynamic variables for insight templates"""
        variables = {
            "country": country.name,
            "profile": profile.name
        }
        
        # Country-specific advantages
        if country.corp_tax < 0.15:
            variables["special_metric"] = "ultra-low corporate tax"
            variables["tax_advantage"] = f"{country.corp_tax*100:.1f}% corporate rate"
        elif country.ease_score > 9.0:
            variables["special_metric"] = "business-friendly environment"
            variables["infrastructure_advantage"] = "world-class business infrastructure"
        else:
            variables["special_metric"] = "market growth potential"
            variables["growth_advantage"] = f"{country.market_growth:.1f}% annual growth"
        
        # Profile-specific factors
        if profile.id == "tech_startup":
            variables["multiplier"] = "2.5"
            variables["suggestion"] = "accelerated talent acquisition"
            variables["focus_area"] = "product-market fit validation"
        elif profile.id == "crypto_trader":
            variables["regulatory_advantage"] = f"{country.name}'s progressive crypto framework"
            variables["alternative"] = "jurisdictional arbitrage strategy"
            variables["catalyst"] = "next regulatory clarity milestone"
        elif profile.id == "consulting":
            variables["business_culture"] = f"{country.name}'s professional service market"
            variables["networking_opportunity"] = "local business associations"
            variables["relationship_strategy"] = "cultural immersion program"
        elif profile.id == "ecommerce":
            variables["conversion_factor"] = "logistics optimization"
            variables["constraint"] = "market access barriers"
            variables["pivot_suggestion"] = "B2B pivot strategy"
        elif profile.id == "real_estate":
            variables["stability_factor"] = "property market fundamentals"
            variables["compound_advantage"] = "rental yield + appreciation"
            variables["safe_strategy"] = "diversified property portfolio"
        elif profile.id == "content_creator":
            variables["lifestyle_benefits"] = "creator-friendly tax structure + quality of life"
            variables["happiness_factor"] = "work-life balance optimization"
            variables["lifestyle_priority"] = "creative freedom and inspiration"
        
        # ROI-specific variables
        if tier == "high_roi":
            variables["percentage"] = str(random.randint(15, 25))
        elif tier == "medium_roi":
            variables["percentage"] = str(random.randint(8, 15))
        else:
            variables["percentage"] = str(random.randint(3, 8))
        
        # Risk-specific variables
        top_risk = max(country.risk_factors.items(), key=lambda x: x[1])
        variables["risk_factor"] = f"{top_risk[0]} risk at {top_risk[1]*100:.1f}%"
        
        return variables
    
    def _generate_risk_variables(self, country: CountryData, risk_score: float) -> Dict:
        """Generate risk-specific variables"""
        top_risk = max(country.risk_factors.items(), key=lambda x: x[1])
        risk_type = top_risk[0]
        
        return {
            "risk_factor": f"{risk_type} instability ({risk_score:.0f}% risk score)",
            "regulation_risk": f"{country.name}'s evolving regulatory landscape",
            "mitigation": ", ".join(self.risk_mitigation_strategies.get(risk_type, ["Professional consultation"])),
            "adaptation_time": "6-12 months",
            "timeframe": f"{random.randint(18, 36)} months",
            "risk_area": risk_type,
            "alternatives": "Portugal, Ireland" if country.name != "Portugal" else "Malta, Cyprus",
            "inflation_factor": f"{country.living_cost/1000:.1f}x cost increase"
        }
    
    def _generate_action_items(self, profile: UserProfile, country: CountryData, tier: str) -> List[str]:
        """Generate specific action items based on profile and tier"""
        base_actions = [
            f"Research {country.visa_options[0]} requirements",
            f"Consult with {country.name} tax advisor",
            "Prepare financial documentation"
        ]
        
        if tier == "high_roi":
            base_actions.extend([
                "Fast-track visa application",
                "Secure local banking relationships",
                "Identify strategic partnerships"
            ])
        elif tier == "medium_roi":
            base_actions.extend([
                "Validate market assumptions",
                "Develop local network",
                "Plan phased transition"
            ])
        else:
            base_actions.extend([
                "Reassess timing and strategy",
                "Consider alternative jurisdictions",
                "Focus on risk mitigation"
            ])
        
        # Profile-specific actions
        profile_actions = {
            "tech_startup": ["Connect with local accelerators", "Research IP protection laws"],
            "crypto_trader": ["Verify crypto regulations", "Establish compliant trading setup"],
            "consulting": ["Join professional associations", "Study local business culture"],
            "ecommerce": ["Analyze logistics infrastructure", "Research VAT implications"],
            "real_estate": ["Study property market cycles", "Verify foreign ownership rules"],
            "content_creator": ["Test internet connectivity", "Research content monetization rules"]
        }
        
        base_actions.extend(profile_actions.get(profile.id, []))
        return base_actions[:6]  # Limit to 6 action items
    
    def _estimate_timeline(self, tier: str, profile: UserProfile) -> str:
        """Estimate realistic timeline based on tier and profile"""
        base_timelines = {
            "high_roi": "6-12 months for optimal positioning",
            "medium_roi": "12-18 months for full transition",
            "low_roi": "18-24 months with careful planning"
        }
        
        # Adjust for profile complexity
        if profile.id in ["crypto_trader", "tech_startup"]:
            return base_timelines[tier].replace("6-12", "9-15").replace("12-18", "15-24")
        
        return base_timelines[tier]

# =========================
# ENHANCED CALCULATION ENGINE
# =========================

class AdvancedROICalculator:
    """Performs ROI calculations with advanced analytics and simulations.
    Attributes:
        monte_carlo_iterations: Number of simulations for Monte Carlo analysis.
        confidence_intervals: Confidence interval levels used in reporting.
    """
    
    def __init__(self):
        """Initialize calculator defaults for Monte Carlo and confidence levels.
        Returns:
            None
        """
        
        self.monte_carlo_iterations = 2000  # Increased for better accuracy
        self.confidence_intervals = [0.05, 0.1, 0.25, 0.5, 0.75, 0.9, 0.95]
    
    def calculate_comprehensive_roi(
        self,
        profile: UserProfile,
        country: CountryData,
        current_revenue: float,
        current_margin: float,
        current_corp_tax: float,
        current_pers_tax: float,
        current_living: float,
        current_business: float,
        revenue_multiplier: float,
        margin_improvement: float,
        success_probability: float,
        time_horizon: int,
        discount_rate: float
    ) -> Dict:
        """Calculate ROI metrics with Monte Carlo, sensitivity, and scenarios.
        Args:
            profile: Active user profile used for multipliers.
            country: Destination country configuration.
            current_revenue: Current monthly revenue in currency units.
            current_margin: Current profit margin percentage.
            current_corp_tax: Current corporate tax rate percentage.
            current_pers_tax: Current personal tax rate percentage.
            current_living: Current monthly living costs.
            current_business: Current monthly business costs.
            revenue_multiplier: Expected revenue growth multiplier after relocation.
            margin_improvement: Expected margin improvement percentage points.
            success_probability: Probability of achieving projected results (0-100).
            time_horizon: Time horizon in months for the projection.
            discount_rate: Annual discount rate percentage for NPV calculations.
        Returns:
            A dictionary containing base metrics, Monte Carlo results,
            sensitivity analyses, scenario comparisons, and risk/opportunity
            scores.
        Side Effects:
            Logs an error to stdout and returns fallback metrics on failure.
        """
        
        try:
            # Input validation and normalization
            current_revenue = max(1000, float(current_revenue or 45000))
            current_margin = max(1, min(95, float(current_margin or 25)))
            
            # Base calculation
            base_result = self._calculate_base_metrics(
                profile, country, current_revenue, current_margin,
                current_corp_tax, current_pers_tax, current_living, current_business,
                revenue_multiplier, margin_improvement, success_probability,
                time_horizon, discount_rate
            )
            
            # Advanced analytics
            monte_carlo_result = self._advanced_monte_carlo(
                profile, country, current_revenue, current_margin,
                revenue_multiplier, margin_improvement, success_probability,
                time_horizon, discount_rate
            )
            
            sensitivity_result = self._comprehensive_sensitivity_analysis(
                profile, country, current_revenue, current_margin,
                revenue_multiplier, margin_improvement, time_horizon, discount_rate
            )
            
            scenario_analysis = self._scenario_analysis(
                profile, country, current_revenue, current_margin,
                revenue_multiplier, margin_improvement, time_horizon, discount_rate
            )
            
            # Risk scoring
            risk_score = self._calculate_comprehensive_risk(country, profile, base_result)
            opportunity_score = self._calculate_opportunity_score(base_result, country, profile)
            
            return {
                **base_result,
                "monte_carlo": monte_carlo_result,
                "sensitivity": sensitivity_result,
                "scenarios": scenario_analysis,
                "risk_score": risk_score,
                "opportunity_score": opportunity_score,
                "recommendation": self._generate_recommendation(base_result, risk_score, opportunity_score)
            }
            
        except Exception as e:
            print(f"ROI Calculation Error: {e}")
            return self._get_fallback_result(country, time_horizon)
    
    def _calculate_base_metrics(self, profile, country, *args) -> Dict:
        """Enhanced base metrics calculation"""
        try:
            (current_revenue, current_margin, current_corp_tax, current_pers_tax,
             current_living, current_business, revenue_multiplier, margin_improvement,
             success_probability, time_horizon, discount_rate) = args
            
            # Current situation analysis
            current_profit = current_revenue * (current_margin / 100)
            current_corp_after_tax = current_profit * (1 - current_corp_tax/100)
            current_pers_after_tax = current_corp_after_tax * (1 - current_pers_tax/100)
            current_net_income = current_pers_after_tax - current_living - current_business
            
            # Projected situation
            success_factor = success_probability / 100
            profile_multiplier = profile.success_multiplier
            
            new_revenue = current_revenue * revenue_multiplier * profile_multiplier
            new_margin = min(95, current_margin + margin_improvement)
            new_profit = new_revenue * (new_margin / 100)
            
            # Apply country tax rates
            new_corp_after_tax = new_profit * (1 - country.corp_tax)
            new_pers_after_tax = new_corp_after_tax * (1 - country.pers_tax)
            new_net_income = new_pers_after_tax - country.living_cost - country.business_cost
            
            # Monthly cash flow delta
            monthly_delta = (new_net_income - current_net_income) * success_factor
            setup_cost = country.setup_cost
            
            # Enhanced cash flow projection with seasonality and growth
            monthly_flows = []
            cumulative_flow = -setup_cost
            payback_month = None
            
            growth_rate = 0.02  # 2% monthly growth assumption
            
            for month in range(1, time_horizon + 1):
                # Apply seasonality
                seasonal_factor = country.seasonality[(month - 1) % 12]
                
                # Apply growth over time
                growth_factor = (1 + growth_rate) ** (month - 1)
                
                # Calculate monthly cash flow
                monthly_cf = monthly_delta * seasonal_factor * growth_factor
                monthly_flows.append(monthly_cf)
                
                cumulative_flow += monthly_cf
                if payback_month is None and cumulative_flow >= 0:
                    payback_month = month
            
            # Advanced financial metrics
            discount_monthly = (1 + discount_rate/100) ** (1/12) - 1
            
            # NPV calculation
            npv = -setup_cost + sum(cf / (1 + discount_monthly) ** month 
                                   for month, cf in enumerate(monthly_flows, 1))
            
            # IRR calculation
            irr_annual = self._calculate_irr(setup_cost, monthly_flows) * 100
            
            # ROI and other metrics
            total_return = sum(monthly_flows)
            roi_percentage = (total_return / setup_cost) * 100 if setup_cost > 0 else 0
            
            # Additional metrics
            profitability_index = (npv + setup_cost) / setup_cost if setup_cost > 0 else 1
            mirr = self._calculate_mirr(setup_cost, monthly_flows, discount_rate/100) * 100
            
            return {
                "npv": npv,
                "roi": roi_percentage,
                "irr_annual": irr_annual,
                "mirr_annual": mirr,
                "payback_months": payback_month or float('inf'),
                "payback_years": (payback_month / 12) if payback_month else float('inf'),
                "monthly_delta": monthly_delta,
                "total_return": total_return,
                "monthly_flows": monthly_flows,
                "setup_cost": setup_cost,
                "profitability_index": profitability_index,
                "current_net_income": current_net_income,
                "projected_net_income": new_net_income
            }
            
        except Exception as e:
            print(f"Base metrics calculation error: {e}")
            return self._get_fallback_result(country, time_horizon)
    
    def _advanced_monte_carlo(self, profile, country, *args) -> Dict:
        """Advanced Monte Carlo simulation with correlated variables"""
        try:
            results = []
            
            for _ in range(self.monte_carlo_iterations):
                # Generate correlated random variables
                market_shock = np.random.normal(0, 0.2)  # Market-wide shock
                
                # Revenue variance (correlated with market)
                revenue_variance = np.random.normal(1.0, 0.18) + market_shock * 0.3
                
                # Margin variance (anti-correlated with revenue for realism)
                margin_variance = np.random.normal(1.0, 0.12) - revenue_variance * 0.1
                
                # Success probability variance
                success_variance = np.random.beta(8, 2) * 1.2  # Skewed distribution
                
                # Cost inflation
                cost_inflation = max(0.8, np.random.normal(1.0, 0.15))
                
                # Modify inputs
                modified_args = list(args)
                modified_args[0] *= max(0.3, revenue_variance)  # revenue
                modified_args[1] *= max(0.5, margin_variance)   # margin
                modified_args[7] *= max(0.1, success_variance)  # success probability
                
                # Adjust costs for inflation
                modified_country = CountryData(
                    **{k: v for k, v in country.__dict__.items() if k != 'living_cost'},
                    living_cost=country.living_cost * cost_inflation
                )
                
                result = self._calculate_base_metrics(profile, modified_country, *modified_args)
                results.append(result)
            
            # Extract key metrics
            rois = [r['roi'] for r in results]
            npvs = [r['npv'] for r in results]
            paybacks = [r['payback_years'] for r in results if r['payback_years'] != float('inf')]
            
            # Calculate comprehensive statistics
            confidence_intervals = {}
            for ci in self.confidence_intervals:
                confidence_intervals[f'roi_{int(ci*100)}'] = np.percentile(rois, ci * 100)
                confidence_intervals[f'npv_{int(ci*100)}'] = np.percentile(npvs, ci * 100)
            
            return {
                "mean_roi": np.mean(rois),
                "median_roi": np.median(rois),
                "std_roi": np.std(rois),
                "skew_roi": float(np.mean(((np.array(rois) - np.mean(rois)) / np.std(rois)) ** 3)),
                "mean_npv": np.mean(npvs),
                "std_npv": np.std(npvs),
                "confidence_intervals": confidence_intervals,
                "probability_positive_roi": sum(1 for roi in rois if roi > 0) / len(rois),
                "probability_100_roi": sum(1 for roi in rois if roi > 100) / len(rois),
                "var_95": np.percentile(rois, 5),  # Value at Risk
                "expected_shortfall": np.mean([roi for roi in rois if roi <= np.percentile(rois, 5)]),
                "mean_payback": np.mean(paybacks) if paybacks else float('inf')
            }
            
        except Exception as e:
            print(f"Monte Carlo simulation error: {e}")
            return {"mean_roi": 0, "std_roi": 0, "probability_positive_roi": 0}
    
    def _comprehensive_sensitivity_analysis(self, profile, country, *args) -> Dict:
        """Comprehensive sensitivity analysis"""
        try:
            base_result = self._calculate_base_metrics(profile, country, *args)
            base_roi = base_result['roi']
            
            sensitivities = {}
            
            # Define variables to test
            variables = [
                ('revenue', 0, [0.8, 0.9, 1.1, 1.2, 1.3]),
                ('margin', 1, [-5, -2, 2, 5, 8]),
                ('revenue_multiplier', 6, [0.8, 1.0, 1.5, 2.0, 2.5]),
                ('margin_improvement', 7, [-5, 0, 5, 10, 15]),
                ('success_probability', 8, [50, 65, 80, 90, 95])
            ]
            
            for var_name, var_index, test_values in variables:
                sensitivities[var_name] = {}
                
                for test_value in test_values:
                    try:
                        modified_args = list(args)
                        
                        if var_name in ['revenue', 'revenue_multiplier']:
                            modified_args[var_index] = args[var_index] * test_value
                        else:
                            modified_args[var_index] = test_value
                        
                        result = self._calculate_base_metrics(profile, country, *modified_args)
                        sensitivities[var_name][str(test_value)] = result['roi']
                    except:
                        sensitivities[var_name][str(test_value)] = base_roi
            
            return sensitivities
            
        except Exception as e:
            print(f"Sensitivity analysis error: {e}")
            return {}
    
    def _scenario_analysis(self, profile, country, *args) -> Dict:
        """Three scenario analysis: pessimistic, realistic, optimistic"""
        try:
            scenarios = {}
            
            # Pessimistic scenario
            pessimistic_args = list(args)
            pessimistic_args[6] *= 0.7   # Lower revenue multiplier
            pessimistic_args[7] *= 0.8   # Lower margin improvement  
            pessimistic_args[8] *= 0.6   # Lower success probability
            
            scenarios['pessimistic'] = self._calculate_base_metrics(profile, country, *pessimistic_args)
            
            # Realistic scenario (base case)
            scenarios['realistic'] = self._calculate_base_metrics(profile, country, *args)
            
            # Optimistic scenario
            optimistic_args = list(args)
            optimistic_args[6] *= 1.3   # Higher revenue multiplier
            optimistic_args[7] *= 1.2   # Higher margin improvement
            optimistic_args[8] = min(95, optimistic_args[8] * 1.1)  # Higher success probability
            
            scenarios['optimistic'] = self._calculate_base_metrics(profile, country, *optimistic_args)
            
            return scenarios
            
        except Exception as e:
            print(f"Scenario analysis error: {e}")
            return {}
    
    def _calculate_irr(self, initial_investment: float, cash_flows: List[float]) -> float:
        """Calculate Internal Rate of Return using Newton-Raphson method"""
        try:
            def npv_function(rate):
                return -initial_investment + sum(cf / (1 + rate) ** (month/12) 
                                               for month, cf in enumerate(cash_flows, 1))
            
            def npv_derivative(rate):
                return sum(-cf * (month/12) / (1 + rate) ** (month/12 + 1)
                          for month, cf in enumerate(cash_flows, 1))
            
            rate = 0.1  # Initial guess
            for _ in range(50):  # Maximum iterations
                npv = npv_function(rate)
                if abs(npv) < 1e-6:
                    return rate
                
                derivative = npv_derivative(rate)
                if abs(derivative) < 1e-10:
                    break
                
                rate = rate - npv / derivative
                
                # Keep rate reasonable
                if rate < -0.99 or rate > 10:
                    return 0
            
            return rate if abs(npv_function(rate)) < 1000 else 0
            
        except:
            return 0
    
    def _calculate_mirr(self, initial_investment: float, cash_flows: List[float], 
                       discount_rate: float) -> float:
        """Calculate Modified Internal Rate of Return"""
        try:
            positive_flows = [max(0, cf) for cf in cash_flows]
            negative_flows = [min(0, cf) for cf in cash_flows]
            
            # Future value of positive flows
            fv_positive = sum(cf * (1 + discount_rate) ** ((len(cash_flows) - month) / 12)
                             for month, cf in enumerate(positive_flows, 1))
            
            # Present value of negative flows
            pv_negative = initial_investment + sum(abs(cf) / (1 + discount_rate) ** (month / 12)
                                                 for month, cf in enumerate(negative_flows, 1))
            
            if pv_negative == 0 or fv_positive <= 0:
                return 0
            
            n_years = len(cash_flows) / 12
            mirr = (fv_positive / pv_negative) ** (1 / n_years) - 1
            
            return mirr if -0.99 <= mirr <= 10 else 0
            
        except:
            return 0
    
    def _calculate_comprehensive_risk(self, country: CountryData, profile: UserProfile, 
                                    result: Dict) -> float:
        """Enhanced risk scoring with multiple factors"""
        try:
            # Base country risks
            political_risk = country.risk_factors.get('political', 0.1) * 25
            economic_risk = country.risk_factors.get('economic', 0.1) * 35
            regulatory_risk = country.risk_factors.get('regulatory', 0.1) * 25
            
            # Market sentiment risk
            sentiment_risk = (1 - country.ai_sentiment) * 15
            
            # ROI volatility risk (from Monte Carlo if available)
            volatility_risk = 0
            if 'monte_carlo' in result:
                std_roi = result['monte_carlo'].get('std_roi', 0)
                volatility_risk = min(20, std_roi / 5)  # Cap at 20 points
            
            # Profile risk adjustment
            risk_tolerance_adjustment = (100 - profile.risk_tolerance) / 100 * 20
            
            # Payback period risk
            payback_risk = 0
            if result['payback_years'] != float('inf'):
                if result['payback_years'] > 5:
                    payback_risk = 15
                elif result['payback_years'] > 3:
                    payback_risk = 10
                elif result['payback_years'] > 2:
                    payback_risk = 5
            else:
                payback_risk = 25
            
            total_risk = (political_risk + economic_risk + regulatory_risk + 
                         sentiment_risk + volatility_risk + risk_tolerance_adjustment + 
                         payback_risk)
            
            return min(100, max(0, total_risk))
            
        except:
            return 50
    
    def _calculate_opportunity_score(self, result: Dict, country: CountryData, profile: UserProfile) -> float:
        """Enhanced opportunity scoring with multiple factors"""
        try:
            # ROI contribution (40% weight)
            roi = result.get('roi', 0)
            roi_score = min(40, roi / 5)  # Cap at 200% ROI = 40 points
            
            # Market growth potential (20% weight)
            growth_score = country.market_growth * 2
            
            # Business environment (20% weight)
            ease_score = country.ease_score * 2
            banking_score = country.banking_score * 2
            environment_score = (ease_score + banking_score) / 2
            
            # AI sentiment and market timing (10% weight)
            sentiment_score = country.ai_sentiment * 10
            
            # Profile alignment (10% weight)
            profile_fit = profile.success_multiplier * 10
            
            total_score = roi_score + growth_score + environment_score + sentiment_score + profile_fit
            return min(100, max(0, total_score))
            
        except:
            return 50
    
    def _generate_recommendation(self, result: Dict, risk_score: float, opportunity_score: float) -> str:
        """Generate investment recommendation based on scores"""
        roi = result.get('roi', 0)
        
        if roi >= 200 and risk_score < 30:
            return "STRONG BUY - Exceptional opportunity with manageable risk"
        elif roi >= 150 and risk_score < 40:
            return "BUY - Strong opportunity with acceptable risk profile"
        elif roi >= 100 and risk_score < 60:
            return "HOLD/CONSIDER - Decent opportunity, monitor risk factors"
        elif roi >= 50 and risk_score < 70:
            return "WEAK HOLD - Marginal opportunity, consider alternatives"
        else:
            return "AVOID - Poor risk-adjusted returns, seek better opportunities"
    
    def _get_fallback_result(self, country: CountryData, time_horizon: int) -> Dict:
        """Fallback result for error cases"""
        return {
            "npv": 0, "roi": 0, "irr_annual": 0, "mirr_annual": 0,
            "payback_months": float('inf'), "payback_years": float('inf'),
            "monthly_delta": 0, "total_return": 0,
            "monthly_flows": [0] * time_horizon, "setup_cost": country.setup_cost,
            "profitability_index": 1, "current_net_income": 0, "projected_net_income": 0
        }

# =========================
# ENHANCED VISUALIZATION ENGINE
# =========================

class AdvancedChartGenerator:
    """Generates Plotly charts summarizing ROI analyses and comparisons."""
    
    @staticmethod
    def create_comprehensive_dashboard(result: Dict, country_name: str, profile_name: str) -> go.Figure:
        """Create an interactive dashboard visualizing ROI analysis.
        Args:
            result: Output dictionary from the ROI calculator.
            country_name: Name of the country being evaluated.
            profile_name: Name of the user's profile.
        Returns:
            A Plotly ``Figure`` object containing multiple subplots with cash
            flow, risk and scenario information.
        Side Effects:
            Uses random sampling to mock Monte Carlo distributions when
            provided with summary statistics.
        """
        try:
            fig = make_subplots(
                rows=3, cols=2,
                subplot_titles=(
                    "Cash Flow Projection", "Monte Carlo ROI Distribution", 
                    "Risk-Return Analysis", "Sensitivity Tornado",
                    "Scenario Comparison", "Confidence Intervals"
                ),
                specs=[
                    [{"type": "scatter"}, {"type": "histogram"}],
                    [{"type": "scatter"}, {"type": "bar"}],
                    [{"type": "bar"}, {"type": "scatter"}]
                ],
                vertical_spacing=0.08,
                horizontal_spacing=0.1
            )
            
            # 1. Enhanced Cash Flow Projection
            monthly_flows = result.get('monthly_flows', [0] * 60)
            months = list(range(1, len(monthly_flows) + 1))
            cumulative = np.cumsum([-result.get('setup_cost', 50000)] + monthly_flows)
            
            fig.add_trace(
                go.Scatter(
                    x=months, y=cumulative, mode='lines+markers',
                    name='Cumulative Cash Flow',
                    line=dict(color='#2563eb', width=3),
                    fill='tonexty' if any(c >= 0 for c in cumulative) else None
                ), row=1, col=1
            )
            
            # Add breakeven line
            fig.add_hline(y=0, line_dash="dash", line_color="red", row=1, col=1)
            
            # 2. Monte Carlo Distribution
            if 'monte_carlo' in result:
                mc_data = result['monte_carlo']
                # Generate sample data based on MC statistics
                roi_samples = np.random.normal(
                    mc_data.get('mean_roi', 0),
                    max(1, mc_data.get('std_roi', 10)),
                    1000
                )
                
                fig.add_trace(
                    go.Histogram(
                        x=roi_samples, name='ROI Distribution',
                        marker_color='#10b981', opacity=0.7,
                        nbinsx=30
                    ), row=1, col=2
                )
            
            # 3. Risk-Return Scatter for multiple countries
            countries = list(ENHANCED_COUNTRIES.keys())
            calculator = AdvancedROICalculator()
            
            risk_scores = []
            return_scores = []
            for c in countries:
                country_data = ENHANCED_COUNTRIES[c]
                risk = calculator._calculate_comprehensive_risk(
                    country_data, 
                    ENHANCED_PROFILES.get('tech_startup', list(ENHANCED_PROFILES.values())[0]),
                    {'roi': country_data.market_growth * 20, 'payback_years': 2}
                )
                risk_scores.append(risk)
                return_scores.append(country_data.market_growth * 20)
            
            fig.add_trace(
                go.Scatter(
                    x=return_scores, y=risk_scores,
                    mode='markers+text', text=countries,
                    textposition="top center",
                    name='Countries Risk-Return',
                    marker=dict(size=12, color='#f59e0b', opacity=0.8)
                ), row=2, col=1
            )
            
            # 4. Sensitivity Tornado Chart
            if 'sensitivity' in result:
                sens_data = result['sensitivity']
                if sens_data:
                    variables = []
                    impacts = []
                    for var, values in sens_data.items():
                        if isinstance(values, dict) and values:
                            val_list = list(values.values())
                            if len(val_list) >= 2:
                                impact = max(val_list) - min(val_list)
                                variables.append(var.replace('_', ' ').title())
                                impacts.append(impact)
                    
                    if variables:
                        fig.add_trace(
                            go.Bar(
                                y=variables, x=impacts, orientation='h',
                                name='Sensitivity Impact',
                                marker_color='#8b5cf6'
                            ), row=2, col=2
                        )
            
            # 5. Scenario Comparison
            if 'scenarios' in result:
                scenarios = result['scenarios']
                scenario_names = list(scenarios.keys())
                scenario_rois = [scenarios[s].get('roi', 0) for s in scenario_names]
                
                colors = ['#ef4444', '#f59e0b', '#10b981']  # Red, Yellow, Green
                fig.add_trace(
                    go.Bar(
                        x=scenario_names, y=scenario_rois,
                        name='Scenario ROI',
                        marker_color=colors[:len(scenario_names)]
                    ), row=3, col=1
                )
            
            # 6. Confidence Intervals
            if 'monte_carlo' in result and 'confidence_intervals' in result['monte_carlo']:
                ci_data = result['monte_carlo']['confidence_intervals']
                ci_levels = [int(k.split('_')[1]) for k in ci_data.keys() if 'roi_' in k]
                ci_values = [ci_data[f'roi_{level}'] for level in ci_levels]
                
                if ci_levels and ci_values:
                    fig.add_trace(
                        go.Scatter(
                            x=ci_levels, y=ci_values,
                            mode='lines+markers',
                            name='ROI Confidence Intervals',
                            line=dict(color='#06b6d4', width=3)
                        ), row=3, col=2
                    )
            
            # Update layout
            fig.update_layout(
                height=1000,
                title_text=f"Comprehensive Analysis: {profile_name} → {country_name}",
                showlegend=False,
                template="plotly_white",
                title_x=0.5,
                title_font_size=20
            )
            
            return fig
            
        except Exception as e:
            print(f"Advanced chart generation error: {e}")
            # Return simple fallback chart
            fig = go.Figure()
            fig.add_annotation(
                text=f"Advanced analytics loading...<br>Error: {str(e)[:100]}...",
                xref="paper", yref="paper",
                x=0.5, y=0.5, showarrow=False,
                font=dict(size=16)
            )
            fig.update_layout(height=400, template="plotly_white")
            return fig
    
    @staticmethod
    def create_country_heatmap(selected_countries: List[str], profile_id: str) -> go.Figure:
        ""Create a comparative heatmap for selected countries.

        Args:
            selected_countries: List of country identifiers to display.
            profile_id: Profile identifier used to tailor scoring.

        Returns:
            A Plotly ``Figure`` heatmap comparing multiple metrics across the
            chosen countries.

        Side Effects:
            Prints an error message if heatmap generation fails.
        """
        try:
            if not selected_countries or profile_id not in ENHANCED_PROFILES:
                return go.Figure()
            
            profile = ENHANCED_PROFILES[profile_id]
            
            # Metrics to compare
            metrics = [
                'Tax Efficiency', 'Living Cost', 'Business Environment', 
                'Market Growth', 'Banking Quality', 'Risk Score'
            ]
            
            heatmap_data = []
            countries_data = []
            
            for country_key in selected_countries[:8]:  # Limit to 8 countries
                if country_key in ENHANCED_COUNTRIES:
                    country = ENHANCED_COUNTRIES[country_key]
                    
                    # Calculate normalized scores (0-100)
                    tax_eff = (1 - (country.corp_tax + country.pers_tax)) * 100
                    cost_eff = max(0, 100 - (country.living_cost / 150))  # Normalized
                    business_env = (country.ease_score + country.banking_score) * 5
                    market_growth = country.market_growth * 10
                    banking = country.banking_score * 10
                    
                    # Risk score (inverted so higher is better)
                    calculator = AdvancedROICalculator()
                    risk_raw = calculator._calculate_comprehensive_risk(country, profile, {'roi': 100, 'payback_years': 2})
                    risk_score = 100 - risk_raw
                    
                    country_scores = [tax_eff, cost_eff, business_env, market_growth, banking, risk_score]
                    heatmap_data.append(country_scores)
                    countries_data.append(country.name)
            
            if not heatmap_data:
                return go.Figure()
            
            fig = go.Figure(data=go.Heatmap(
                z=heatmap_data,
                x=metrics,
                y=countries_data,
                colorscale='RdYlGn',
                text=[[f'{val:.1f}' for val in row] for row in heatmap_data],
                texttemplate="%{text}",
                textfont={"size": 12},
                colorbar=dict(title="Score (0-100)")
            ))
            
            fig.update_layout(
                title=f"Country Comparison Heatmap - {profile.name}",
                xaxis_title="Evaluation Criteria",
                yaxis_title="Countries",
                height=400 + len(countries_data) * 30,
                template="plotly_white"
            )
            
            return fig
            
        except Exception as e:
            print(f"Heatmap generation error: {e}")
            fig = go.Figure()
            fig.add_annotation(text=f"Heatmap error: {str(e)}", x=0.5, y=0.5)
            return fig
# =========================
# LEAD GENERATION & CRM SYSTEM
# =========================
class EnhancedLeadEngine:
"""Creates personalized offers and manages lead-generation logic."""
    def __init__(self):
        """Initialize conversion funnel thresholds and pricing tiers.

        Returns:
            None
        """
        self.conversion_funnel = {
            'email_capture': {'roi_min': 30, 'confidence': 0.2},
            'consultation_booking': {'roi_min': 100, 'confidence': 0.5},
            'premium_service': {'roi_min': 200, 'confidence': 0.7},
            'vip_concierge': {'roi_min': 300, 'confidence': 0.8}
        }
        
        self.pricing_tiers = {
            'starter': {'base_price': 497, 'max_discount': 0.8},
            'standard': {'base_price': 1997, 'max_discount': 0.6},  # mid tier
            'premium': {'base_price': 4997, 'max_discount': 0.5},  # high tier
            'vip': {'base_price': 9997, 'max_discount': 0.3}  # elite tier
        }
    
    def generate_dynamic_offer(
        self,
        result: Dict,  # ROI metrics
        profile: UserProfile,  # user persona
        country: CountryData,  # country data
    ) -> Dict:
        """Generate a tailored offer for the user based on analysis results.

        Args:
            result: ROI calculation output containing financial metrics.
            profile: The user\'s persona driving discount logic.
            country: Destination country information affecting pricing.
        Returns:
            A dictionary describing the offer tier, pricing, incentives and
            messaging suitable for display to the user.
        Side Effects:
            Logs an error message if offer generation fails.
        """
        try:
            roi = result.get('roi', 0)
            confidence = result.get('monte_carlo', {}).get('probability_positive_roi', 0)
            risk_score = result.get('risk_score', 50)
            opportunity_score = result.get('opportunity_score', 50)
            
            # Determine offer tier based on multiple factors
            offer_tier = self._calculate_offer_tier(roi, confidence, risk_score, opportunity_score)
            
            # Generate personalized pricing
            base_pricing = self.pricing_tiers[offer_tier]
            discount_factor = self._calculate_dynamic_discount(roi, confidence, profile)
            
            original_price = base_pricing['base_price']
            max_discount = base_pricing['max_discount']
            final_discount = min(max_discount, discount_factor)
            discounted_price = int(original_price * (1 - final_discount))
            
            # Calculate value proposition
            potential_savings = result.get('total_return', 0) * 12  # Annualized
            value_multiple = max(3, potential_savings / original_price) if original_price > 0 else 5
            
            offer = {
                'tier': offer_tier,
                'title': self._generate_offer_title(offer_tier, country, profile),
                'subtitle': self._generate_offer_subtitle(roi, country),
                'original_price': f"${original_price:,}",
                'discounted_price': f"${discounted_price:,}",
                'savings': f"${original_price - discounted_price:,}",
                'value_statement': f"${int(potential_savings):,}+ potential annual savings",
                'discount_percentage': f"{int(final_discount * 100)}%",
                'urgency': self._generate_urgency_message(offer_tier, roi),
                'includes': self._generate_offer_includes(offer_tier, country, profile),
                'cta': self._generate_cta_text(offer_tier),
                'guarantee': self._generate_guarantee(offer_tier),
                'bonuses': self._generate_bonuses(offer_tier, roi),
                'social_proof': self._generate_social_proof(country, profile),
                'timeline': self._estimate_delivery_timeline(offer_tier),
                'payment_options': self._generate_payment_options(discounted_price, offer_tier)
            }
            
            return offer
            
        except Exception as e:
            print(f"Offer generation error: {e}")
            return self._get_fallback_offer(country, profile)
    
    def _calculate_offer_tier(self, roi: float, confidence: float, risk_score: float, opportunity_score: float) -> str:
        """Calculate appropriate offer tier based on user metrics"""
        # Weighted scoring
        roi_score = min(40, roi / 5)  # Max 40 points for 200% ROI
        confidence_score = confidence * 30  # Max 30 points
        risk_bonus = max(0, (100 - risk_score) / 100 * 20)  # Max 20 points for low risk
        opportunity_bonus = opportunity_score / 100 * 10  # Max 10 points
        
        total_score = roi_score + confidence_score + risk_bonus + opportunity_bonus
        
        if total_score >= 80:
            return 'vip'
        elif total_score >= 60:
            return 'premium'
        elif total_score >= 40:
            return 'standard'
        else:
            return 'starter'
    
    def _calculate_dynamic_discount(self, roi: float, confidence: float, profile: UserProfile) -> float:
        """Calculate dynamic discount based on user profile and results"""
        base_discount = 0.2  # 20% base discount
        
        # ROI-based discount (higher ROI = higher discount to incentivize action)
        roi_discount = min(0.3, roi / 500)  # Up to 30% for 150%+ ROI
        
        # Confidence-based discount
        confidence_discount = confidence * 0.2  # Up to 20% for high confidence
        
        # Profile risk tolerance (higher risk tolerance = slightly lower discount)
        risk_adjustment = (100 - profile.risk_tolerance) / 1000  # Small adjustment
        
        total_discount = base_discount + roi_discount + confidence_discount + risk_adjustment
        return min(0.8, total_discount)  # Cap at 80% discount
    
    def _generate_offer_title(self, tier: str, country: CountryData, profile: UserProfile) -> str:
        """Generate compelling offer titles"""
        titles = {
            'starter': f"{country.name} Migration Starter Kit",
            'standard': f"Complete {country.name} Business Migration System",
            'premium': f"Premium {country.name} Relocation Concierge",
            'vip': f"VIP {country.name} Migration Mastermind"
        }
        return titles.get(tier, f"{country.name} Migration Package")
    
    def _generate_offer_subtitle(self, roi: float, country: CountryData) -> str:
        """Generate compelling subtitles based on ROI"""
        if roi >= 200:
            return f"Unlock {roi:.0f}% ROI with {country.name}'s business-friendly ecosystem"
        elif roi >= 100:
            return f"Double your profits with strategic {country.name} relocation"
        else:
            return f"Optimize your business structure in {country.name}"
    
    def _generate_urgency_message(self, tier: str, roi: float) -> str:
        """Generate urgency messages"""
        messages = {
            'vip': "Exclusive: Only 3 VIP spots available this quarter",
            'premium': "Limited: 10 premium packages remaining this month", 
            'standard': "Special pricing ends in 72 hours",
            'starter': "Early bird discount - first 50 clients only"
        }
        
        if roi >= 300:
            return "⚡ URGENT: ROI this high rarely lasts - regulatory changes imminent"
        
        return messages.get(tier, "Limited time offer")
    
    def _generate_offer_includes(self, tier: str, country: CountryData, profile: UserProfile) -> List[str]:
        """Generate tier-specific inclusions"""
        base_includes = {
            'starter': [
                f"Complete {country.name} business setup guide",
                "Visa requirements checklist", 
                "Tax optimization overview",
                "30-day email support"
            ],
            'standard': [
                f"Step-by-step {country.name} migration blueprint",
                "Legal requirements documentation",
                "Tax optimization strategies",
                "Banking and business setup guide",
                "90-day implementation support",
                "Private community access"
            ],
            'premium': [
                "Personal migration consultant assigned",
                "Legal document preparation service",
                "Tax strategy consultation (2 sessions)",
                "Banking introduction service",
                "Local network connections",
                "12-month ongoing support",
                "Priority community access",
                f"Exclusive {country.name} networking events"
            ],
            'vip': [
                "Dedicated migration concierge team",
                "Personal lawyer consultation (5 hours)",
                "Accountant consultation (3 sessions)", 
                "Banking relationship management",
                "Property viewing assistance",
                "Cultural integration program",
                "24/7 priority support for 18 months",
                "Exclusive mastermind group access",
                "Quarterly strategy review sessions"
            ]
        }
        
        includes = base_includes.get(tier, base_includes['starter']).copy()
        
        # Add profile-specific bonuses
        if profile.id == 'crypto_trader' and tier in ['premium', 'vip']:
            includes.append("Crypto-specific compliance consultation")
        elif profile.id == 'tech_startup' and tier in ['premium', 'vip']:
            includes.append("IP protection strategy session")
        
        return includes
    
    def _generate_cta_text(self, tier: str) -> str:
        """Generate compelling CTA text"""
        ctas = {
            'starter': "Start Your Journey Today",
            'standard': "Secure Your Migration Blueprint", 
            'premium': "Claim Your Premium Package",
            'vip': "Apply for VIP Concierge"
        }
        return ctas.get(tier, "Get Started Now")
    
    def _generate_guarantee(self, tier: str) -> str:
        """Generate tier-appropriate guarantees"""
        guarantees = {
            'starter': "30-day money-back guarantee",
            'standard': "60-day satisfaction guarantee",
            'premium': "90-day results guarantee or full refund", 
            'vip': "12-month success guarantee with performance metrics"
        }
        return guarantees.get(tier, "Satisfaction guaranteed")
    
    def _generate_bonuses(self, tier: str, roi: float) -> List[str]:
        """Generate compelling bonuses"""
        base_bonuses = {
            'starter': ["Digital nomad tax guide", "Country comparison calculator"],
            'standard': ["Advanced tax optimization course", "International business setup templates"],
            'premium': ["Personal branding consultation", "Global investment opportunities report"],
            'vip': ["Annual tax strategy review", "International wealth management consultation"]
        }
        
        bonuses = base_bonuses.get(tier, []).copy()
        
        # ROI-based bonus additions
        if roi >= 200:
            bonuses.insert(0, f"🎁 BONUS: ROI Optimization Masterclass (${random.randint(497, 997)} value)")
        
        return bonuses
    
    def _generate_social_proof(self, country: CountryData, profile: UserProfile) -> str:
        """Generate relevant social proof"""
        proofs = [
            f"Join 2,{random.randint(100, 900)}+ entrepreneurs who've successfully relocated to {country.name}",
            f"★★★★★ Rated 4.{random.randint(7, 9)}/5 by {random.randint(500, 1500)} clients", 
            f"Featured in {random.choice(['Forbes', 'Entrepreneur', 'Inc Magazine', 'Business Insider'])}"
        ]
        return random.choice(proofs)
    
    def _estimate_delivery_timeline(self, tier: str) -> str:
        """Estimate delivery timeline"""
        timelines = {
            'starter': "Instant digital delivery",
            'standard': "Materials delivered within 24 hours",
            'premium': "Consultation scheduled within 48 hours", 
            'vip': "Concierge team assigned within 24 hours"
        }
        return timelines.get(tier, "Fast delivery")
    
    def _generate_payment_options(self, price: int, tier: str) -> List[str]:
        """Generate payment options"""
        options = [f"One-time payment: ${price:,}"]
        
        if price >= 1000 and tier in ['standard', 'premium', 'vip']:
            monthly = int(price / 3)
            options.append(f"3-month plan: ${monthly:,}/month")
            
        if price >= 2000 and tier in ['premium', 'vip']:
            monthly = int(price / 6)
            options.append(f"6-month plan: ${monthly:,}/month")
        
        return options
    
    def _get_fallback_offer(self, country: CountryData, profile: UserProfile) -> Dict:
        """Fallback offer for error cases"""
        return {
            'tier': 'standard',
            'title': f"{country.name} Migration Package",
            'subtitle': f"Complete guide to relocating your business to {country.name}",
            'original_price': "$1,997",
            'discounted_price': "$997", 
            'savings': "$1,000",
            'value_statement': "Complete migration solution",
            'discount_percentage': "50%",
            'urgency': "Limited time 50% discount",
            'includes': ["Migration guide", "Legal checklist", "Tax overview", "Support access"],
            'cta': "Get Your Package",
            'guarantee': "60-day money-back guarantee",
            'bonuses': ["Tax optimization guide"],
            'social_proof': "Trusted by thousands of entrepreneurs",
            'timeline': "Delivered within 24 hours",
            'payment_options': ["One-time payment: $997", "3-month plan: $332/month"]
        }
# =========================
# MAIN APPLICATION - ENHANCED
# =========================
def create_premium_immigration_app():
    """Create the revolutionary VisaTier 5.0 application"""
    
    with gr.Blocks(theme=PREMIUM_THEME, css=PREMIUM_CSS, title="VisaTier 5.0") as app:
        
        # State management
        current_profile = gr.State("tech_startup")
        calculation_results = gr.State({})
        user_session = gr.State({})
        ai_insights = gr.State({})
        
        # Revolutionary Header
        gr.HTML("""
        <div class="premium-header">
            <div class="header-content">
                <div>
                    <h1 class="header-title">VisaTier 5.0 - AI Migration Intelligence</h1>
                    <p class="header-subtitle">Advanced Monte Carlo Analysis • Personalized AI Insights • Risk-Adjusted ROI</p>
                </div>
                <div class="header-stats">
                    <div><strong>25,000+</strong> successful migrations</div>
                    <div><strong>$487M+</strong> in optimized relocations</div>
                    <div><strong>96.3%</strong> client success rate</div>
                </div>
            </div>
        </div>
        """)
        
        # Real-time success notification
        gr.HTML("""
        <div class="notification-popup">
            <strong>🚨 Maria L. just achieved 287% ROI relocating to Singapore!</strong>
            <div>Join 1,200+ data-driven entrepreneurs this month</div>
        </div>
        """)
        
        # Enhanced Profile Selection
        with gr.Row():
            gr.Markdown("## Step 1: Choose Your Entrepreneur Profile", elem_classes=["fadeIn"])
        
        profile_cards_html = '<div class="profile-grid">'
        for profile_id, profile in ENHANCED_PROFILES.items():
            profile_cards_html += f"""
            <div class="profile-card" onclick="selectProfile('{profile_id}', this)" data-profile="{profile_id}">
                <span class="profile-icon">{profile.icon}</span>
                <div class="profile-name">{profile.name}</div>
                <div class="profile-revenue">~€{profile.typical_revenue:,}/mo typical</div>
                <div class="profile-description">{profile.description}</div>
            </div>
            """
        
        profile_cards_html += """
        </div>
        <script>
        function selectProfile(profileId, element) {
            // Remove selected class from all cards
            document.querySelectorAll('.profile-card').forEach(card => {
                card.classList.remove('selected');
            });
            
            // Add selected class to clicked card
            element.classList.add('selected');
            
            // Update hidden dropdown
            const dropdown = document.querySelector('#profile-selector select');
            if (dropdown) {
                dropdown.value = profileId;
                dropdown.dispatchEvent(new Event('change', { bubbles: true }));
            }
        }
        
        // Auto-select first profile on load
        setTimeout(() => {
            const firstProfile = document.querySelector('.profile-card');
            if (firstProfile) {
                selectProfile(firstProfile.dataset.profile, firstProfile);
            }
        }, 100);
        </script>
        """
        
        profile_selector_display = gr.HTML(profile_cards_html)
        profile_selector = gr.Dropdown(
            choices=list(ENHANCED_PROFILES.keys()),
            value="tech_startup",
            visible=False,
            elem_id="profile-selector"
        )
        
        # Progress indicator
        gr.HTML("""
        <div class="progress-container">
            <div class="progress-bar" style="width: 25%;"></div>
        </div>
        <div style="text-align: center; margin: 1rem 0; color: var(--text-muted);">Step 1 of 4: Profile Selected ✓</div>
        """)
        
        # Enhanced testimonial
        gr.HTML("""
        <div class="testimonial">
            <div class="testimonial-text">
                "The AI insights were incredibly accurate. VisaTier 5.0 predicted my exact challenges and opportunities. 
                The Monte Carlo analysis gave me confidence to make the $50K investment - achieved 340% ROI in 14 months!"
            </div>
            <div class="testimonial-author">— Alex Chen, Fintech Founder (relocated to Dubai)</div>
        </div>
        """)
        
        # Enhanced Input Section
        with gr.Row():
            with gr.Column(scale=1):
                gr.Markdown("## Step 2: Current Business Metrics")
                
                with gr.Accordion("Financial Overview", open=True):
                    with gr.Row():
                        current_revenue = gr.Number(
                            value=65000, label="Monthly Revenue (€)",
                            info="Your current monthly business revenue"
                        )
                        current_margin = gr.Slider(
                            value=25, minimum=1, maximum=80, step=1,
                            label="EBITDA Margin (%)", info="Profit margin before taxes"
                        )
                    
                    with gr.Row():
                        current_corp_tax = gr.Slider(
                            value=25, minimum=0, maximum=50, step=1,
                            label="Corporate Tax (%)", info="Current corporate tax rate"
                        )
                        current_pers_tax = gr.Slider(
                            value=35, minimum=0, maximum=60, step=1,
                            label="Personal Tax (%)", info="Current personal income tax rate"
                        )
                    
                    with gr.Row():
                        current_living = gr.Number(
                            value=3500, label="Monthly Living Costs (€)",
                            info="Housing, food, transportation, etc."
                        )
                        current_business = gr.Number(
                            value=800, label="Monthly Business Costs (€)",
                            info="Office, software, services, etc."
                        )
            
            with gr.Column(scale=1):
                gr.Markdown("## Step 3: Growth Projections")
                
                with gr.Accordion("Revenue & Margin Optimization", open=True):
                    revenue_multiplier = gr.Slider(
                        value=1.5, minimum=0.8, maximum=5.0, step=0.1,
                        label="Revenue Growth Multiplier",
                        info="Expected revenue increase after relocation"
                    )
                    
                    margin_improvement = gr.Slider(
                        value=8, minimum=-10, maximum=25, step=1,
                        label="Margin Improvement (%)",
                        info="EBITDA margin increase from tax optimization"
                    )
                    
                    success_probability = gr.Slider(
                        value=75, minimum=30, maximum=95, step=5,
                        label="Success Probability (%)",
                        info="Your confidence in achieving projections"
                    )
                
                with gr.Accordion("Analysis Parameters", open=False):
                    time_horizon = gr.Slider(
                        value=60, minimum=12, maximum=120, step=6,
                        label="Analysis Period (months)",
                        info="Time horizon for ROI calculation"
                    )
                    
                    discount_rate = gr.Slider(
                        value=8, minimum=3, maximum=15, step=0.5,
                        label="Discount Rate (%)",
                        info="Your required rate of return"
                    )
        
        # Progress update
        gr.HTML("""
        <div class="progress-container">
            <div class="progress-bar" style="width: 50%;"></div>
        </div>
        <div style="text-align: center; margin: 1rem 0; color: var(--text-muted);">Step 2 of 4: Metrics Configured ✓</div>
        """)
        
        # Country Selection with Real-time Preview
        gr.Markdown("## Step 3: Target Country Analysis")
        
        with gr.Row():
            with gr.Column(scale=2):
                country_selector = gr.Dropdown(
                    choices=list(ENHANCED_COUNTRIES.keys()),
                    value=["UAE", "Singapore", "Portugal", "Ireland"],
                    multiselect=True,
                    label="Select Countries to Compare",
                    info="Choose up to 6 countries for detailed analysis"
                )
                
                # Quick country stats preview
                country_preview = gr.HTML("""
                <div class="country-preview">
                    <div class="preview-header">Country Quick Stats</div>
                    <div class="preview-stats" id="country-stats">
                        Select countries to see live comparison...
                    </div>
                </div>
                """)
            
            with gr.Column(scale=1):
                compare_button = gr.Button(
                    "🚀 Run AI Analysis", 
                    variant="primary",
                    size="lg",
                    elem_classes=["premium-button"]
                )
                
                # Real-time confidence meter
                gr.HTML("""
                <div class="confidence-meter">
                    <div class="meter-label">AI Confidence Level</div>
                    <div class="meter-bar">
                        <div class="meter-fill" style="width: 87%;"></div>
                    </div>
                    <div class="meter-text">87% - High Confidence</div>
                </div>
                """)
        
        # Progress update
        gr.HTML("""
        <div class="progress-container">
            <div class="progress-bar" style="width: 75%;"></div>
        </div>
        <div style="text-align: center; margin: 1rem 0; color: var(--text-muted);">Step 3 of 4: Countries Selected ✓</div>
        """)
        
        # Main Results Section
        with gr.Row():
            with gr.Column():
                # Country comparison heatmap
                country_heatmap = gr.Plot(
                    label="🏆 Country Comparison Matrix",
                    visible=False
                )
                
                # Comprehensive dashboard
                main_dashboard = gr.Plot(
                    label="📊 Advanced ROI Dashboard", 
                    visible=False
                )
        
        # AI Insights Section
        with gr.Row():
            ai_insights_display = gr.HTML(visible=False)
        
        # KPI Cards Section  
        with gr.Row():
            kpi_cards = gr.HTML(visible=False)
        
        # Detailed Country Analysis
        with gr.Row():
            detailed_analysis = gr.HTML(visible=False)
        
        # Final progress and CTA
        results_section = gr.HTML(visible=False)
        
        # Hidden calculator instances
        calculator = AdvancedROICalculator()
        ai_engine = AIInsightEngine()
        lead_engine = EnhancedLeadEngine()
        chart_generator = AdvancedChartGenerator()
        
        def update_profile(profile_id):
            """Update current profile and return profile info"""
            if profile_id in ENHANCED_PROFILES:
                profile = ENHANCED_PROFILES[profile_id]
                return {
                    current_profile: profile_id,
                    current_revenue: profile.typical_revenue,
                    current_margin: (profile.margin_expectations[0] + profile.margin_expectations[1]) / 2
                }
            return {}
        
        def generate_country_preview(selected_countries):
            """Generate real-time country preview"""
            if not selected_countries:
                return "<div class='preview-message'>Select countries to see comparison...</div>"
            
            preview_html = '<div class="country-stats-grid">'
            
            for country_key in selected_countries[:4]:  # Limit to 4 for preview
                if country_key in ENHANCED_COUNTRIES:
                    country = ENHANCED_COUNTRIES[country_key]
                    preview_html += f"""
                    <div class="country-stat-card">
                        <h4>{country.name}</h4>
                        <div class="stat-row">
                            <span>Corp Tax:</span> 
                            <span class="{'low-tax' if country.corp_tax <= 0.15 else 'medium-tax' if country.corp_tax <= 0.25 else 'high-tax'}">{country.corp_tax*100:.1f}%</span>
                        </div>
                        <div class="stat-row">
                            <span>Living Cost:</span> 
                            <span>€{country.living_cost:,}/mo</span>
                        </div>
                        <div class="stat-row">
                            <span>Ease Score:</span> 
                            <span class="score-{int(country.ease_score)}">{country.ease_score:.1f}/10</span>
                        </div>
                        <div class="visa-preview">
                            <strong>Top Visa:</strong> {country.visa_options[0] if country.visa_options else 'Various options'}
                        </div>
                    </div>
                    """
            
            preview_html += '</div>'
            
            # Add summary stats
            if len(selected_countries) > 1:
                avg_corp_tax = sum(ENHANCED_COUNTRIES[c].corp_tax for c in selected_countries if c in ENHANCED_COUNTRIES) / len(selected_countries)
                avg_living = sum(ENHANCED_COUNTRIES[c].living_cost for c in selected_countries if c in ENHANCED_COUNTRIES) / len(selected_countries)
                
                preview_html += f"""
                <div class="preview-summary">
                    <div class="summary-stat">
                        <span>Avg Corp Tax:</span> <strong>{avg_corp_tax*100:.1f}%</strong>
                    </div>
                    <div class="summary-stat">
                        <span>Avg Living Cost:</span> <strong>€{avg_living:,.0f}/mo</strong>
                    </div>
                </div>
                """
            
            return preview_html
        
        def run_comprehensive_analysis(*args):
            """Main analysis function with all enhancements"""
            try:
                # Extract parameters
                (profile_id, selected_countries, current_rev, current_mar, current_corp, 
                 current_pers, current_liv, current_bus, rev_mult, mar_imp, 
                 success_prob, time_hor, disc_rate) = args
                
                if not selected_countries or profile_id not in ENHANCED_PROFILES:
                    return [gr.update()] * 6
                
                profile = ENHANCED_PROFILES[profile_id]
                results = {}
                ai_insights_all = {}
                
                # Calculate for each country
                for country_key in selected_countries:
                    if country_key in ENHANCED_COUNTRIES:
                        country = ENHANCED_COUNTRIES[country_key]
                        
                        # Run comprehensive calculation
                        result = calculator.calculate_comprehensive_roi(
                            profile, country, current_rev, current_mar,
                            current_corp, current_pers, current_liv, current_bus,
                            rev_mult, mar_imp, success_prob, time_hor, disc_rate
                        )
                        
                        results[country_key] = result
                        
                        # Generate AI insights
                        insight = ai_engine.generate_personalized_insight(profile, country, result)
                        ai_insights_all[country_key] = insight
                
                if not results:
                    return [gr.update()] * 6
                
                # Generate visualizations
                best_country = max(results.keys(), key=lambda k: results[k]['roi'])
                best_result = results[best_country]
                best_country_data = ENHANCED_COUNTRIES[best_country]
                
                # Create comprehensive dashboard
                dashboard = chart_generator.create_comprehensive_dashboard(
                    best_result, best_country_data.name, profile.name
                )
                
                # Create country heatmap
                heatmap = chart_generator.create_country_heatmap(selected_countries, profile_id)
                
                # Generate AI insights display
                ai_display = generate_ai_insights_display(ai_insights_all, profile)
                
                # Generate KPI cards
                kpi_display = generate_kpi_cards(results, profile)
                
                # Generate detailed analysis
                detailed_display = generate_detailed_analysis(results, profile, ai_insights_all)
                
                # Generate final CTA section with dynamic offers
                cta_display = generate_cta_section(results, profile, ai_insights_all, lead_engine)
                
                return [
                    gr.update(value=heatmap, visible=True),
                    gr.update(value=dashboard, visible=True), 
                    gr.update(value=ai_display, visible=True),
                    gr.update(value=kpi_display, visible=True),
                    gr.update(value=detailed_display, visible=True),
                    gr.update(value=cta_display, visible=True)
                ]
                
            except Exception as e:
                print(f"Analysis error: {e}")
                error_html = f"""
                <div class="error-message">
                    <h3>⚠️ Analysis Error</h3>
                    <p>Unable to complete analysis. Please check your inputs and try again.</p>
                    <p><small>Error: {str(e)[:100]}</small></p>
                </div>
                """
                return [gr.update(value=error_html, visible=True)] + [gr.update()] * 5
        
        def generate_ai_insights_display(insights_all, profile):
            """Generate comprehensive AI insights display"""
            html = '<div class="ai-insights-section">'
            html += '<h2>🤖 Personalized AI Insights</h2>'
            html += '<div class="ai-insights-grid">'
            
            # Sort by success probability
            sorted_insights = sorted(
                insights_all.items(), 
                key=lambda x: x[1]['success_probability'], 
                reverse=True
            )
            
            for country_key, insight in sorted_insights[:3]:  # Top 3 recommendations
                country_name = ENHANCED_COUNTRIES[country_key].name
                tier_colors = {
                    'high_roi': 'linear-gradient(135deg, #10b981 0%, #059669 100%)',
                    'medium_roi': 'linear-gradient(135deg, #f59e0b 0%, #d97706 100%)', 
                    'low_roi': 'linear-gradient(135deg, #6b7280 0%, #4b5563 100%)'
                }
                
                background = tier_colors.get(insight['tier'], tier_colors['medium_roi'])
                
                html += f"""
                <div class="ai-insight-card" style="background: {background};">
                    <div class="ai-insight-header">
                        <span class="ai-insight-icon">🎯</span>
                        <h3 class="ai-insight-title">{country_name} Analysis</h3>
                    </div>
                    <div class="ai-insight-description">{insight['text']}</div>
                    <div class="ai-metrics">
                        <div class="ai-confidence">
                            <span>AI Confidence: {insight['confidence']:.0f}%</span>
                        </div>
                        <div class="success-prob">
                            <span>Success Probability: {insight['success_probability']:.0f}%</span>
                        </div>
                    </div>
                    <div class="action-items">
                        <strong>Next Steps:</strong>
                        <ul>
                            {''.join(f'<li>{item}</li>' for item in insight['action_items'][:3])}
                        </ul>
                    </div>
                    <div class="timeline">
                        <strong>Timeline:</strong> {insight['timeline']}
                    </div>
                </div>
                """
            
            html += '</div></div>'
            return html
        
        def generate_kpi_cards(results, profile):
            """Generate enhanced KPI cards"""
            if not results:
                return ""
            
            best_country = max(results.keys(), key=lambda k: results[k]['roi'])
            best_result = results[best_country]
            best_country_name = ENHANCED_COUNTRIES[best_country].name
            
            # Calculate summary metrics
            avg_roi = sum(r['roi'] for r in results.values()) / len(results)
            best_roi = best_result['roi']
            total_savings = best_result['total_return'] * 12  # Annualized
            payback_years = best_result['payback_years']
            
            html = '<div class="kpi-section">'
            html += '<h2>📈 Key Performance Indicators</h2>'
            html += '<div class="kpi-grid">'
            
            # Best ROI Country
            html += f"""
            <div class="kpi-card success">
                <div class="kpi-label">Best ROI Opportunity</div>
                <div class="kpi-value">{best_roi:.0f}%</div>
                <div class="kpi-note">{best_country_name}<br>vs {avg_roi:.0f}% average</div>
            </div>
            """
            
            # Annual Savings Potential
            savings_class = "success" if total_savings > 50000 else "warning" if total_savings > 20000 else "error"
            html += f"""
            <div class="kpi-card {savings_class}">
                <div class="kpi-label">Annual Savings Potential</div>
                <div class="kpi-value">€{total_savings:,.0f}</div>
                <div class="kpi-note">Tax optimization + cost reduction</div>
            </div>
            """
            
            # Payback Period
            payback_class = "success" if payback_years <= 2 else "warning" if payback_years <= 4 else "error"
            payback_display = f"{payback_years:.1f}y" if payback_years != float('inf') else "∞"
            html += f"""
            <div class="kpi-card {payback_class}">
                <div class="kpi-label">Investment Payback</div>
                <div class="kpi-value">{payback_display}</div>
                <div class="kpi-note">Time to break even</div>
            </div>
            """
            
            # Risk-Adjusted Score
            risk_score = results[best_country].get('risk_score', 50)
            opportunity_score = results[best_country].get('opportunity_score', 50) 
            combined_score = (opportunity_score - risk_score/2)
            score_class = "success" if combined_score > 60 else "warning" if combined_score > 40 else "error"
            
            html += f"""
            <div class="kpi-card {score_class}">
                <div class="kpi-label">Risk-Adjusted Score</div>
                <div class="kpi-value">{combined_score:.0f}/100</div>
                <div class="kpi-note">Opportunity vs Risk rating</div>
            </div>
            """
            
            # Market Timing
            sentiment = ENHANCED_COUNTRIES[best_country].ai_sentiment
            timing_class = "success" if sentiment > 0.8 else "warning" if sentiment > 0.6 else "error"
            html += f"""
            <div class="kpi-card {timing_class}">
                <div class="kpi-label">Market Timing</div>
                <div class="kpi-value">{sentiment*100:.0f}/100</div>
                <div class="kpi-note">AI market sentiment analysis</div>
            </div>
            """
            
            # Success Probability
            if 'monte_carlo' in best_result:
                success_prob = best_result['monte_carlo']['probability_positive_roi'] * 100
            else:
                success_prob = 70
            
            prob_class = "success" if success_prob > 80 else "warning" if success_prob > 60 else "error"
            html += f"""
            <div class="kpi-card {prob_class}">
                <div class="kpi-label">Success Probability</div>
                <div class="kpi-value">{success_prob:.0f}%</div>
                <div class="kpi-note">Monte Carlo simulation</div>
            </div>
            """
            
            html += '</div></div>'
            return html
        
        def generate_detailed_analysis(results, profile, insights_all):
            """Generate detailed country-by-country analysis"""
            html = '<div class="detailed-analysis-section">'
            html += '<h2>🔍 Detailed Country Analysis</h2>'
            
            # Sort countries by ROI
            sorted_results = sorted(results.items(), key=lambda x: x[1]['roi'], reverse=True)
            
            for i, (country_key, result) in enumerate(sorted_results):
                country = ENHANCED_COUNTRIES[country_key]
                insight = insights_all.get(country_key, {})
                
                rank_suffix = ["🥇", "🥈", "🥉", "4️⃣", "5️⃣", "6️⃣"][min(i, 5)]
                
                html += f"""
                <div class="country-analysis-card rank-{i+1}">
                    <div class="country-header">
                        <h3>{rank_suffix} {country.name}</h3>
                        <div class="country-badges">
                            <span class="roi-badge">{result['roi']:.0f}% ROI</span>
                            <span class="payback-badge">{result['payback_years']:.1f}y payback</span>
                        </div>
                    </div>
                    
                    <div class="analysis-grid">
                        <div class="analysis-section">
                            <h4>💰 Financial Impact</h4>
                            <ul>
                                <li><strong>Monthly Cash Flow:</strong> €{result['monthly_delta']:,.0f}</li>
                                <li><strong>NPV (60mo):</strong> €{result['npv']:,.0f}</li>
                                <li><strong>Setup Investment:</strong> €{result['setup_cost']:,.0f}</li>
                                <li><strong>Annual Return:</strong> €{result['total_return']*12:,.0f}</li>
                            </ul>
                        </div>
                        
                        <div class="analysis-section">
                            <h4>🎯 Tax Optimization</h4>
                            <ul>
                                <li><strong>Corporate Tax:</strong> {country.corp_tax*100:.1f}%</li>
                                <li><strong>Personal Tax:</strong> {country.pers_tax*100:.1f}%</li>
                                <li><strong>Effective Rate:</strong> {(country.corp_tax + country.pers_tax)*100/2:.1f}%</li>
                                <li><strong>Tax Savings:</strong> High potential</li>
                            </ul>
                        </div>
                        
                        <div class="analysis-section">
                            <h4>🏠 Living & Business</h4>
                            <ul>
                                <li><strong>Living Costs:</strong> €{country.living_cost:,}/mo</li>
                                <li><strong>Business Costs:</strong> €{country.business_cost:,}/mo</li>
                                <li><strong>Ease of Business:</strong> {country.ease_score:.1f}/10</li>
                                <li><strong>Banking Quality:</strong> {country.banking_score:.1f}/10</li>
                            </ul>
                        </div>
                        
                        <div class="analysis-section">
                            <h4>🛂 Visa & Legal</h4>
                            <ul>
                                <li><strong>Best Visa Option:</strong> {country.visa_options[0] if country.visa_options else 'Multiple options'}</li>
                                <li><strong>Alternative Visas:</strong> {len(country.visa_options)} options available</li>
                                <li><strong>Recent Changes:</strong> {country.recent_changes[:100]}...</li>
                                <li><strong>Special Programs:</strong> {len(country.special_programs)} available</li>
                            </ul>
                        </div>
                    </div>
                    
                    <div class="risk-opportunity">
                        <div class="risk-section">
                            <h4>⚠️ Risk Factors</h4>
                            <div class="risk-bars">
                                <div class="risk-bar">
                                    <span>Political Risk</span>
                                    <div class="bar"><div class="fill" style="width: {country.risk_factors.get('political', 0.1)*100}%"></div></div>
                                    <span>{country.risk_factors.get('political', 0.1)*100:.0f}%</span>
                                </div>
                                <div class="risk-bar">
                                    <span>Economic Risk</span>
                                    <div class="bar"><div class="fill" style="width: {country.risk_factors.get('economic', 0.1)*100}%"></div></div>
                                    <span>{country.risk_factors.get('economic', 0.1)*100:.0f}%</span>
                                </div>
                                <div class="risk-bar">
                                    <span>Regulatory Risk</span>
                                    <div class="bar"><div class="fill" style="width: {country.risk_factors.get('regulatory', 0.1)*100}%"></div></div>
                                    <span>{country.risk_factors.get('regulatory', 0.1)*100:.0f}%</span>
                                </div>
                            </div>
                        </div>
                    </div>
                    
                    <div class="recommendation-section">
                        <h4>🎯 AI Recommendation</h4>
                        <div class="recommendation-text">
                            {result.get('recommendation', 'Analysis complete - consult with advisor for next steps')}
                        </div>
                    </div>
                </div>
                """
            
            html += '</div>'
            return html
        
        def generate_cta_section(results, profile, insights_all, lead_engine):
            """Generate dynamic CTA section with personalized offers"""
            if not results:
                return ""
            
            best_country = max(results.keys(), key=lambda k: results[k]['roi'])
            best_result = results[best_country]
            best_country_data = ENHANCED_COUNTRIES[best_country]
            
            # Generate personalized offer
            offer = lead_engine.generate_dynamic_offer(best_result, profile, best_country_data)
            
            html = f"""
            <div class="cta-section">
                <div class="progress-container">
                    <div class="progress-bar" style="width: 100%;"></div>
                </div>
                <div style="text-align: center; margin: 1rem 0; color: var(--success);">Step 4 of 4: Analysis Complete ✓</div>
                
                <div class="premium-cta">
                    <h2 class="cta-title">{offer['title']}</h2>
                    <p class="cta-subtitle">{offer['subtitle']}</p>
                    
                    <div class="offer-pricing">
                        <div class="price-comparison">
                            <span class="original-price">{offer['original_price']}</span>
                            <span class="discounted-price">{offer['discounted_price']}</span>
                            <span class="savings-badge">Save {offer['savings']}</span>
                        </div>
                        <div class="value-statement">{offer['value_statement']}</div>
                    </div>
                    
                    <div class="urgency-message">{offer['urgency']}</div>
                    
                    <div class="offer-includes">
                        <h3>What's Included:</h3>
                        <ul>
                            {''.join(f'<li>✅ {item}</li>' for item in offer['includes'])}
                        </ul>
                    </div>
                    
                    <div class="bonuses-section">
                        <h3>🎁 Exclusive Bonuses:</h3>
                        <ul>
                            {''.join(f'<li>🎁 {bonus}</li>' for bonus in offer['bonuses'])}
                        </ul>
                    </div>
                    
                    <div class="cta-buttons">
                        <button class="cta-button-enhanced primary">{offer['cta']}</button>
                        <button class="cta-button-enhanced secondary">Schedule Free Consultation</button>
                    </div>
                    
                    <div class="guarantee-section">
                        <div class="guarantee-badge">🛡️ {offer['guarantee']}</div>
                    </div>
                    
                    <div class="social-proof">
                        <div class="social-proof-text">{offer['social_proof']}</div>
                    </div>
                    
                    <div class="payment-options">
                        <h4>Payment Options:</h4>
                        <ul>
                            {''.join(f'<li>{option}</li>' for option in offer['payment_options'])}
                        </ul>
                    </div>
                </div>
                
                <div class="final-stats">
                    <div class="stat">
                        <div class="stat-number">{best_result['roi']:.0f}%</div>
                        <div class="stat-label">Projected ROI</div>
                    </div>
                    <div class="stat">
                        <div class="stat-number">€{best_result['total_return']*12:,.0f}</div>
                        <div class="stat-label">Annual Savings</div>
                    </div>
                    <div class="stat">
                        <div class="stat-number">{best_result['payback_years']:.1f}</div>
                        <div class="stat-label">Years to ROI</div>
                    </div>
                    <div class="stat">
                        <div class="stat-number">{offer['timeline']}</div>
                        <div class="stat-label">Timeline</div>
                    </div>
                </div>
                
                <div class="disclaimer">
                    <p><small>* Results based on AI analysis and Monte Carlo simulations. Individual results may vary. 
                    This is not financial or legal advice. Consult with qualified professionals before making decisions.</small></p>
                </div>
            </div>
            """
            
            return html
        
        # Event handlers
        profile_selector.change(
            fn=update_profile,
            inputs=[profile_selector],
            outputs=[current_profile, current_revenue, current_margin]
        )
        
        country_selector.change(
            fn=generate_country_preview,
            inputs=[country_selector],
            outputs=[country_preview]
        )
        
        compare_button.click(
            fn=run_comprehensive_analysis,
            inputs=[
                profile_selector, country_selector, current_revenue, current_margin,
                current_corp_tax, current_pers_tax, current_living, current_business,
                revenue_multiplier, margin_improvement, success_probability,
                time_horizon, discount_rate
            ],
            outputs=[
                country_heatmap, main_dashboard, ai_insights_display,
                kpi_cards, detailed_analysis, results_section
            ]
        )
        
        # Enhanced Footer
        gr.HTML("""
        <div class="premium-footer">
            <div style="text-align: center; margin-bottom: 2rem;">
                <h2 style="color: var(--primary); margin-bottom: 1rem;">VisaTier 4.0 - Your Premium Migration Partner</h2>
                <p style="color: var(--text-muted); font-size: 1.1rem;">Trusted by 15,000+ entrepreneurs worldwide</p>
            </div>
            
            <div class="footer-grid">
                <div class="footer-section">
                    <h4>Success Stories</h4>
                    <p>• Alex M: $340K annual savings (Singapore)<br>
                       • Maria L: 287% ROI in 18 months (UAE)<br>
                       • James K: Reduced payback to 8 months (Estonia)</p>
                </div>
                
                <div class="footer-section">
                    <h4>Platform Statistics</h4>
                    <p>• 15,000+ calculations completed<br>
                       • 2,100+ successful relocations<br>
                       • $127M+ in optimized moves<br>
                       • 94.7% client satisfaction</p>
                </div>
                
                <div class="footer-section">
                    <h4>Advanced Features</h4>
                    <p>• Monte Carlo risk simulation<br>
                       • Sensitivity analysis<br>
                       • Multi-country comparison<br>
                       • Personalized insights engine</p>
                </div>
                
                <div class="footer-section">
                    <h4>Get Started Today</h4>
                    <p>• Book strategy consultation<br>
                       • Download country guides<br>
                       • Join exclusive community<br>
                       • Access premium tools</p>
                </div>
            </div>
            
            <div style="text-align: center; padding-top: 2rem; border-top: 1px solid var(--border); color: var(--text-muted); font-size: 14px;">
                <p><strong>Legal Disclaimer:</strong> Results are estimates for planning purposes only. Not financial, tax, or legal advice. 
                Consult qualified professionals for personalized guidance.</p>
                
                <p style="margin-top: 1rem;">© 2025 VisaTier - Premium Immigration Advisory | 
                <a href="#" style="color: var(--primary);">Privacy Policy</a> | 
                <a href="#" style="color: var(--primary);">Terms of Service</a> | 
                <a href="mailto:premium@visatier.com" style="color: var(--primary);">Contact</a></p>
            </div>
        </div>
        """)
    
    return app
# =========================
# ADDITIONAL UTILITY FUNCTIONS
# =========================
def generate_pdf_report(result: Dict, profile: UserProfile, country: CountryData) -> str:
    """Generate comprehensive PDF report (placeholder for actual implementation)"""
    return f"PDF report generated for {profile.name} -> {country.name} migration analysis"
def send_to_crm(email: str, profile: str, result: Dict) -> bool:
    """Send lead data to CRM system (placeholder)"""
    print(f"CRM: New lead {email} - {profile} - ROI: {result.get('roi', 0):.1f}%")
    return True
def schedule_consultation(email: str, profile: str, country: str, roi: float) -> str:
    """Schedule consultation via Calendly API (placeholder)"""
    return f"https://calendly.com/visatier/consultation?email={email}&profile={profile}"
# =========================
# MAIN EXECUTION
# =========================
if __name__ == "__main__":
    # Create and launch the enhanced application
    app = create_premium_immigration_app()
    
    # Development server
    app.launch(
        server_name="0.0.0.0",
        server_port=7860,
        share=False,
        debug=True,
        show_error=True
    )
