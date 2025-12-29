# Liga MX Data Pipeline & Feature Engineering

This project focuses on building a robust and scalable data processing pipeline for Liga MX match data using Python.

The main goal is not just model training, but the creation of a **clean, well-defined dataset and feature engineering system** that can later be consumed by predictive models.

## Project Objectives
- Extract and structure Liga MX match statistics
- Design and formalize football-related features (form, momentum, performance trends)
- Build a reusable data processing pipeline
- Prepare high-quality datasets for future machine learning models

## Current Focus
The project is currently centered on:
- Data ingestion and transformation
- Feature definition and validation
- Improving data consistency and football interpretability

Model development is treated as a downstream consumer of the data pipeline.

## Tech Stack
- Python
- Pandas / NumPy
- Custom data processing modules

## Project Status
🚧 Work in progress — actively expanding feature engineering and pipeline robustness.

## Motivation
This project is part of a long-term learning path focused on applied data science, machine learning, and real-world football analytics.

## Objective updates
Build a professional data pipeline for football, focused on the probabilistic estimation of results, rather than the deterministic prediction of scores.
The main focus is on:
  -pre-match feature engineering
  -design of reproducible datasets
  -football interpretability
  -scalability towards more advanced probabilistic models

Football is a sport with a high element of chance, so predicting exact results is neither a realistic nor a professional goal. Instead, this project takes an approach of:
  ~Probabilistic modeling, estimating the probability of events (e.g., home team win) given pre-match conditions.

## Current scope of the project
~Competition: Liga MX
~Season used: Clausura 2024
~Time frame: last 5 matches
~Granularity: one record per match (home vs away)
Using a single season avoids introducing structural noise caused by significant changes between seasons (squads, coaches, context).
## Data Pipeline
1. Data ingestion and base structure
Each match is initially represented with two records:
one per team
including goals, home/away indicator, and match date

2. Pre-match feature engineering
~Points
Points obtained per match:
  Win = 3
  Draw = 1
  Loss = 0

~Form (Team Form)
Measures a team’s recent average performance.
Definition:
Form
  Form=3n1​∑pointslast n​
Window: last 5 matches
Range: [0, 1]
Interpretation:
high values → strong recent performance
low values → poor recent performance

~Momentum (Performance Trend)
Measures the direction of recent performance.
Definition:
Slope of a simple linear regression over points from the last 5 matches.
Interpretation:
Momentum > 0 → improving team
Momentum < 0 → declining team
This metric is intentionally more volatile than Form.

3. Pre-match dataset (home vs away)

Each row in the final dataset represents one match, with separate features for home and away teams:

  -home_form
  -away_form
  -home_momentum
  -away_momentum

Additionally, relative features are included:

  -form_diff
  -momentum_diff

4. Explicit home advantage feature

An explicit feature is added:

home_advantage = 1

This allows the model to learn a baseline home advantage offset, a standard practice in probabilistic football models.

## Target Definition

The project uses a binary probabilistic target.

Current target:
home_win = 1 → home team wins
home_win = 0 → draw or away win

This design is:

  -simple
  -robust
  -scalable to:
    W / D / L classification
  -goal-based (Poisson) models
  -Bayesian approaches

## Feature Validation (EDA)

Before modeling, features were validated through:

  -distribution analysis
  -range checks
  -football-based sanity checks

Results:
  -Form → stable and well-behaved
  -Momentum → informative but higher variance
  -Relative features centered around zero → no evident bias

## What This Project Does NOT Do (by design)

-Does not predict exact scorelines
-Does not use deep learning
-Does not prematurely optimize models
-Does not include post-match information in features

## Next Steps

- Train a baseline probabilistic model
- Evaluate probability calibration
- Extend to goal-based models
-Add advanced features (home/away splits, attack/defense)
