# from modules.config import OPENAI_API_KEY
from modules.data_loader import load_and_clean
from modules.eda_report import generate_profile_report

df = load_and_clean("data/sales_data.csv")
generate_profile_report(df)
