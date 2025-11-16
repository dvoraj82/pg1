import sys
import requests


def download_url_and_get_all_hrefs(url):
    """
    Funkce stahne url predanou v parametru url pomoci volani response = requests.get(),
    zkontroluje navratovy kod response.status_code, ktery musi byt 200,
    pokud ano, najdete ve stazenem obsahu stranky response.content vsechny vyskyty
    <a href="url">odkaz</a> a z nich nactete url, ktere vratite jako seznam pomoci return
    """
    response = requests.get(url)

    if response.status_code != 200:
        raise Exception(f"Chyba při stahování stránky: {response.status_code}")
    
    html = response.text
    hrefs = []

    position = 0
    while True:
        a_start = html.find("<a", position)
        if a_start == -1:
            break

        href_position = html.find("href=", a_start)
        if href_position == -1:
            pos = a_start + 2
            continue

        uvozovky = html[href_position + 5]
        if uvozovky not in ['"', "'"]:
            position = href_position + 5
            continue

        value_start = href_position + 6
        value_end = html.find(uvozovky, value_start)
        if value_end == -1:
            position = value_start
            continue

        url_found = html[value_start:value_end]
        hrefs.append(url_found)

        position = value_end + 1
    
    
    return hrefs


if __name__ == "__main__":
    try:
        url = sys.argv[1]
        hrefs = download_url_and_get_all_hrefs(url)
    # osetrete potencialni chyby pomoci vetve except
        for href in hrefs:
            print(href)
    
    except Exception as e:
        print(f"Program skoncil chybou: {e}")
