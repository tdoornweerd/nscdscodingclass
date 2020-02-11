import pandas as pd
insurence = pd.read_csv('FL_insurance_sample.csv')
print(insurence.groupby('county').min()['tiv_2012'])