# 📒 Notebooks – Probabilistic Modeling (Liga MX)

This folder contains the **core analytical notebooks** used throughout the development of the Liga MX probabilistic modeling project.

The notebooks are intentionally structured to reflect the **conceptual evolution of the project**, from baseline modeling to temporal validation and probabilistic evaluation.  
They are not isolated experiments, but part of a coherent modeling narrative.

---

## 🧭 Notebook Overview

### 01_baseline_logistic_regression.ipynb  
**Probabilistic Baseline – Calibrated Logistic Regression**

This notebook establishes the **baseline probabilistic model** for the project.

**Purpose:**
- Define a strong, interpretable probabilistic reference
- Focus on probability quality rather than raw accuracy
- Serve as a benchmark for all subsequent models

**Key aspects:**
- Logistic Regression with pre-match features
- Probability calibration (Platt / isotonic when applicable)
- Reliability curves and sanity checks
- Interpretation aligned with football logic

This baseline is treated as a **non-negotiable reference point** for evaluation.

---

### 02_exploration_tree.ipynb  
**Decision Trees – Exploratory Modeling**

This notebook explores **tree-based models** to evaluate:

- Non-linear decision boundaries
- Feature interaction effects
- Interpretability trade-offs vs probabilistic stability

**Focus:**
- Exploratory analysis
- Understanding model behavior
- Not intended as a final production model

---

### 03_exploratory_model_SVM.ipynb  
**Support Vector Machines – Exploratory Analysis**

This notebook evaluates SVMs as an alternative modeling approach.

**Focus:**
- Margin-based classification
- Stability across probability regions
- Sensitivity to feature scaling and class separation

The goal is **conceptual comparison**, not optimization.

---

### 04_expanding_window.ipynb  
**Temporal Cross-Validation – Expanding Window**

This notebook implements the **core validation strategy** of the project.

**Why this matters:**
Football data is temporal.  
Random splits introduce leakage and unrealistic performance estimates.

**Implemented approach:**
- Expanding window cross-validation
- Train on past matches → validate on future matches
- Season-aware evaluation

This notebook defines the **evaluation backbone** used by the project.

---

### 05_evaluation_model.ipynb  
**Probabilistic Evaluation & Reliability Analysis**

This notebook focuses exclusively on **probability quality evaluation**.

**Key analyses:**
- Probability bins (bucket-based evaluation)
- Empirical win rate vs predicted probability
- Brier score and log loss by probability zone
- Identification of reliable vs unreliable regions

This notebook is intentionally analytical and reflective, serving as a **learning and validation artifact**.

---

## 📊 Modeling Philosophy (Notebook-Level)

Across all notebooks, the project follows these principles:

- Football is a **high-variance system**
- Exact result prediction is not the objective
- Well-calibrated probabilities are more valuable than accuracy
- Evaluation must be temporal, interpretable, and football-aware

Models are treated as **consumers of a robust data pipeline**, not the center of the system.

---

## 🚧 Notes on Structure

Some notebooks are exploratory by design.  
Others are closer to final, portfolio-ready artifacts.

This separation is intentional and reflects:
- Learning progression
- Hypothesis testing
- Professional modeling workflow

---

## 🔜 Next Steps

- Feature robustness and optimization
- Zone-based probability refinement
- Model comparison under calibrated settings
- Extension to multi-output probabilistic modeling

---

*This folder documents not only results, but the reasoning behind them.*
