import requests
import bs4
 
def findImages(what):
    url = f"https://commons.wikimedia.org/w/index.php?search={what}&title=Special:MediaSearch&type=image"
    result = requests.get(url).content
    items = bs4.BeautifulSoup(result, "html.parser").find_all(class_="sd-image")
    for image in items:
        print(f"alt:{image['alt']} || url:{image['src']}")
 
findImages("dog")