from bs4 import BeautifulSoup
import requests

# Start the session
session = requests.Session()

# Create the payload
payload = {'_username': '[USERNAME]', '_password': '[PASSWORD]'}

# Post the payload to the site to log in
s = session.post("https://github.com/login", data=payload)

# Navigate to the next page and scrape the data
s = session.get('https://github.com/[USERNAME]')

soup = BeautifulSoup(s.text, 'html.parser')
results = soup.find(class_='js-pinned-items-reorder-container')
job_elems = results.find_all(
    'div', class_='Box pinned-item-list-item d-flex p-3 width-full js-pinned-item-list-item public fork reorderable sortable-button-item')
for job_elem in job_elems:
    title_elem = job_elem.find('span', class_='repo')
    print(title_elem.text.strip())