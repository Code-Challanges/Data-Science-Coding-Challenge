import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# Set random seed for reproducibility
np.random.seed(42)

# Number of customers
num_customers = 1000

# Generate random customer data
customer_id = np.arange(1, num_customers + 1)
age = np.random.randint(18, 70, size=num_customers)
gender = np.random.choice(['male', 'female', 'non-binary'], size=num_customers, p=[0.48, 0.48, 0.04])
annual_income = np.random.randint(20000, 120000, size=num_customers)
purchase_amount = np.round(np.random.uniform(10, 5000, size=num_customers), 2)
purchase_count = np.random.randint(1, 100, size=num_customers)

# Generate dates
today = datetime.now()
join_dates = [today - timedelta(days=random.randint(365, 365*10)) for _ in range(num_customers)]
last_purchase_dates = [join_date + timedelta(days=random.randint(1, (today - join_date).days)) for join_date in join_dates]

# Calculate average purchase intervals and total spent
avg_purchase_interval_days = [random.randint(1, 90) for _ in range(num_customers)]
total_spent = np.round(purchase_amount * purchase_count, 2)

# Churn labels (1 = churned, 0 = active)
label_churn = np.random.choice([0, 1], size=num_customers, p=[0.85, 0.15])

# Create the DataFrame
data = {
    'customer_id': customer_id,
    'age': age,
    'gender': gender,
    'annual_income': annual_income,
    'purchase_amount': purchase_amount,
    'purchase_count': purchase_count,
    'join_date': join_dates,
    'last_purchase_date': last_purchase_dates,
    'avg_purchase_interval_days': avg_purchase_interval_days,
    'total_spent': total_spent,
    'label_churn': label_churn
}

df = pd.DataFrame(data)

# Save the generated DataFrame to a CSV file
file_path = '/mnt/data/ecommerce_customer_data.csv'
df.to_csv(file_path, index=False)

file_path
