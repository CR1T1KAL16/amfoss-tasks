import discord
import csv
from scraper import scrape_livescore
import datetime

intents = discord.Intents.default()
intents.message_content = True
intents.members = True  
intents.presences = True 

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} hath been summoned')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!livescore'):
        first,over,score,second,result= scrape_livescore()
        response = f" {first}{over}{score}\n{second}\n{result}"
        await message.channel.send(response)
        
        current_date = datetime.datetime.now()
        date_string = current_date.strftime('%Y-%m-%d')
        await message.channel.send(f'{date_string}')
    if message.content.startswith('!help'):
        await message.channel.send('Commands:\n!csv - get the csv file the livescores are stored in\n!livescore - get the live scores')

    if message.content.startswith('!csv'):
        first,over,score,second,result= scrape_livescore()
        with open('cricket_scores.csv', 'a', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow([first,over,score,second,result])

           
client.run('MTE0ODg4NDA2NDkyNTkyOTQ3Mw.GkxIBD.Ww7INrUxKQOPGn-6MDSNXYKr3oGls77e6cO9zs')
