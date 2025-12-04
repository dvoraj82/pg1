from muj_modul import fibonaci
import requests
from unittest.mock import MagicMock


class Downloader:
    def __init__(self):
        self.url = "http://www.cnb.cz/cs/financni_trhy/devizovy_trh/kurzy_devizoveho_trhu/denni_kurz.txt"
        self.data = {}
        self.get()
 
 
    def get(self):
        responce = requests.get(self.url)
        if not responce.ok:
            return None
        data = {}
        for line in responce.text.split('\n')[2:]:
            s = line.split('|')
            if len(s) < 5:
                continue
            self.data[s[3]] = float(s[4].replace(',', '.'))
        
    
    def convert_from_czk(self, ammount_czk, code):
        return ammount_czk / self.data[code]


def test_downloader():
    requests.get = MagicMock(
        return_value=MagicMock(
            ok=True,
            text="""03.12.2025 #234
země|měna|množství|kód|kurz
USA|dolar|1|USD|20,660"""
))


    downloader = Downloader()
    data = downloader.get()
    assert round(downloader.convert_from_czk(100, "USD"), 2) == 4.84
            


#def test_fibonaci():
#    assert fibonaci(2) == [1, 1, 2]
#    assert fibonaci(10) == [1, 1, 2, 3, 5, 8]



if __name__ == "__main__":
    downloader = Downloader()
    downloader.get()
    print(downloader.convert_from_czk(100, "USD"))