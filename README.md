<h1 align="center">Automated Report Generator</h1>

<p align="center">
  <strong>An automated Python pipeline that extracts data from emails and websites, then generates pristine Excel and PDF reports.</strong>
</p>

## 📝 Description

The **Automated Report Generator** is a Python-based utility designed to streamline the gathering and formatting of operational data. It connects to configured IMAP email servers and targeted web URLs to extract information. It then aggregates this incoming data into `pandas` DataFrames and renders comprehensive `.xlsx` spreadsheets and structured `.pdf` reports automatically.

It's perfect for quickly generating daily morning summaries without manual effort.

## ✨ Features

- **📧 Email Parsing**: Connects to any standard IMAP server (Gmail, Outlook, etc.), filters targeted emails, and extracts headers/bodies.
- **🌐 Web Scraping**: Utilizes `requests` and `BeautifulSoup` to scrape HTML websites and ingest custom web metrics.
- **📊 Automated Reporting**: Aggregates the gathered data and natively exports it to robust Excel sheets and readable PDF files.
- **⏰ Daemon Mode**: Includes a basic scheduling layer (`schedule`) to run the reporting pipeline recurrently on autopilot.

## 🛠 Prerequisites

- Python 3.8+
- Pip package manager

## 🚀 Installation & Setup

1. **Clone the repository** (or download the source code):
   ```bash
   git clone https://github.com/yourusername/automated-report-generator.git
   cd automated-report-generator
   ```

2. **Install the dependencies**:
   It is highly recommended to use a virtual environment (`python -m venv venv`).
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure your environment**:
   Rename or copy the configuration template:
   ```bash
   cp .env.example .env
   ```
   Open the `.env` file and insert your specific IMAP server credentials alongside the URL target you wish to scrape.

## 💻 Usage

To execute the pipeline and generate your reports immediately, run:
```bash
python src/main.py
```

If you wish to allow the script to remain persistently active and run scheduled jobs (e.g., automatically every day at 09:00 AM), run:
```bash
python src/main.py --daemon
```

After execution, the aggregated logic will create `output_report.xlsx` and `output_report.pdf` files in the root project directory.

## 📁 Architecture

- `src/main.py`: The entry point script and scheduler logic.
- `src/email_fetcher.py`: Connects to user specified inbox, searching matching criteria.
- `src/web_scraper.py`: Manages the remote HTML queries and DOM traversal.
- `src/report_generator.py`: Holds the Pandas (`to_excel`) and FPDF implementation logic.

## ✍️ Author

**Jyothsna**
