import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r"C:\Users\Zubenathi\Downloads\WA_Fn-UseC_-Telco-Customer-Churn.csv")

df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
df.dropna(subset=['TotalCharges'], inplace=True)

#Convert Churn to binary
df['Churn_Flag'] = (df['Churn'] == 'Yes').astype(int)

#Create cohort column(signup month based on tenure)
df['Signup_Month'] = pd.to_datetime('2020-01-01') - pd.to_timedelta(df['tenure'] * 30, unit='D')
df['Cohort_Month'] = df['Signup_Month'].dt.to_period('M')

#Preview
print(df[['customerID', 'tenure', 'MonthlyCharges', 'Churn','Cohort_Month']].head())
print("\nChurn rate:", df['Churn_Flag'].mean())

#Create cohort index(months since signup)
df['Cohort'] = df['Cohort_Month'].dt.strftime('%Y-%m')
cohorts = df.groupby('Cohort')['customerID'].count().rename('Total_Customers')

#Retention table
retention = pd.crosstab(df['Cohort'], df['tenure'])

if 0 in retention.columns:
    retention = retention.div(retention[0], axis=0)
else:
    retention = retention.div(retention[retention.columns[0]], axis=0)

#Show top 10 cohorts, months 0-12
print(retention.iloc[:10, :13].round(2))

# Group by contract type
churn_by_contract = df.groupby('Contract')['Churn_Flag'].mean().sort_values()
print(churn_by_contract)

# Group by payment method
churn_by_payment = df.groupby('PaymentMethod')['Churn_Flag'].mean().sort_values(ascending=False)
print(churn_by_payment)

# EXPORT TO DOWNLOADS - ADD THIS LINE
df.to_csv(r"C:\Users\Zubenathi\Downloads\cleaned_customer_data.csv", index=False)
print("\n✓ File saved to: C:\\Users\\Zubenathi\\Downloads\\cleaned_customer_data.csv")

# Tenure vs churn
plt.figure(figsize=(10,4))
df.boxplot(column='tenure', by='Churn')
plt.title('Tenure Distribution: Churned vs Retained')
plt.suptitle('')
plt.show()

# Monthly charges distribution
sns.histplot(data=df, x='MonthlyCharges', hue='Churn', bins=30, alpha=0.6)
plt.title('Monthly Charges by Churn Status')
plt.show()