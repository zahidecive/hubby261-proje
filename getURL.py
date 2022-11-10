import urllib.request
from bs4 import BeautifulSoup

class GetURL:

    dataFile = "dataURL.txt"
    getFile = "getURL.txt"

    def __init__(self):
        fileTest = open(self.getFile, 'a')
        fileTest.close()

    def getWeb(self):

        print("Örümcek çalışıyor...")

        dataOpen = open(self.dataFile, 'r')
        getOpen = open(self.getFile, 'w')

        for dataGet in dataOpen:

            kontrolHTTP = dataGet[:7]
            kontrolHTTPS = dataGet[:8]
            if kontrolHTTP == 'http://' or kontrolHTTPS == 'https://':
                print('Ziyaret edilen URL:' +dataGet)


            webSite = urllib.request.urlopen(dataGet)
            getBytes = webSite.read()
            webPage = getBytes.decode("utf8")
            webSite.close()
            soup = BeautifulSoup(webPage, 'html.parser')
            getOpen.write(dataGet.strip() + " - " + soup.title.contents[0] + "\n")

        else:
            print('Ön eki eksik,' + dataGet + 'ziyaret tamamlanamadı!')

        dataOpen.close()
        getOpen.close()

        print("Çalışma tamamlandı!")

    def getList(self):

        getOpen = open(self.getFile, 'r')
        for dataShow in getOpen:
          print(dataShow)
        getOpen.close()
