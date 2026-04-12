import os
import csv
from datetime import datetime

# Ask user to enter folder path
folder_path = input("Enter folder path: ")

# Get current timestamp (for file name)
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

# Output file name
output_file = f"All_Files_{timestamp}.csv"

# Open CSV file for writing
with open(output_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    
    # Updated header row
    writer.writerow([
        "File Name", 
        "File Extension", 
        "Size in KB", 
        "Creation Date", 
        "Last Modified Date", 
        "Complete Path of File"
    ])
    
    # Walk through folder and subfolders
    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            full_path = os.path.join(root, file_name)
            
            # Get file size in KB
            size_kb = os.path.getsize(full_path) / 1024
            
            # Split file name and extension
            name, extension = os.path.splitext(file_name)
            
            # Get creation and modified time
            creation_time = os.path.getctime(full_path)
            modified_time = os.path.getmtime(full_path)
            
            # Convert timestamp to readable format
            creation_date = datetime.fromtimestamp(creation_time).strftime("%Y-%m-%d %H:%M:%S")
            modified_date = datetime.fromtimestamp(modified_time).strftime("%Y-%m-%d %H:%M:%S")
            
            # Write row
            writer.writerow([
                name, 
                extension, 
                round(size_kb, 2), 
                creation_date, 
                modified_date, 
                full_path
            ])

print(f"\n✅ Done! File saved as: {output_file}")