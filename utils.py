import pandas as pd
df = pd.read_csv('data/titanic.csv') 
female_passengers = df[df['sex'] == 'male']
print(female_passengers)