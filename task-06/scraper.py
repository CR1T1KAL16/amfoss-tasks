
        
import os
import discord
intents = discord.Intents.default()
client = discord.Client(intents=intents)    
import aiofiles
  

import requests
from bs4 import BeautifulSoup
from datetime import datetime
import csv


def scrape_livescore():
    
    url = 'https://www.espncricinfo.com/live-cricket-score'
    # url has been requested
    response = requests.get(url,verify=False)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    all=soup.find("div",class_="ds-text-compact-xxs").text
    team1 = soup.find("p",class_="ds-text-tight-m ds-font-bold ds-capitalize ds-truncate").text    
    team2 = soup.find_all("p",class_="ds-text-tight-m ds-font-bold ds-capitalize ds-truncate")[1].text

    score1 = soup.find('strong').text
    score2 = soup.find_all('strong')[1].text

    over1=soup.find('span',class_="ds-text-compact-xs ds-mr-0.5").text
    over2=soup.find_all('span',class_="ds-text-compact-xs ds-mr-0.5")[1].text
    if over1 not in all or over2 not in all:
        over1='-'
        over2='-'

    result=soup.find("p",class_="class=ds-text-tight-s ds-font-regular ds-truncate ds-text-typo")
    
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    with open("cricket_scores.csv","a") as scores:
        scores.write(f'{team1},{over1},{score1},{team2},{over2},{score2},{result} {timestamp}\n')


async def generate_csv(channel):    
    async with aiofiles.open("cricket_scores.csv","rb") as file:
        await channel.send(file=discord.File(file,filename='cricket_scores.csv'))
