# app/utils.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def load_and_filter_data(country, threshold):
    country_files = {
        "Benin": "benin_clean.csv",
        "Sierra Leone": "sierraleone_clean.csv",
        "Togo": "togo_clean.csv"
    }
    filename = country_files.get(country)
    if not filename:
        raise ValueError(f"Unknown country: {country}")

    # Compute the project root path
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # Normalize the path to use correct separators
    file_path = os.path.normpath(os.path.join(base_dir, "uidata", filename))
    
 
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    df = pd.read_csv(file_path)
    if 'GHI' not in df.columns:
        raise KeyError("GHI column not found in the dataset")
    return df[df['GHI'] > threshold]

def plot_ghi_boxplot(data):
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.boxplot(y='GHI', data=data, ax=ax)
    ax.set_title(f'GHI Distribution for {data.shape[0]} Samples')
    ax.set_ylabel('GHI (W/m²)')
    return fig

def create_summary_table(data, threshold):
    summary = data[['GHI', 'DNI', 'DHI']].agg(['mean', 'median']).round(2)
    return summary