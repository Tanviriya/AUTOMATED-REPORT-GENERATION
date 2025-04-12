# Importing necessary libraries
import pandas as pd               # For reading and analyzing data
from fpdf import FPDF             # For creating PDF reports

# Setting the path to the CSV file (make sure this file exists at the given location)
file_path = "C:\\Users\\Admin\\Desktop\\python programming internship projects\\data.csv"

# Trying to read the CSV file
try:
    df = pd.read_csv(file_path)
except FileNotFoundError:
    print("Error: data.csv file not found. Please check the file path.")
    exit()  # Stop the program if file is not found

# Getting basic information about the dataset
summary_stats = df.describe().to_string()      # Summary like mean, min, max, etc.
print(df.describe())                           # Also print to console for verification
column_names = df.columns.tolist()             # List of column names
total_rows = len(df)                           # Total number of rows

# Creating a custom class to design the PDF layout
class PDFReport(FPDF):
    def header(self):
        self.set_font("Arial", "B", 16)         # Set font for the header
        self.cell(200, 10, "Automated Data Report", ln=True, align="C")  # Title at the top center
        self.ln(10)                              # Line break

    def footer(self):
        self.set_y(-15)                          # Position 15 units from the bottom
        self.set_font("Arial", "I", 10)          # Italic font for page number
        self.cell(0, 10, f"Page {self.page_no()}", align="C")

# Creating the PDF object and adding a page
pdf = PDFReport()
pdf.add_page()
pdf.set_font("Arial", size=12)                  # Set regular font size

# Adding dataset info to PDF
pdf.cell(200, 10, "Dataset Analysis Report", ln=True, align="C")  # Report title
pdf.ln(10)                                       # Line break
pdf.cell(0, 10, f"Total Rows: {total_rows}", ln=True)              # Row count
pdf.cell(0, 10, f"Columns: {', '.join(column_names)}", ln=True)    # Columns

pdf.ln(5)                                        # Extra spacing

# Adding summary statistics to PDF
pdf.set_font("Arial", "B", 12)                   # Bold for heading
pdf.cell(0, 10, "Summary Statistics:", ln=True)
pdf.set_font("Arial", size=10)                   # Regular font for data

pdf.multi_cell(0, 10, summary_stats)             # Multiline text for stats
pdf.ln(5)

# Saving the PDF report
pdf_file_name = "generated_report.pdf"
pdf.output(pdf_file_name)                        # Generates and saves the PDF file

print(f"PDF Report Generated: {pdf_file_name}")  # Confirmation message
