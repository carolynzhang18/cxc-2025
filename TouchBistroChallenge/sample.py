import pandas as pd

file_path = 'bills.csv' 
df = pd.read_csv(file_path)

max_valid_duration = 86400 
df = df[df['order_duration_seconds'] <= max_valid_duration]

df = df[df['bill_total_billed'] > 0]

sample_fraction = 1
sampled_df = df.sample(frac=sample_fraction, random_state=1837)

sampled_file_path = 'filtered_day.csv'
sampled_df.to_csv(sampled_file_path, index=False)

print(f"\nSampled dataset saved to {sampled_file_path}")
