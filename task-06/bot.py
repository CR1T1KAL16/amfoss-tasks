import discord
from scraper import scrape_livescore
import os


intents = discord.Intents.default()
client = discord.Client(intents=intents)
@client.event
async def ready():
    print(f'{client.user} hath been summoned')

@client.event
async def on_message(message):
    if message.content.startswith('!livescore'):
        scrape_livescore()
        with open('cricket_scores.csv', 'r') as file:
            last_row = file.readlines()[-1]
        team1, over1, score1, team2, over2, score2, result, timestamp = last_row.split(',')
        response = f'Team 1: {team1} {over1} {score1}\nTeam 2: {team2} {over2} {score2} \n {result} \n {timestamp}'
        
        # Send the response message
        await message.channel.send(response)

    elif message.content.startswith('!generate'):
        # Send the CSV data as a message to the user
        # file=scrape_livescore()
        
        # csv_file=discord.File(file,filename="cricket_scores.csv")
        # await message.channel.send(file=csv_file)
        with open('cricket_scores.csv', 'r') as file:
            csv_contents = file.read()
            
            # Check if the file is not None
            if csv_contents:
                # Send the CSV file
                csv_file = discord.File('cricket_scores.csv')
                await message.channel.send(file=csv_file)
            else:
                await message.channel.send('Error generating the CSV file.')
        
    elif message.content.startswith('!help'):
        # Send the list of commands and their description
        response = 'Commands:\n!livescore - Get the live feed on the crux of the match.\n!generate - Get the CSV file that contains the list of all the live scores that have been fetched (along with the timestamp).\n!help - Get a list of the commands along with their description.'
        await message.channel.send(response)



           
client.run('MTE0ODg4NDA2NDkyNTkyOTQ3Mw.GkxIBD.Ww7INrUxKQOPGn-6MDSNXYKr3oGls77e6cO9zs')
