# Probabilistic Football Modeling Pipeline (Liga MX)

This project focuses on building a **robust, interpretable, and football-aware data pipeline** for probabilistic modeling using Liga MX match data.

Rather than predicting exact scores or deterministic outcomes, the goal is to design a **clean and reusable pre-match dataset** that supports **probability estimation, calibration analysis, and decision-making under uncertainty**.

---

## 🎯 Project Goals

- Build a structured and reproducible **pre-match data pipeline**
- Design **football-informed features** (form, momentum, relative strength)
- Ensure **data consistency, interpretability, and temporal correctness**
- Produce datasets suitable for **probabilistic models**, not just point predictions
- Treat models as **downstream consumers** of the data pipeline

---

## ⚙️ Scope & Data

- Competition: Liga MX  
- Granularity: One record per match (home vs away)  
- Temporal structure: Rolling pre-match windows  
- Feature computation strictly respects **pre-match availability**

While some exploratory steps focus on controlled seasonal subsets, the pipeline and evaluation strategy are designed to support **multi-season, temporally consistent modeling**.

---

## 🧠 Feature Engineering (Pre-Match)

Each match is represented using separate features for home and away teams:

- `home_form`, `away_form`
- `home_momentum`, `away_momentum`

Relative features are also included:

- `form_diff`
- `momentum_diff`

**Form** captures recent performance level, while  
**Momentum** captures the direction and trend of that performance.

All features are computed using **only information available before kickoff**, preventing leakage.

---

## 🎯 Target Definition

Current target:

- `home_win = 1` → home team wins  
- `home_win = 0` → draw or away win  

This binary setup is intentionally simple and extensible to:

- multi-class outcomes (W / D / L)
- goal-based probabilistic models
- Bayesian or hierarchical approaches

---

## 📊 Modeling Philosophy

Football is a **high-variance, low-signal sport**.

Predicting exact outcomes is neither realistic nor informative.

This project prioritizes:

- probability estimation
- calibration and reliability
- ranking-based and zone-based interpretation

Accuracy alone is not treated as a sufficient metric.

---

## 🔬 Validation & Evaluation

Model outputs are evaluated using:

- temporal cross-validation (expanding window)
- probabilistic metrics (log loss, Brier score)
- reliability curves and probability buckets

The full evaluation process and technical reasoning are documented in the **notebooks folder**, which serves as a traceable record of modeling decisions.

---

## 🚧 Project Status

Work in progress.

Current focus areas:

- feature robustness and signal validation
- probabilistic calibration analysis
- identification of reliable vs unreliable prediction zones

---

## 🔜 Next Steps

- Targeted feature engineering to improve mid-probability regions
- Model comparison under a fixed evaluation protocol
- Extension toward richer probabilistic outputs

