import requests
import pandas as pd

# URL of the page
url = "https://www.zaubacorp.com/companies-list/status-Strike%20Off/p-100-company.html"

# Get HTML content
response = requests.get(url)

# Use pandas to read all tables from the page
tables = pd.read_html(response.text)

# Usually the first table is the one we want
df = tables[0]

# Save to Excel file
output_file = "companies_list.xlsx"
df.to_excel(output_file, index=False)

print("✅ Data saved to:", output_file)