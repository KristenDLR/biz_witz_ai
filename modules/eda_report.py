import pandas as pd
from ydata_profiling import ProfileReport

def generate_profile_report(df, output_path="reports/eda_report.html"):
    profile = ProfileReport(df, title="Sales Data EDA", explorative=True)
    profile.to_file(output_path)


def summarize_eda(df):
    monthly_sales_raw = df.groupby(df['date'].dt.to_period('M'))['sales'].sum()
    monthly_sales = {str(period): float(sales) for period, sales in monthly_sales_raw.items()}

    return {
        "top_products": df['product'].value_counts().head(3).to_dict(),
        "avg_sales": float(df['sales'].mean()),
        "monthly_sales": monthly_sales,
        "satisfaction_distribution": df['customer_satisfaction'].value_counts().to_dict(),
        "age_stats": {
            "mean": float(df['customer_age'].mean()),
            "std": float(df['customer_age'].std()),
            "min": int(df['customer_age'].min()),
            "max": int(df['customer_age'].max())
        }
    }

