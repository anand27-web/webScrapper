import requests
from bs4 import BeautifulSoup

# 1. Define our target URL
url = "http://books.toscrape.com/"

# 2. Send a GET request (This is your Python script acting like a web browser)
print("Sending request to website...")
response = requests.get(url)

# 3. Check if the website allowed us in (HTTP Status Code 200 means OK)
if response.status_code == 200:
    print("Successfully connected!\n")
    print("-" * 30)
    
    # 4. Hand the raw HTML over to BeautifulSoup to parse it into a readable structure
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # 5. Use the map we found in Step 1: Find ALL book containers on the page
    books = soup.find_all('article', class_='product_pod')
    
    print(f"Found {len(books)} books on the front page. Extracting data...\n")
    
    # 6. Loop through the first 5 books to extract our specific data points
    for book in books[:5]:
        # The title is stored in the 'title' attribute of the <a> tag inside the <h3> tag
        title = book.h3.a['title']
        
        # The price is the text inside the <p> tag that has the class 'price_color'
        price = book.find('p', class_='price_color').text
        
        # Print the cleaned-up results
        print(f"Title: {title}")
        print(f"Price: {price}")
        print("-" * 30)

else:
    print(f"Failed to connect. The server returned status code: {response.status_code}")