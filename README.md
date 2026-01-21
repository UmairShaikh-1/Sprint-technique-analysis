# Sprint-technique-analysis
This project explores how starting‑block biomechanics influence a sprinter’s time to 30 meters, using a synthetic dataset modeled on realistic ranges for elite and average athletes. 
The goal is to quantify how variables such as block angles, knee angles, reaction time, and RFmax contribute to early‑acceleration performance.

## Project Overview
* Synthetic dataset of 500 sprinters (250 elite, 250 average)
* Biomechanical variables: block angles, knee angles, TBCG, RFmax, reaction time
* Performance metrics: 10m, 20m, and 30m sprint times
* Regression modeling to identify which factors most strongly influence 30m time
* Coefficient analysis to interpret direction and magnitude of relationships

## Methodology
1. Data Generation
A synthetic dataset was created using realistic ranges for elite and average sprinters. Performance times were modeled using weighted biomechanical factors plus noise.

2. Preprocessing
* One‑hot encoding for skill level
* Feature scaling using StandardScaler
* Train/test split for modeling

3. Modeling
A Linear Regression model was used to quantify how each biomechanical variable affects 30m sprint time.

4. Coefficient Analysis
* Model coefficients were extracted and visualized to interpret:
* Positive vs negative relationships
* Relative strength of each variable

## Key Insights
* RFmax and block angles show strong negative relationships with 30m time (better mechanics → faster acceleration).
* Knee angles and TBCG tend to increase 30m time when suboptimal.
* Sprint performance emerges from multiple interacting factors, not a single dominant variable.
