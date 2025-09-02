# from modules.config import OPENAI_API_KEY
from modules.data_loader import load_and_clean
from modules.eda_report import generate_profile_report, summarize_eda
from modules.eda_summary import save_summary_to_json


df = load_and_clean("data/sales_data.csv")
generate_profile_report(df)

summary = summarize_eda(df)
print(summary)

save_summary_to_json(summary)