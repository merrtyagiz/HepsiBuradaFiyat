import requests
from bs4 import BeautifulSoup
siteIsmi=input("Merhaba, lutfen Hepsi burada urununuzun linkini giriniz...")


def hepsiBuradaFiyatlar(siteIsmi):

    r=requests.get(siteIsmi)
    soup=BeautifulSoup(r.content,"html.parser")

    #ilkFiyat=soup.find_all("del",{"id":"originalPrice"})   #dilersem indirimsiz fiyati da görebilirim
    #print(ilkFiyat[0].text)

    fiyat=soup.find_all("span",{"itemprop":"price"})    #sitedeki fiyatin bilgisini çektim
    sonFiyatim=fiyat[0].text.split("(")                 #fiyati düzgün bir şekilde görebilmek için split etim
    return sonFiyatim[0]

print("Sonuc: ",hepsiBuradaFiyatlar(siteIsmi))

