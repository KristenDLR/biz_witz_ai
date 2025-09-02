import pandas as pd
from ydata_profiling import ProfileReport

def generate_profile_report(df, output_path="reports/eda_report.html"):
    profile = ProfileReport(df, title="Sales Data EDA", explorative=True)
    profile.to_file(output_path)



