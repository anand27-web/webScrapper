from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

app = Flask(__name__)
CORS(app) 

@app.route('/api/scrape', methods=['POST'])
def scrape_url():
    data = request.json
    target_url = data.get('url')
    
    if not target_url:
        return jsonify({"error": "No URL provided."}), 400

    try:
        print(f"Scraping: {target_url}")
        
        # Our Fake ID
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        }
        
        response = requests.get(target_url, headers=headers, timeout=10)
        
        if response.status_code != 200:
            return jsonify({"error": f"Website returned status code {response.status_code}"}), 400
            
        soup = BeautifulSoup(response.text, 'html.parser')
        
        page_title = soup.title.string.strip() if soup.title else "No Title Found"
        headings = [h.text.strip() for h in soup.find_all(['h1', 'h2']) if h.text.strip()]
        top_headings = headings[:5]
        total_links = len(soup.find_all('a'))

        # ==========================================
        # NEW PIPELINE LOGIC: Export to CSV
        # ==========================================
        # 1. Structure the data for pandas
        pipeline_data = {
            "URL": [target_url],
            "Page Title": [page_title],
            "Total Links": [total_links],
            # Join the list of headings into a single string so it fits in one spreadsheet cell
            "Top Headings": [", ".join(top_headings)] 
        }
        
        # 2. Convert to a DataFrame (a virtual spreadsheet)
        df = pd.DataFrame(pipeline_data)
        
        # 3. Define the file name
        csv_filename = "market_data_export.csv"
        
        # 4. Save it! If the file exists, append a new row. If not, create it.
        if not os.path.isfile(csv_filename):
            df.to_csv(csv_filename, index=False)
        else:
            df.to_csv(csv_filename, mode='a', header=False, index=False)
            
        print(f"Data successfully saved to {csv_filename}")
        # ==========================================

        return jsonify({
            "success": True,
            "url": target_url,
            "title": page_title,
            "top_headings": top_headings,
            "total_links": total_links,
            "message": "Data exported to CSV successfully!"
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)