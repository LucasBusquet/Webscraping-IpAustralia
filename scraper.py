from bs4 import BeautifulSoup
import requests
from csv import writer
i = 0
url = "https://search.ipaustralia.gov.au/trademarks/search/view/187554?q=tm"

with open('webscraper.csv', 'w', encoding='utf-8', newline='') as f:
    theWriter = writer(f)
    header = ['Number', 'Words', 'Image Description',
              'Status', 'Priority Date', 'Class', 'Kind']
    theWriter.writerow(header)
    while i < 50:
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')

        # Primera parte
        lists = soup.find_all(
            'div', class_="col c-50 box-with-shadow flex-col")

        # El if chequea si tiene o no tiene descripcion la imagen

        if soup.find('dl', class_="list-of-definition list-up-down").find_next('dt').find_next('dt').text == 'Image description':
            for list in lists:
                number = list.find('dd').text.replace('\n', '')
                words = list.find('dd').find_next('dd').text.replace('\n', '')
                imgDesc = list.find('dd').find_next(
                    'dd').find_next('dd').text.replace('\n', '')
                status = list.find('dl', class_="list-of-definition list-up-down").find(
                    'i').find_next('span').text.replace('\n', '')
                prioDate = list.find('dd').find_next('dd').find_next(
                    'dd').find_next('dd').find_next('dd').text.replace('\n', '')
                classN = list.find('dd').find_next('dd').find_next('dd').find_next(
                    'dd').find_next('dd').find_next('dd').text.replace('\n', '')
                kind = list.find('dd').find_next('dd').find_next('dd').find_next(
                    'dd').find_next('dd').find_next('dd').find_next('dd').text.replace('\n', '')
        else:
            for list in lists:
                number = list.find('dd').text.replace('\n', '')
                words = list.find('dd').find_next('dd').text.replace('\n', '')
                imgDesc = 0
                status = list.find('dl', class_="list-of-definition list-up-down").find(
                    'i').find_next('span').text.replace('\n', '')
                prioDate = list.find('dd').find_next('dd').find_next(
                    'dd').find_next('dd').text.replace('\n', '')
                classN = list.find('dd').find_next('dd').find_next(
                    'dd').find_next('dd').find_next('dd').text.replace('\n', '')
                kind = list.find('dd').find_next('dd').find_next('dd').find_next(
                    'dd').find_next('dd').find_next('dd').text.replace('\n', '')

        info = [number, words, imgDesc, status, prioDate, classN, kind]
        theWriter.writerow(info)
        url2 = soup.find('a', id='nextMark').get('href')
        url = "https://search.ipaustralia.gov.au" + url2
        i = i + 1

# Segunda parte

# goodAndServ = soup.find('dl', class_= "list-of-definition goods-service").find('dd')

# Tercer parte

# oppDetail = soup.find('div', class_= "opposition-summary").find('p')
