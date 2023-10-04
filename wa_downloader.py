import datetime
import requests
from bs4 import BeautifulSoup
from clint.textui import progress

class FetchData:
  host = None
  html = None
  headers = {
    'User-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
  }

  def get (self, param):
    r = requests.get(f'{self.host}{param}', headers=self.headers, allow_redirects=True)
    htmlParser = BeautifulSoup(r.content, 'html.parser')
    self.html = htmlParser

  def download (self, param, filePath):
    fileDownload = requests.get(f'{self.host}{param}', headers=self.headers, allow_redirects=True, stream=True)

    with open(filePath, 'wb') as f:
      totalLength = int(fileDownload.headers.get('content-length'))
      for chunk in progress.bar(fileDownload.iter_content(chunk_size=1024), expected_size=(totalLength / 1024) + 1):
        if chunk:
          f.write(chunk)
          f.flush()

def getLink (elm):
  href = elm['href']
  return href

def output (message):
  now = datetime.datetime.now()
  startText = now.strftime("%H:%M:%S")
  print(f'{startText} ==> {message}')

def main ():
  output('Connecting application...')
  app = FetchData()
  
  app.host = 'https://www.apkmirror.com'

  output('Searching for latest whatsapp beta...')
  app.get('/apk/whatsapp-inc/whatsapp/')

  findLatestWhatsAppBeta = app.html.find_all('a', 'fontBlack')
  whatsBetaLinkReleaseFilter = next((link for link in findLatestWhatsAppBeta if 'beta' in link.text.strip()), None)
  version = next((v for v in whatsBetaLinkReleaseFilter.text.split() if '.' in v), None)
  whatsAppLink = getLink(whatsBetaLinkReleaseFilter)

  pathFile = f'whatsapp_{version}_beta.apk'
  output('[OK] Found!!!')

  output('Connecting at download server...')
  app.get(whatsAppLink)
  waDownloadPage = app.html.find_all('a', class_='accent_color')
  waDownloadPageFilter = next((link for link in waDownloadPage if link.text.strip() == version), None)
  waDownloadPageLink = getLink(waDownloadPageFilter)
  output('[OK] Connected')

  output('Bypass on protected page...')
  app.get(waDownloadPageLink)
  bypassLinkDownload = app.html.find('a', class_='downloadButton')
  bypassLink = getLink(bypassLinkDownload)
  output('[OK] Done')

  output(f'Getting download link of whatsapp version {version} beta')
  app.get(bypassLink)
  downloadWhatsAppElm = app.html.find('a', string='here')
  downloadWhatsApp = getLink(downloadWhatsAppElm)
  output('[OK] Got!!!')

  output(f'Downloading {pathFile}')
  app.download(downloadWhatsApp, pathFile)
  output(f'Completed your file is {pathFile}.')

if __name__ == '__main__':
  main()