
# coding: utf-8

# In[45]:


import pandas as pd
import numpy as np


# In[46]:


cols = ['Age', 'Sex', 'Chest_pain_type', 'Resting_BP', 'Cholestrol_mg/dl', 'Fasting_sugar', 'Resting_ECG', 'Max_HR_achieved', 'Exercise_induced_angina', 'ST_depression', 'Slope_of_peak_exercise', 'Colored_vessels', 'Thal', 'Diagnosis']


# In[47]:


cleveland_file = 'heart_disease_classify/processed_cleveland.csv'
hungarian_file = 'heart_disease_classify/processed_hungarian.csv'
switzerland_file = 'heart_disease_classify/processed_switzerland.csv'
long_beach_file = 'heart_disease_classify/processed_va.csv'

cleveland = pd.read_csv(cleveland_file, names = cols)
hungarian = pd.read_csv(hungarian_file, names = cols)
switzerland = pd.read_csv(switzerland_file, names = cols)
long_beach = pd.read_csv(long_beach_file, names  = cols)


# In[48]:


df = cleveland.append(hungarian, ignore_index = True)
df = df.append(switzerland, ignore_index = True)
df = df.append(long_beach, ignore_index = True)
df = df.replace('?', np.NaN)
df = df.astype(float)


# In[49]:


df


# In[50]:


# Counting missing values

count_nans = []

for column in cols:
    count_nans.append(df[column].isnull().sum())

count_nans


# In[51]:


# Converting to binary

df[df['Diagnosis'] * 1 != 0] = 1.0


# In[52]:


df = df.drop(['Slope_of_peak_exercise', 'Colored_vessels', 'Thal'], axis = 1)


# In[53]:


df


# In[54]:


df.to_csv('fill_missing_values.csv', index = False)

