import os
from PyPDF2 import PdfMerger

# Folder where your PDFs are stored
folder_path = r"F:\EffCorp_Courses\Day06\all_downloaded_pdf"

# Output merged PDF file
output_file = os.path.join(folder_path, "Merged_Output.pdf")

# Create a PdfMerger object
merger = PdfMerger()

# Get all files from folder
files = os.listdir(folder_path)

# Filter only PDF files
pdf_files = []
for file in files:
    if file.endswith(".pdf"):
        pdf_files.append(file)

# Optional: sort files (important for correct order)
pdf_files.sort()

# Add each PDF to merger
for pdf in pdf_files:
    full_path = os.path.join(folder_path, pdf)
    print("Adding:", pdf)
    merger.append(full_path)

# Write merged PDF
merger.write(output_file)

# Close merger
merger.close()

print("\nDone! Merged PDF saved as:", output_file)