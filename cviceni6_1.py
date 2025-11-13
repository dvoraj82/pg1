import requests

def download_rates(url):
    response = requests.get(url)
    if not response.ok:
        return None
    
    rates = {}

    data = response.text
    data = data.split('\n')
    date = data[0].split('#')[0].strip()

    for line in data[2:]:
        fields = line.split('|')
        if len(fields) < 5:
            continue
        multipl = int(fields[2])
        rates[fields[3]] = float(fields[4].replace(',', '.')) / multipl

    return date, rates


if __name__ == "__main__":

    date, listek = download_rates("http://www.cnb.cz/cs/financni_trhy/devizovy_trh/kurzy_devizoveho_trhu/denni_kurz.txt")

    print(date)
    print(listek)

