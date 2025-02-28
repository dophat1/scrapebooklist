import requests
from bs4 import BeautifulSoup
import json
import time


all_data = []

# Scrape pages from 1 to 106
for page in range(1, 107):
    base_url = "https://dtv-ebook.com.vn/tieu-thuyet-490/{page}.html"
    url = base_url.format(page=page)
    try:
        response = requests.get(url, timeout=100)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)
    except requests.exceptions.RequestException as e:
        print(f"Error fetching page {page}: {e}")
        continue

    # Parse the page content
    soup = BeautifulSoup(response.text, 'html.parser')

    # Get the current page number
    current_page_elem = soup.find('li', class_="current")
    current_page = current_page_elem.get_text(strip=True) if current_page_elem else f"Page {page}"

    # Extract book titles
    book_titles = soup.find_all('h2', class_="tensanpham")
    titles = [title.get_text(strip=True) for title in book_titles]

    for title in titles:
        all_data.append({
            "title": title,
            "page": current_page
        })

    print(f"Scraped {len(titles)} books from {current_page}.")
    if len(titles) == 0:
        print('The end')
        break
    else:
        continue

    time.sleep(1)  # Avoid overloading the server

output_file = "tieuthuyet.json"
with open(output_file, "w", encoding="utf-8") as file:
    json.dump(all_data, file, ensure_ascii=False, indent=4)

print(f"Scraping complete. Total books scraped: {len(all_data)}")