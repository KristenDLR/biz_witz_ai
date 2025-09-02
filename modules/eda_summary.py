import json

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


def save_summary_to_json(summary, path="reports/eda_summary.json"):
    with open(path, "w") as f:
        json.dump(summary, f, indent=2)

def validate_summary_structure(summary_dict):
    required_keys = [
        "top_products",
        "avg_sales",
        "monthly_sales",
        "satisfaction_distribution",
        "age_stats"
    ]

    for key in required_keys:
        if key not in summary_dict:
            raise ValueError(f"Missing key in summary: '{key}'")

    if not isinstance(summary_dict["top_products"], dict):
        raise TypeError("Expected 'top_products' to be a dict")

    if not isinstance(summary_dict["avg_sales"], (int, float)):
        raise TypeError("Expected 'avg_sales' to be a number")

    if not isinstance(summary_dict["monthly_sales"], dict):
        raise TypeError("Expected 'monthly_sales' to be a dict")

    if not isinstance(summary_dict["age_stats"], dict):
        raise TypeError("Expected 'age_stats' to be a dict")

    print("Summary structure is valid.")

