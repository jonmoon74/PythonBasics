import requests
from bs4 import BeautifulSoup

url = "http://linuxcommand.org/lc3_lts0040.php"

src = requests.get(url)
content = src.text

soup = BeautifulSoup(content, "html.parser")

result1 = soup.find_all('table')
print(result1)
