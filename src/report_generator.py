import pandas as pd
from fpdf import FPDF
import logging

logger = logging.getLogger(__name__)

def generate_excel(data, filename="output_report.xlsx"):
    """Generate Excel report from a list of dicts using pandas."""
    if not data:
        logger.warning("No data provided to generate Excel report.")
        return
        
    df = pd.DataFrame(data)
    df.to_excel(filename, index=False)
    logger.info(f"Excel report successfully generated: {filename}")

def generate_pdf(data, filename="output_report.pdf"):
    """Generate a PDF summary report."""
    if not data:
        logger.warning("No data provided to generate PDF report.")
        return
        
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("helvetica", "B", 16)
    pdf.cell(0, 10, "Automated Data Report", new_y="NEXT", align="C")
    
    pdf.set_font("helvetica", size=12)
    pdf.cell(0, 10, "Data Summary:", new_y="NEXT")
    
    pdf.set_font("helvetica", size=10)
    for index, row in enumerate(data):
        pdf.set_font("helvetica", "B", 10)
        pdf.cell(0, 8, f"Entry {index + 1}:", new_y="NEXT")
        pdf.set_font("helvetica", "", 10)
        for key, value in row.items():
            text = f"  {key}: {value}"
            # encode text properly or simply ignore unmappable
            # standard fpdf requires handling unicode, avoiding emojis
            pdf.cell(0, 6, text, new_y="NEXT")
        pdf.cell(0, 4, "", new_y="NEXT") # spacing
        
    pdf.output(filename)
    logger.info(f"PDF report successfully generated: {filename}")
