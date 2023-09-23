import requests
from bs4 import BeautifulSoup

# def scrape_livescore():
url="https://www.espncricinfo.com/live-cricket-score"
page=requests.get(url)

soup=BeautifulSoup(page.content,"html.parser")


#def scrape_livescore():
count=0
results=soup.find_all("div",class_="ds-text-compact-xxs")
def scrape_livescore():
    for result in results:    
        score=result.find("div",class_="ds-flex ds-flex-col ds-mt-2 ds-mb-2")
        s=result.find_all("span",class_="ds-text-compact-xs ds-mr-0.5")
        span=''
        for i in s:        
            if 'ov' in i.text:
                span=i.text
                break
            
        spans=span.split("\n")

        strong=result.find("strong")

        res=result.find("p",class_="ds-text-tight-s ds-font-regular ds-truncate ds-text-typo")
        teams=result.find_all("p",class_="ds-text-tight-m ds-font-bold ds-capitalize ds-truncate")
        return teams[0].text,spans[0],strong.text,teams[1].text,res.text



def scrape_result():
    results=soup.find_all("p",class_="ds-text-tight-s ds-font-regular ds-truncate ds-text-typo")
    for result in results:
        return result.text

        
        

