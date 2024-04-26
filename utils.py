import pandas as pd
df = pd.read_csv('/Users/sheillapurwandiary/Desktop/HWR - BIPM_mac/Semester 2/EABD/git_kata/data/titanic.csv') 
female_passengers = df[df['Sex'] == 'female']
print(female_passengers)