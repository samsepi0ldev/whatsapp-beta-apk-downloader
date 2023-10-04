import requests
from bs4 import BeautifulSoup
from clint.textui import progress

host = 'https://www.apkmirror.com'
url = f'{host}/apk/whatsapp-inc/whatsapp/'
headers = {
  'User-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
}

print('Connecting in server...')
page = requests.get(url, headers=headers, allow_redirects=True)
soup = BeautifulSoup(page.content, "html.parser")

print('Search for version of WhatsApp Beta...')
links_wa = soup.find_all('a', class_='fontBlack')

wa_link = next((link_wa for link_wa in links_wa if 'beta' in link_wa.text.strip()), None)
next_link = f'{host}{wa_link["href"]}'

version = next(text for text in wa_link.text.split() if '.' in text)

download_page = requests.get(next_link, headers=headers, allow_redirects=True)
soup_download_page = BeautifulSoup(download_page.content, "html.parser")

download_page_link = soup_download_page.find_all('a', string=lambda text: version, class_='accent_color')
wa_download_parse = next((link for link in download_page_link if link.text.strip() == version), None)['href']
wa_download_link = f'{host}{wa_download_parse}'

print('Parsing path...')

download_apk = requests.get(wa_download_link, headers=headers, allow_redirects=True)
download_apk_soup = BeautifulSoup(download_apk.content, "html.parser")

download_link = download_apk_soup.find('a', class_='downloadButton')['href']

wa_beta_download_link = f'{host}{download_link}'

print('Getting link to download...')

downloaded = requests.get(wa_beta_download_link, headers=headers, allow_redirects=True)

downloaded_parse = BeautifulSoup(downloaded.content, "html.parser")
wa_link_download_elm = downloaded_parse.find('a', string='here')['href']
wa_link_download = f'{host}{wa_link_download_elm}'

print('Initialing download...')

download_wa_request = requests.get(wa_link_download, headers=headers, allow_redirects=True, stream=True)
path = f'wa_beta_{version}.apk'

with open(path, 'wb') as f:
  total_length = int(download_wa_request.headers.get('content-length'))
  for chunk in progress.bar(download_wa_request.iter_content(chunk_size=1024), expected_size=(total_length/1024) + 1):
    if chunk:
      f.write(chunk)
      f.flush()
