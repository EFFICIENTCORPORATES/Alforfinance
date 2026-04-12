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
    
    # Write header row
    writer.writerow(["File Name", "File Extension", "Size in KB", "Complete Path of File"])
    
    # Walk through folder and subfolders
    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            # Full path of file
            full_path = os.path.join(root, file_name)
            
            # Get file size in KB
            size_kb = os.path.getsize(full_path) / 1024
            
            # Split file name and extension
            name, extension = os.path.splitext(file_name)
            
            # Write data to CSV
            writer.writerow([name, extension, round(size_kb, 2), full_path])

# Print message when done
print(f"\nDone! File saved as: {output_file}")