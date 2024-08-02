import requests
from bs4 import BeautifulSoup

r = requests.get("https://www.theknot.com/content/pick-up-lines")
soup = BeautifulSoup(r.content, "html.parser")

for i in range(50):
    content = soup.findAll('ul', id = f"p-n-{i}")
    content