import pandas as pd

file_path = 'bills.csv' 
df = pd.read_csv(file_path)

max_valid_duration = 86400 
df = df[df['order_duration_seconds'] <= max_valid_duration]

venue_xref_id_filter = '3b26b048e5d84c63fd58ceccd2ce99f9b7590d91f9c5e0122ba7770b45933582'
df = df[df['venue_xref_id'] == venue_xref_id_filter]

df = df[df['bill_total_billed'] > 0]

sample_fraction = 1
sampled_df = df.sample(frac=sample_fraction, random_state=1837)

sampled_file_path = 'filtered_ottawa_bar2.csv'
sampled_df.to_csv(sampled_file_path, index=False)

print(f"\nSampled dataset saved to {sampled_file_path}")