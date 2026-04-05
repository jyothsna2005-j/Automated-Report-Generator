import os
import schedule
import time
from dotenv import load_dotenv
import logging

# Set up root logger
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

from email_fetcher import fetch_email_data
from web_scraper import fetch_web_data
from report_generator import generate_excel, generate_pdf

def run_job():
    logger.info("Starting automated report generation job...")
    # Load or reload variables from .env
    load_dotenv(override=True) 

    email_data = fetch_email_data()
    web_data = fetch_web_data()
    
    # Combine data
    combined_data = email_data + web_data
    
    # Generate reports if we have data
    if combined_data:
        excel_out = os.getenv("OUTPUT_EXCEL", "output_report.xlsx")
        pdf_out = os.getenv("OUTPUT_PDF", "output_report.pdf")
        
        generate_excel(combined_data, excel_out)
        generate_pdf(combined_data, pdf_out)
        logger.info("Job completed successfully.")
    else:
        logger.warning("No data collected from any source. Reports skipped.")

if __name__ == "__main__":
    # Optionally, we can accept arguments for cron mode
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "--daemon":
        schedule.every().day.at("09:00").do(run_job)
        logger.info("Running in daemon mode. Scheduler is running. Waiting for next job...")
        while True:
            schedule.run_pending()
            time.sleep(60)
    else:
        # Run once immediately
        logger.info("Running job once.")
        run_job()
