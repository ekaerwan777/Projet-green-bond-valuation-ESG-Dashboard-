# 🌱 Green Bond Valuation & ESG Dashboard — Hackathon Project

> School hackathon project — ESG Finance & Data Analytics  
> Tools: Python · Streamlit · Plotly · Pandas

---

## 📌 Overview

This project was built during a school hackathon. It combines two complementary deliverables around **sustainable finance and ESG monitoring**:

1. **Green Bond Valuation** — a quantitative pricing model applied to the EDF Green Bond (ISIN: FR001400ZGF2)
2. **Interactive ESG Dashboard** — a Streamlit app tracking key climate, social and governance indicators

---

## 1️⃣ Green Bond Valuation (Notebook)

### Context
Green bonds are fixed-income instruments whose proceeds are exclusively used to finance environmentally sustainable projects. Pricing them accurately requires accounting for both standard fixed-income mechanics and the **greenium** — the yield premium investors accept in exchange for the bond's ESG label.

### Methods implemented

| # | Method | Description |
|---|--------|-------------|
| 1 | **YTM Pricing** | Discounts all cashflows using a single flat yield-to-maturity |
| 2 | **Spot Curve Pricing** | Discounts each cashflow at its corresponding zero-coupon rate |
| 3 | **Credit Spread Pricing** | Adds a credit spread (90 bps) on top of the risk-free rate |
| 4 | **Greenium Pricing** | Reduces the credit spread by 15 bps to reflect ESG premium |

### Results (EDF Green Bond — 3.25% coupon, 6-year maturity)

| Method | Price |
|--------|-------|
| YTM (3.3%) | 997.32 |
| Spot curve | 1000.94 |
| Credit spread (90 bps) | 970.98 |
| Greenium adjusted (−15 bps) | 978.79 |

### Key insight
The greenium reduces the effective discount rate, which mechanically increases the bond price. This reflects the market reality where ESG-labeled bonds trade at a slight premium relative to conventional equivalents from the same issuer.

---

## 2️⃣ Interactive ESG Dashboard (Streamlit App)

### Sections

| Section | Description |
|---------|-------------|
| 🌡️ **Global Temperature** | Time series of global average temperature anomalies |
| 🌊 **Sea Level** | Satellite-measured ocean level evolution + avg annual rise (mm/yr) |
| 🏭 **CO₂ by Country** | Bar chart of top emitting countries |
| 🏢 **CO₂ by Company** | Slider-filtered ranking of most polluting companies by year |
| ⚖️ **Gender Pay Equity** | Eurostat-sourced labor market indicators by country |

### Running the dashboard

```bash
pip install streamlit plotly pandas
streamlit run Dashboard_esg.py
```

> Make sure the following CSV files are in the same directory:
> `Temperature.csv`, `Sea_level.csv`, `co2_countries.csv`, `co2_companies.csv`, `gender.csv`

---

## 🛠️ Stack

- **Python 3.12**
- **Streamlit** — interactive web app
- **Plotly Express** — dynamic charts
- **Pandas** — data wrangling
- **math / dataclasses** — bond pricing engine

---

## 📁 Repository Structure

```
├── hackathon_2.ipynb       # Green Bond pricing notebook
├── Dashboard_esg.py        # Streamlit ESG dashboard
├── Temperature.csv
├── Sea_level.csv
├── co2_countries.csv
├── co2_companies.csv
├── gender.csv
└── README.md
```

---
