# Automated Web Scraping & Data Pipeline

A full-stack data extraction engine and pipeline designed to gather, parse, and export web data. It features a custom Python backend for scraping and a sleek, interactive frontend dashboard for real-time data visualization.

## 🚀 Features

* **Custom Extraction Engine:** Engineered using Python, `requests`, and `BeautifulSoup` to bypass standard security and map DOM structures.
* **Automated Data Pipeline:** Cleans and structures extracted HTML/XML data (titles, links, headings) using `pandas`.
* **Structured Export:** Automatically logs and appends successful scrapes into a structured CSV format for downstream trend visualization.
* **Interactive Dashboard:** A modern, responsive HTML/JS frontend that allows users to input target URLs and view extracted metadata in real-time.
* **RESTful API:** Flask backend handles Cross-Origin Resource Sharing (CORS) and serves extraction logic to the client.

## 🛠️ Tech Stack

* **Backend:** Python 3, Flask
* **Data Processing:** Pandas, BeautifulSoup4, Requests
* **Frontend:** HTML5, CSS3 (Custom Variables, Animations), Vanilla JavaScript
* **Environment:** macOS, Python `venv`

## ⚙️ Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/yourusername/market-scraper.git](https://github.com/yourusername/market-scraper.git)
   cd market-scraper