import pandas as pd

df = pd.read_csv("dataset.csv")

initial_columns = df.columns.tolist()
initial_shape = df.shape
initial_na = df.isna().sum()

if 'Unnamed: 0' in df.columns:
    df = df.drop(columns=['Unnamed: 0'])

essential_columns = ['track_name', 'artists', 'popularity', 'danceability', 'energy']
df_cleaned = df.dropna(subset=essential_columns)

final_columns = df_cleaned.columns.tolist()
final_shape = df_cleaned.shape
final_na = df_cleaned.isna().sum()

output_path = "cleaned_dataset.csv"
df_cleaned.to_csv(output_path, index=False)

{
    "initial_shape": initial_shape,
    "final_shape": final_shape,
    "initial_columns": initial_columns,
    "final_columns": final_columns,
    "initial_na": initial_na.to_dict(),
    "final_na": final_na.to_dict(),
    "cleaned_file": output_path
}
