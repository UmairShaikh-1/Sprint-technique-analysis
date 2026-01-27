# Sprint-technique-analysis
This project explores how different variables in the starting‑block influence a sprinter’s time to 30 meters, using a synthetic dataset modeled on realistic ranges for elite and average athletes. 
The goal is to identify how variables such as block angles, knee angles, reaction time, and RFmax contribute to early‑acceleration performance.

## Project Overview
* Synthetic dataset of 500 sprinters (250 elite, 250 average)
* Biomechanical variables: block angles, knee angles, TBCG, RFmax, reaction time
* Performance metrics: 10m, 20m, and 30m sprint times
* Regression modeling to identify which factors most strongly influence 30m time
* Coefficient analysis to interpret direction and magnitude of relationships

## Methodology
1. Data Generation
A synthetic dataset was created based on realistic facts and figures for elite and average sprinters. 

2. Preprocessing
* One‑hot encoding for skill level
* Feature scaling using StandardScaler
* Train/test split for modeling

3. Modeling
A Linear Regression model was used to identify the impact of each variable.

4. Coefficient Analysis
Model coefficients were extracted and visualized to interpret:
* Positive vs negative relationships
* Relative strength of each variable

## Key Insights
* RFmax and block angles show strong negative relationships with 30m time.
* Having improper Knee angles and TBCG increase the timme to 30m.
* There are a multitude of different factors that contribute to 30m time.

## Running the code:

Clone this repository: git clone synthetic_sprint_data_comparison.csv

Install the required libraries: pip install numpy pandas matplotlib sklearn os

Run the Jupyter Notebook or Python script: python sprinteracceleration.py
