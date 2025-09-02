import pandas as pd
from ydata_profiling import ProfileReport

def generate_profile_report(df, output_path="reports/eda_report.html"):
    profile = ProfileReport(df, title="Sales Data EDA", explorative=True)
    profile.to_file(output_path)


def summarize_eda(df):
    return {
        "top_products": df['product'].value_counts().head(3).to_dict(),
        "avg_sales": df['sales'].mean(),
        "monthly_sales": df.groupby(df['date'].dt.to_period('M'))['sales'].sum().to_dict(),
        "satisfaction_distribution": df['customer_satisfaction'].value_counts().to_dict(),
        "age_stats": {
            "mean": df['customer_age'].mean(),
            "std": df['customer_age'].std(),
            "min": df['customer_age'].min(),
            "max": df['customer_age'].max()
        }
    }
