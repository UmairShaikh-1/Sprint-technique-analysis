#This analysis is focused on the factors of a sprinters block start that effect the 30m sprint
#The data contains the 30,20 and 10 meters of elite and average sprinters
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression,Ridge
import matplotlib.pyplot as plt
import os

#producing synthetic dataset based on real data
'''
# Set a seed for reproducibility
np.random.seed(42)

# Define the number of athletes for each group
num_elite = 250
num_average = 250
total_athletes = num_elite + num_average

# --- Generate Elite Sprinter Data ---
elite_data = {
    'skill_level': ['Elite'] * num_elite,
    'front_block_angle': np.random.uniform(40, 55, num_elite).round(1),
    'rear_block_angle': np.random.uniform(55, 65, num_elite).round(1),
    'front_knee_angle': np.random.uniform(90, 105, num_elite).round(1),
    'rear_knee_angle': np.random.uniform(120,140,num_elite).round(1),
    'TBCG': np.random.uniform(40,50,num_elite).round(1),
    'RFmax': np.random.uniform(0.55, 0.65, num_elite).round(2),
    'reaction_time': np.random.uniform(0.12, 0.18, num_elite).round(3)
}

# --- Generate Average Sprinter Data ---
average_data = {
    'skill_level': ['Average'] * num_average,
    'front_block_angle': np.random.uniform(55, 65, num_average).round(1),
    'rear_block_angle': np.random.uniform(60, 75, num_average).round(1),
    'front_knee_angle': np.random.uniform(100, 120, num_average).round(1),
    'rear_knee_angle': np.random.uniform(125,155,num_elite).round(1),
    'TBCG': np.random.uniform(50,60,num_average).round(1),
    'RFmax': np.random.uniform(0.40, 0.55, num_average).round(2),
    'reaction_time': np.random.uniform(0.18, 0.25, num_average).round(3)
}

# Combine the data into a single DataFrame
df_elite = pd.DataFrame(elite_data)
df_average = pd.DataFrame(average_data)
df = pd.concat([df_elite, df_average], ignore_index=True)

# Add an athlete ID
df['athlete_id'] = range(1, total_athletes + 1)

# --- Create Performance Metrics (Target Variables) ---
# A simplified model where better biomechanics and faster reaction time lead to faster times
df['is_elite']= (df['skill_level'] == 'Elite').astype(int)

df['time_to_30m_raw'] = (
    5.0  # Base time
    -1.0 * df['is_elite']
    - 0.006 * df['front_block_angle']
    - 0.006 * df['rear_block_angle']
    + 0.002 * df['front_knee_angle']
    + 0.002 * df['rear_knee_angle']
    + 0.007 * df['TBCG']
    - 0.3 * df['RFmax']
    - 1 * df['reaction_time']
)

# Add noise and ensure times are within a plausible range
df['time_to_30m'] = np.clip(df['time_to_30m_raw'],3.7,5.0).round(2)

# Create related metrics for 10m and 20m
df['time_to_10m'] = df['time_to_30m'] - np.random.uniform(2.0, 2.8, total_athletes)
df['time_to_20m'] = df['time_to_30m'] - np.random.uniform(0.8, 1.3, total_athletes)

# Ensure the times are logical and rounded
df['time_to_10m'] = np.clip(df['time_to_10m'], 1.5, 2.3).round(2)
df['time_to_20m'] = np.clip(df['time_to_20m'], 2.8, 3.8).round(2)

# Drop the raw calculation column
df.drop(columns=['time_to_30m_raw','is_elite'], inplace=True)

# Reorder columns for readability
cols = ['athlete_id', 'skill_level', 'reaction_time', 'front_block_angle', 'rear_block_angle', 'front_knee_angle','rear_knee_angle','TBCG', 'RFmax', 'time_to_10m', 'time_to_20m', 'time_to_30m']
df = df[cols]

# Display the first few rows
print(df.head())

# Save the dataset to a CSV file
df.to_csv('C:/Users/Umair/OneDrive - University of West London/Documents/Career/DL projects/synthetic_sprint_data_comparison.csv', index=False)
print("\nSynthetic data with Elite vs. Average comparison saved to 'synthetic_sprint_data_comparison.csv'")
'''

#fetching the dataset 
script_path = os.path.dirname(__file__)
file_path = os.path.join(script_path,'synthetic_sprint_data_comparison.csv')
df = pd.read_csv(file_path)

#converting string columns into computer readable format
dummies_df = pd.get_dummies(data=df['skill_level'], drop_first=True).astype(int)
training_df = df.drop(columns=['skill_level'])
training_df = pd.concat([training_df, dummies_df], axis=1)

#saparating target and features and removing unwanted columns
X = training_df.drop(columns=['athlete_id','time_to_10m','time_to_20m','time_to_30m','Elite'])
Y = training_df['time_to_30m'].to_frame()

#scatter plots can give a good idea about the positve or negative relation of the variables with the target.
#time to 30m is determined by many factors. This dataset focuses only on the starting block.
#since no single variable has a drastic impact on the time to 30m. Its difficult to identify the direction of each variable.
'''
fig, axes = plt.subplots(nrows=1,ncols=2,figsize=(20,20))
axes[0].scatter(X['front_knee_angle'],Y['time_to_30m'])
axes[0].set_title('front knee angle vs time to 30m')
axes[0].set_xlabel('front knee angle (degrees)')
axes[0].set_ylabel('time to 30m (s)')

axes[1].scatter(X['rear_knee_angle'],Y['time_to_30m'])
axes[1].set_title('rear knee angle vs time to 30m')
axes[1].set_xlabel('rear knee angle (degrees)')
axes[1].set_ylabel('time to 30m (s)')
plt.show()
'''

'''
fig, axes = plt.subplots(nrows=1,ncols=2,figsize=(20,20))
axes[0].scatter(X['front_block_angle'],Y['time_to_30m'])
axes[0].set_title('front block angle vs time to 30m')
axes[0].set_xlabel('front block angle (degrees)')
axes[0].set_ylabel('time to 30m (s)')

axes[1].scatter(X['rear_block_angle'],Y['time_to_30m'])
axes[1].set_title('rear block angle vs time to 30m')
axes[1].set_xlabel('rear block angle (degrees)')
axes[1].set_ylabel('time to 30m (s)')
plt.show()
'''

'''
fig, axes = plt.subplots(nrows=1,ncols=2,figsize=(20,20))
axes[0].scatter(X['TBCG'],Y['time_to_30m'])
axes[0].set_title('TBCG vs time to 30m')
axes[0].set_xlabel('TBCG (degrees)')
axes[0].set_ylabel('time to 30m (s)')

axes[1].scatter(X['RFmax'],Y['time_to_30m'])
axes[1].set_title('RFmax vs time to 30m')
axes[1].set_xlabel('RFmax (percentage)')
axes[1].set_ylabel('time to 30m (s)')
plt.show()
'''

#scaling the training data
scaler = StandardScaler()
scaled_train = scaler.fit_transform(X)
train_df = pd.DataFrame(data=scaled_train,columns=X.columns)

#using linear regression model for training
#linear regression gives us a clear idea about how each variable is related to the target using coefficients
linear_model = LinearRegression()
train_model = linear_model.fit(train_df,Y)
coefficients = train_model.coef_.reshape(-1,)
coefficients_df = pd.DataFrame({'features':train_df.columns , 'coefficients':coefficients})

#plotting a graph to show the strength of the variable and if it has positive or negative relation with the time to 30m 
'''
plt.figure()
plt.title('magnitue and direction of coefficients')
plt.xlabel('magnitude')
plt.ylabel('coefficients')
plt.barh(coefficients_df['features'],coefficients_df['coefficients'])
plt.show()
'''


