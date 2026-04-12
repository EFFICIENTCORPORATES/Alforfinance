import requests
from bs4 import BeautifulSoup
import os

# URL of the webpage
url = "https://www.icai.org/post/bos-int-p1-may2026-exam"

# Folder where PDFs will be saved
save_folder = r"F:\EffCorp_Courses\Day06\all_downloaded_pdf"

# Create folder if it does not exist
if not os.path.exists(save_folder):
    os.makedirs(save_folder)

# Get webpage content
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Find all links (<a> tags)
links = soup.find_all("a")

# Loop through all links
for link in links:
    href = link.get("href")
    
    # Check if link is a PDF
    if href and ".pdf" in href:
        
        # If link is relative, make it full URL
        if href.startswith("/"):
            pdf_url = "https://www.icai.org" + href
        else:
            pdf_url = href
        
        print("Downloading:", pdf_url)
        
        try:
            # Download PDF
            pdf_response = requests.get(pdf_url)
            
            # Get file name from URL
            file_name = pdf_url.split("/")[-1]
            
            # Full path where file will be saved
            file_path = os.path.join(save_folder, file_name)
            
            # Save file
            with open(file_path, "wb") as f:
                f.write(pdf_response.content)
            
            print("Saved:", file_name)
        
        except Exception as e:
            print("Error downloading:", pdf_url)
            print(e)

print("\nAll downloads completed!")