import time
try:
    import discord
except ImportError:
    print('Discord.py is not installed! Install it via "pip install discord.py" in the terminal\nthe script will automatically close in 5 seconds')
    time.sleep(5)
    raise SystemExit
from discord.ext import commands
try:
   import colorama
except ImportError:
    print('Colorama is not installed! Install it via "pip install colorama" in the terminal\nthe script will automatically close in 5 seconds')
    time.sleep(5)
    raise SystemExit
import os
from colorama import Fore, Style
import asyncio
# imports all the stuff you'll need

# enabling member intents:
intents = discord.Intents().default()
intents.members = True
client = discord.Client(intents=intents)

# disclaimer:
print(f"{Style.BRIGHT}DISCLAIMER:")
time.sleep(0.5)
print(f"{Style.RESET_ALL}User automation and spamming are {Fore.LIGHTYELLOW_EX}{Style.BRIGHT}against Discord's TOS!!{Style.RESET_ALL}{Fore.RESET}")
time.sleep(0.8)
print("Use this tool only for educational purposes and at your own risk")
time.sleep(0.8)
print("Ask the server owner if you're allowed to use this tool")
print(f'''{Fore.LIGHTGREEN_EX}{Style.BRIGHT}Mass Dm {Style.RESET_ALL}{Fore.RESET}will only work with a {Fore.LIGHTGREEN_EX}{Style.BRIGHT}Bot-Token{Style.RESET_ALL}{Fore.RESET} which has enabled{Style.BRIGHT}{Fore.GREEN} member intents{Style.RESET_ALL}{Fore.RESET}.
This does also count for {Style.BRIGHT}{Fore.LIGHTGREEN_EX}Mass Ban{Fore.RESET}{Style.RESET_ALL} (in the Nuke part of the code) and {Fore.LIGHTGREEN_EX}{Style.BRIGHT}Mass Nickname{Style.RESET_ALL}{Fore.RESET} (in the Raid part of the code).
{Fore.LIGHTGREEN_EX}{Style.BRIGHT}Mass Dm friends {Style.RESET_ALL}{Fore.RESET}will only work with a {Style.BRIGHT}{Fore.LIGHTGREEN_EX}Human-Token{Style.RESET_ALL}.
''')
time.sleep(0.8)

# poor booting animation:
print(f"{Style.BRIGHT}Booting {Fore.RED}长闩尺ㄩ爪闩 {Fore.RESET}Bot")
time.sleep(0.3)
print(f"{Fore.RED}25%")
time.sleep(0.5)
print(f"{Fore.YELLOW}50%")
time.sleep(0.6)
print(f"{Fore.LIGHTYELLOW_EX}75%")
time.sleep(0.7)
print(f"{Fore.LIGHTGREEN_EX}99%")
time.sleep(1)
print(f"{Fore.LIGHTBLUE_EX}长闩尺ㄩ爪闩 Bot booted")
time.sleep(1)

# setting bot to true or false:
chupapi = input('Are you using a Bot-Token(enter yes or no)?>> ')
if chupapi == "yes":
    munanyo = "BOT_TOKEN"
elif chupapi == "no":
    munanyo = "HUMAN_TOKEN"
while chupapi !="no" and chupapi != "yes":
    print(f'{Fore.RED}Invalid option😅\nPlease Enter yes or no')
    chupapi = input('Are you using a Bot-Token(enter yes or no)?>> ')
if chupapi == "yes":
    munanyo = "BOT_TOKEN"
elif chupapi == "no":
    munanyo = "HUMAN_TOKEN"

# getting the token:
token = input('Input Token>> ')


# main part of the code:
async def main():
    # mass dm part of the code:
    async def massdm():
        print(f'{Fore.LIGHTYELLOW_EX}------')
        if chupapi == "no":
            print(
                f"{Fore.RED}Mass Dm doesn\'t work with a Human-Token\nPress Enter to return to the main menu")
            await main()
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
                ahegao = input(f"{Fore.GREEN}What Should I Send?>>  ")
                for member in guild.members:
                    try:
                        await member.send(ahegao)
                        print(
                            f"{Fore.LIGHTGREEN_EX}[✅] Sent{Fore.WHITE} {ahegao} {Fore.LIGHTGREEN_EX}to {Fore.YELLOW}{member}")
                        await asyncio.sleep(0.1)
                    except Exception as e:
                        print(
                            f"{Fore.RED}[❌] Didn\'t send{Fore.WHITE} {ahegao} {Fore.RED}to {Fore.YELLOW}{member}{Fore.RED} - {e}")
        print(f'{Fore.LIGHTGREEN_EX}⚡All tasks completed⚡')
        input(f"\n{Fore.WHITE}Thanks for using {Fore.YELLOW}长闩尺ㄩ爪闩\nPress Enter to return to the main menu")
        await main()
    # embed mass dm friends part of the code:
    async def embedmassdmfriends():
        print(f'{Fore.LIGHTYELLOW_EX}------')
        if chupapi == "yes":
            print(
                f"{Fore.RED}Embed Mass Dm friends doesn\'t work with a Bot-Token\nPress Enter to return to the main menu")
            await main()
        else:
            pass
        print(f'{Fore.LIGHTYELLOW_EX}Embed Mass Dm friends was selected')
        print(f'{Fore.LIGHTYELLOW_EX}------')
        print('------')
        title = input(f"{Fore.LIGHTGREEN_EX}What Should Be The Title?>>  ")
        desc = input(f"{Fore.LIGHTGREEN_EX}What Should Be The Description(leave blank for none)?>>  ")
        thumb = input(f"{Fore.LIGHTGREEN_EX}What Should Be The Thumbnail(Enter the url and leave blank for none)?>>  ")
        img = input(f"{Fore.LIGHTGREEN_EX}What Should Be The Image(Enter the url and leave blank for none)?>>  ")
        footer = input(f"{Fore.LIGHTGREEN_EX}What Should Be The Footer(leave blank for none)?>>  ")
        footer_icon = input(
            f"{Fore.LIGHTGREEN_EX}What Should Be The Footer-Icon(Enter the url and leave blank for none)?>>  ")
        author = input(f"{Fore.LIGHTGREEN_EX}Who Should Be The Message Author(leave blank for none)?>>  ")
        icn = input(
            f"{Fore.LIGHTGREEN_EX}What Should Be The Message Author Icon(Enter the url leave blank for none)?>>  ")
        if title and desc and thumb and img and footer and footer_icon and author and icn is None:
            input(f"{Fore.RED}You can\'t set everything to none!\nPress Enter to return to the main menu")
            await main()
        else:
            pass
        karma = discord.Embed(
            title=f"{title}",
            description=f'{desc}',
            color=discord.Colour.purple())
        karma.set_thumbnail(url=f'{thumb}'),
        karma.set_image(url=f"{img}")
        karma.set_footer(text=f"{footer}", icon_url=f"{footer_icon}")
        karma.set_author(name=f"{author}", icon_url=f"{icn}")
        for user in client.user.friends:
            try:
                await user.send(embed=karma)
                print(f"{Fore.LIGHTGREEN_EX}[✅] Sent{Fore.WHITE} the embed {Fore.LIGHTGREEN_EX}to {Fore.YELLOW}{user}")
                await asyncio.sleep(0.1)
            except Exception as e:
                print(
                    f"{Fore.RED}[❌] Didn\'t send{Fore.WHITE} the embed {Fore.RED}to {Fore.YELLOW}{user}{Fore.RED} - {e}")
        print(f'{Fore.LIGHTGREEN_EX}⚡All tasks completed⚡')
        input(f"\n{Fore.WHITE}Thanks for using {Fore.YELLOW}长闩尺ㄩ爪闩\nPress Enter to return to the main menu")
        await main()
    # embed mass dm part of the code:
    async def embedmassdm():
        print(f'{Fore.LIGHTYELLOW_EX}------')
        if chupapi == "no":
            input(
                f"{Fore.RED}Embed Mass Dm doesn\'t work with a Human-Token\nPress Enter to return to the main menu")
            await main()
        else:
            pass
        print(f'{Fore.LIGHTYELLOW_EX}Embed Mass Dm was selected')
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
                hanime_tv = input(f"{Fore.LIGHTGREEN_EX}What Should Be The Title(leave blank for none)?>>  ")
                hentai = input(f"{Fore.LIGHTGREEN_EX}What Should Be The Description(leave blank for none)?>>  ")
                seggs = input(
                    f"{Fore.LIGHTGREEN_EX}What Should Be The Thumbnail(Enter the url and leave blank for none)?>>  ")
                incest = input(
                    f"{Fore.LIGHTGREEN_EX}What Should Be The Image(Enter the url and leave blank for none)?>>  ")
                knockknockknock = input(f"{Fore.LIGHTGREEN_EX}What Should Be The Footer(leave blank for none)?>>  ")
                fbi = input(
                    f"{Fore.LIGHTGREEN_EX}What Should Be The Footer-Icon(Enter the url and leave blank for none)?>>  ")
                opn = input(f"{Fore.LIGHTGREEN_EX}Who Should Be The Message Author(leave blank for none)?>>  ")
                up = input(
                    f"{Fore.LIGHTGREEN_EX}What Should Be The Message Author Icon(Enter the url leave blank for none)?>>  ")
                if hanime_tv and hentai and seggs and incest and knockknockknock and fbi and opn and up is None:
                    input(
                        f"{Fore.RED}You can\'t set everything to none!\nPress Enter to return to the main menu")
                    await main()
                else:
                    pass
                kamehameha = discord.Embed(
                    title=f"{hanime_tv}",
                    description=f'{hentai}',
                    color=discord.Colour.purple())
                kamehameha.set_thumbnail(url=f'{seggs}'),
                kamehameha.set_image(url=f"{incest}")
                kamehameha.set_footer(text=f"{knockknockknock}", icon_url=f"{fbi}")
                kamehameha.set_author(name=f"{opn}", icon_url=f"{up}")
                for member in guild.members:
                    try:
                        await member.send(embed=kamehameha)
                        print(
                            f"{Fore.LIGHTGREEN_EX}[✅] Sent{Fore.WHITE} the embed {Fore.LIGHTGREEN_EX}to {Fore.YELLOW}{member}")
                        await asyncio.sleep(0.1)
                    except Exception as e:
                        print(
                            f"{Fore.RED}[❌] Didn\'t send{Fore.WHITE} the embed {Fore.RED}to {Fore.YELLOW}{member}{Fore.RED} - {e}")
        print(f'{Fore.LIGHTGREEN_EX}⚡All tasks completed⚡')
        input(f"\n{Fore.WHITE}Thanks for using {Fore.YELLOW}长闩尺ㄩ爪闩\nPress Enter to return to the main menu")
        await main()
    # nuke part of the code:
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
                index = 0
                guildchannels = len(guild.channels)
                for channel in guild.channels:
                    try:
                        await channel.delete()
                        index += 1
                        print(
                            f"{Fore.LIGHTGREEN_EX}[✅] {index}/{guildchannels} [CHANNEL DELETED] {Fore.WHITE}{channel.name}{Fore.LIGHTGREEN_EX} in '{guild.name}'")
                        await asyncio.sleep(0.1)
                    except Exception as e:
                        print(
                            f"{Fore.RED}[❌] {index}/{guildchannels} [CHANNEL NOT DELETED] {Fore.WHITE}{channel.name}{Fore.RED} in '{guild.name}' - {e}")
                index = 0
                guildroles = len(guild.roles)
                for role in guild.roles:
                    try:
                        index += 1
                        await role.delete()
                        print(
                            f"{Fore.LIGHTGREEN_EX}[✅] {index}/{guildroles} [ROLE DELETED] {Fore.WHITE}{role.name}{Fore.LIGHTGREEN_EX} in '{guild.name}'")
                        await asyncio.sleep(0.1)
                    except Exception as e:
                        print(
                            f"{Fore.RED}[❌] {index}/{guildroles} [ROLE NOT DELETED] {Fore.WHITE}{role.name}{Fore.RED} in '{guild.name}' - {e}")
                index = 0
                guildmembers = len(guild.members)
                for member in guild.members:
                    try:
                        index += 1
                        await guild.ban(member, reason=ban_reason, delete_message_days=7)
                        print(
                            f"{Fore.LIGHTGREEN_EX}[✅] {index}/{guildmembers} [BANNED] {Fore.WHITE}{member}{Fore.LIGHTGREEN_EX} (ID: {member.id}) in '{guild.name}'")
                        await asyncio.sleep(0.1)
                    except Exception as e:
                        print(
                            f"{Fore.RED}[❌] {index}/{guildmembers} [BAN FAILED] {Fore.WHITE}{member}{Fore.RED} (ID: {member.id}) in '{guild.name}'- {e}")
                index = 0
                guildemojis = len(guild.emojis)
                for emoji in guild.emojis:
                    print(emoji)
                    try:
                        index += 1
                        await emoji.delete()
                        print(
                            f"{Fore.LIGHTGREEN_EX}[✅] {index}/{guildemojis} [EMOJI DELETED] {Fore.WHITE}{emoji.name}{Fore.LIGHTGREEN_EX} in '{guild.name}'")
                        await asyncio.sleep(0.1)
                    except Exception as e:
                        print(
                            f"{Fore.RED}[❌] {index}/{guildemojis} [EMOJI NOT DELETED] {Fore.WHITE}{emoji.name}{Fore.RED} in '{guild.name}' - {e}")
                index = 0
                guildinvites = len(guild.invites)
                for invite in guild.invites:
                    try:
                        index += 1
                        await invite.delete()
                        print(
                            f"{Fore.LIGHTGREEN_EX}[✅] {index}/{guildinvites} [INVITE DELETED] {Fore.WHITE}{invite}{Fore.LIGHTGREEN_EX} in '{guild.name}'")
                        await asyncio.sleep(0.1)
                    except Exception as e:
                        print(
                            f"{Fore.RED}[❌]  {index}/{guildinvites} [INVITE NOT DELETED] {Fore.WHITE}{invite}{Fore.RED} in '{guild.name}' - {e}")
        print(f'{Fore.LIGHTGREEN_EX}⚡All tasks completed⚡')
        input(f"\n{Fore.WHITE}Thanks for using {Fore.YELLOW}长闩尺ㄩ爪闩\nPress Enter to return to the main menu")
        await main()
    # exit part of the code:
    def exit():
        input(f"{Fore.WHITE}Thanks for using {Fore.YELLOW}长闩尺ㄩ爪闩\nPress Enter 5 times to close the program.")
        [input(i) for i in range(4, 0, -1)]
        raise SystemExit
    # raid part of the code:
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
                servername = input(f"{Fore.LIGHTGREEN_EX}Please enter a guild name>> ")
                role = input(f"{Fore.LIGHTGREEN_EX}Please enter a role name>> ")
                text_channel = input(f"{Fore.LIGHTGREEN_EX}Please enter a text channel name>> ")
                newnick = input(f"{Fore.LIGHTGREEN_EX}Please enter a kind nickname for all the members>> ")
                await guild.edit(name=servername)
                print(f"[✅]Renamed the guild to: {Fore.WHITE}{servername}")
                await guild.create_text_channel(text_channel)
                print(
                    f"{Fore.LIGHTGREEN_EX}[✅]Created a text channel:{Fore.WHITE} {text_channel}{Fore.LIGHTGREEN_EX} in {guild.name}")
                await asyncio.sleep(0.1)
                await guild.create_text_channel(text_channel)
                print(
                    f"{Fore.LIGHTGREEN_EX}[✅]Created a text channel:{Fore.WHITE} {text_channel}{Fore.LIGHTGREEN_EX} in {guild.name}")
                await asyncio.sleep(0.1)
                await guild.create_text_channel(text_channel)
                print(
                    f"{Fore.LIGHTGREEN_EX}[✅]Created a text channel:{Fore.WHITE} {text_channel}{Fore.LIGHTGREEN_EX} in {guild.name}")
                await asyncio.sleep(0.1)
                await guild.create_text_channel(text_channel)
                print(
                    f"{Fore.LIGHTGREEN_EX}[✅]Created a text channel:{Fore.WHITE} {text_channel}{Fore.LIGHTGREEN_EX} in {guild.name}")
                await asyncio.sleep(0.1)
                await guild.create_text_channel(text_channel)
                print(
                    f"{Fore.LIGHTGREEN_EX}[✅]Created a text channel:{Fore.WHITE} {text_channel}{Fore.LIGHTGREEN_EX} in {guild.name}")
                await asyncio.sleep(0.1)
                await guild.create_text_channel(text_channel)
                print(
                    f"{Fore.LIGHTGREEN_EX}[✅]Created a text channel:{Fore.WHITE} {text_channel}{Fore.LIGHTGREEN_EX} in {guild.name}")
                await asyncio.sleep(0.1)
                await guild.create_text_channel(text_channel)
                print(
                    f"{Fore.LIGHTGREEN_EX}[✅]Created a text channel:{Fore.WHITE} {text_channel}{Fore.LIGHTGREEN_EX} in {guild.name}")
                await asyncio.sleep(0.1)
                await guild.create_text_channel(text_channel)
                print(
                    f"{Fore.LIGHTGREEN_EX}[✅]Created a text channel:{Fore.WHITE} {text_channel}{Fore.LIGHTGREEN_EX} in {guild.name}")
                await asyncio.sleep(0.1)
                await guild.create_text_channel(text_channel)
                print(
                    f"{Fore.LIGHTGREEN_EX}[✅]Created a text channel:{Fore.WHITE} {text_channel}{Fore.LIGHTGREEN_EX} in {guild.name}")
                await asyncio.sleep(0.1)
                await guild.create_text_channel(text_channel)
                print(
                    f"{Fore.LIGHTGREEN_EX}[✅]Created a text channel:{Fore.WHITE} {text_channel}{Fore.LIGHTGREEN_EX} in {guild.name}")
                await asyncio.sleep(0.1)
                await guild.create_text_channel(text_channel)
                print(
                    f"{Fore.LIGHTGREEN_EX}[✅]Created a text channel:{Fore.WHITE} {text_channel}{Fore.LIGHTGREEN_EX} in {guild.name}")
                await asyncio.sleep(0.1)
                await guild.create_text_channel(text_channel)
                print(
                    f"{Fore.LIGHTGREEN_EX}[✅]Created a text channel:{Fore.WHITE} {text_channel}{Fore.LIGHTGREEN_EX} in {guild.name}")
                await asyncio.sleep(0.1)
                await guild.create_text_channel(text_channel)
                print(
                    f"{Fore.LIGHTGREEN_EX}[✅]Created a text channel:{Fore.WHITE} {text_channel}{Fore.LIGHTGREEN_EX} in {guild.name}")
                await asyncio.sleep(0.1)
                await guild.create_text_channel(text_channel)
                print(
                    f"{Fore.LIGHTGREEN_EX}[✅]Created a text channel:{Fore.WHITE} {text_channel}{Fore.LIGHTGREEN_EX} in {guild.name}")
                await asyncio.sleep(0.1)
                await guild.create_text_channel(text_channel)
                print(
                    f"{Fore.LIGHTGREEN_EX}[✅]Created a text channel:{Fore.WHITE} {text_channel}{Fore.LIGHTGREEN_EX} in {guild.name}")
                await asyncio.sleep(0.1)
                await guild.create_text_channel(text_channel)
                print(
                    f"{Fore.LIGHTGREEN_EX}[✅]Created a text channel:{Fore.WHITE} {text_channel}{Fore.LIGHTGREEN_EX} in {guild.name}")
                await asyncio.sleep(0.1)
                await guild.create_text_channel(text_channel)
                print(
                    f"{Fore.LIGHTGREEN_EX}[✅]Created a text channel:{Fore.WHITE} {text_channel}{Fore.LIGHTGREEN_EX} in {guild.name}")
                await asyncio.sleep(0.1)
                await guild.create_text_channel(text_channel)
                print(
                    f"{Fore.LIGHTGREEN_EX}[✅]Created a text channel:{Fore.WHITE} {text_channel}{Fore.LIGHTGREEN_EX} in {guild.name}")
                await asyncio.sleep(0.1)
                await guild.create_text_channel(text_channel)
                print(
                    f"{Fore.LIGHTGREEN_EX}[✅]Created a text channel:{Fore.WHITE} {text_channel}{Fore.LIGHTGREEN_EX} in {guild.name}")
                await asyncio.sleep(0.1)
                await guild.create_text_channel(text_channel)
                print(
                    f"{Fore.LIGHTGREEN_EX}[✅]Created a text channel:{Fore.WHITE} {text_channel}{Fore.LIGHTGREEN_EX} in {guild.name}")
                await asyncio.sleep(0.1)
                await guild.create_text_channel(text_channel)
                print(
                    f"{Fore.LIGHTGREEN_EX}[✅]Created a text channel: {Fore.WHITE}{text_channel}{Fore.LIGHTGREEN_EX} in {guild.name}")
                await asyncio.sleep(0.1)
                await guild.create_text_channel(text_channel)
                print(
                    f"{Fore.LIGHTGREEN_EX}[✅]Created a text channel: {Fore.WHITE}{text_channel}{Fore.LIGHTGREEN_EX} in {guild.name}")
                await asyncio.sleep(0.1)
                await guild.create_text_channel(text_channel)
                print(
                    f"{Fore.LIGHTGREEN_EX}[✅]Created a text channel: {Fore.WHITE}{text_channel}{Fore.LIGHTGREEN_EX} in {guild.name}")
                await asyncio.sleep(0.1)
                await guild.create_text_channel(text_channel)
                print(
                    f"{Fore.LIGHTGREEN_EX}[✅]Created a text channel: {Fore.WHITE}{text_channel}{Fore.LIGHTGREEN_EX} in {guild.name}")
                await asyncio.sleep(0.1)
                await guild.create_text_channel(text_channel)
                print(
                    f"{Fore.LIGHTGREEN_EX}[✅]Created a text channel: {Fore.WHITE}{text_channel}{Fore.LIGHTGREEN_EX} in {guild.name}")
                await asyncio.sleep(0.1)
                await guild.create_text_channel(text_channel)
                print(
                    f"{Fore.LIGHTGREEN_EX}[✅]Created a text channel: {Fore.WHITE}{text_channel}{Fore.LIGHTGREEN_EX} in {guild.name}")
                await asyncio.sleep(0.1)
                await guild.create_text_channel(text_channel)
                print(
                    f"{Fore.LIGHTGREEN_EX}[✅]Created a text channel: {Fore.WHITE}{text_channel}{Fore.LIGHTGREEN_EX} in {guild.name}")
                await asyncio.sleep(0.1)
                await guild.create_text_channel(text_channel)
                print(
                    f"{Fore.LIGHTGREEN_EX}[✅]Created a text channel: {Fore.WHITE}{text_channel}{Fore.LIGHTGREEN_EX} in {guild.name}")
                await asyncio.sleep(0.1)
                await guild.create_text_channel(text_channel)
                print(
                    f"{Fore.LIGHTGREEN_EX}[✅]Created a text channel: {Fore.WHITE}{text_channel}{Fore.LIGHTGREEN_EX} in {guild.name}")
                await asyncio.sleep(0.1)
                await guild.create_text_channel(text_channel)
                print(
                    f"{Fore.LIGHTGREEN_EX}[✅]Created a text channel: {Fore.WHITE}{text_channel}{Fore.LIGHTGREEN_EX} in {guild.name}")
                await asyncio.sleep(0.1)
                await guild.create_role(name=role)
                print(f"{Fore.LIGHTGREEN_EX}[✅]Created a role: {Fore.WHITE}{role}{Fore.LIGHTGREEN_EX} in {guild.name}")
                await asyncio.sleep(0.1)
                await guild.create_role(name=role)
                print(f"{Fore.LIGHTGREEN_EX}[✅]Created a role: {Fore.WHITE}{role}{Fore.LIGHTGREEN_EX} in {guild.name}")
                await asyncio.sleep(0.1)
                await guild.create_role(name=role)
                print(f"{Fore.LIGHTGREEN_EX}[✅]Created a role: {Fore.WHITE}{role}{Fore.LIGHTGREEN_EX} in {guild.name}")
                await asyncio.sleep(0.1)
                await guild.create_role(name=role)
                print(f"{Fore.LIGHTGREEN_EX}[✅]Created a role: {Fore.WHITE}{role}{Fore.LIGHTGREEN_EX} in {guild.name}")
                await asyncio.sleep(0.1)
                await guild.create_role(name=role)
                print(f"{Fore.LIGHTGREEN_EX}[✅]Created a role: {Fore.WHITE}{role}{Fore.LIGHTGREEN_EX} in {guild.name}")
                await asyncio.sleep(0.1)
                await guild.create_role(name=role)
                print(f"{Fore.LIGHTGREEN_EX}[✅]Created a role: {Fore.WHITE}{role} {Fore.LIGHTGREEN_EX}in {guild.name}")
                await asyncio.sleep(0.1)
                await guild.create_role(name=role)
                print(f"{Fore.LIGHTGREEN_EX}[✅]Created a role: {Fore.WHITE}{role}{Fore.LIGHTGREEN_EX} in {guild.name}")
                await asyncio.sleep(0.1)
                await guild.create_role(name=role)
                print(f"{Fore.LIGHTGREEN_EX}[✅]Created a role: {Fore.WHITE}{role} {Fore.LIGHTGREEN_EX}in {guild.name}")
                await asyncio.sleep(0.1)
                await guild.create_role(name=role)
                print(f"{Fore.LIGHTGREEN_EX}[✅]Created a role: {Fore.WHITE}{role}{Fore.LIGHTGREEN_EX} in {guild.name}")
                await asyncio.sleep(0.1)
                await guild.create_role(name=role)
                print(f"{Fore.LIGHTGREEN_EX}[✅]Created a role: {Fore.WHITE}{role}{Fore.LIGHTGREEN_EX} in {guild.name}")
                await asyncio.sleep(0.1)
                await guild.create_role(name=role)
                print(f"{Fore.LIGHTGREEN_EX}[✅]Created a role: {Fore.WHITE}{role}{Fore.LIGHTGREEN_EX} in {guild.name}")
                await asyncio.sleep(0.1)
                await guild.create_role(name=role)
                print(f"{Fore.LIGHTGREEN_EX}[✅]Created a role: {Fore.WHITE}{role}{Fore.LIGHTGREEN_EX} in {guild.name}")
                await asyncio.sleep(0.1)
                await guild.create_role(name=role)
                print(f"{Fore.LIGHTGREEN_EX}[✅]Created a role: {Fore.WHITE}{role}{Fore.LIGHTGREEN_EX} in {guild.name}")
                await asyncio.sleep(0.1)
                await guild.create_role(name=role)
                print(f"{Fore.LIGHTGREEN_EX}[✅]Created a role: {Fore.WHITE}{role}{Fore.LIGHTGREEN_EX} in {guild.name}")
                await asyncio.sleep(0.1)
                await guild.create_role(name=role)
                print(f"{Fore.LIGHTGREEN_EX}[✅]Created a role: {Fore.WHITE}{role}{Fore.LIGHTGREEN_EX} in {guild.name}")
                await asyncio.sleep(0.1)
                await guild.create_role(name=role)
                print(f"{Fore.LIGHTGREEN_EX}[✅]Created a role: {Fore.WHITE}{role}{Fore.LIGHTGREEN_EX} in {guild.name}")
                await asyncio.sleep(0.1)
                await guild.create_role(name=role)
                print(f"{Fore.LIGHTGREEN_EX}[✅]Created a role: {Fore.WHITE}{role}{Fore.LIGHTGREEN_EX} in {guild.name}")
                await asyncio.sleep(0.1)
                await guild.create_role(name=role)
                print(f"{Fore.LIGHTGREEN_EX}[✅]Created a role: {Fore.WHITE}{role}{Fore.LIGHTGREEN_EX} in {guild.name}")
                await asyncio.sleep(0.1)
                await guild.create_role(name=role)
                print(f"{Fore.LIGHTGREEN_EX}[✅]Created a role: {Fore.WHITE}{role}{Fore.LIGHTGREEN_EX} in {guild.name}")
                await asyncio.sleep(0.1)
                await guild.create_role(name=role)
                print(f"{Fore.LIGHTGREEN_EX}[✅]Created a role: {Fore.WHITE}{role}{Fore.LIGHTGREEN_EX} in {guild.name}")
                await asyncio.sleep(0.1)
                await guild.create_role(name=role)
                print(f"{Fore.LIGHTGREEN_EX}[✅]Created a role: {Fore.WHITE}{role}{Fore.LIGHTGREEN_EX} in {guild.name}")
                await asyncio.sleep(0.1)
                await guild.create_role(name=role)
                print(f"{Fore.LIGHTGREEN_EX}[✅]Created a role: {Fore.WHITE}{role}{Fore.LIGHTGREEN_EX} in {guild.name}")
                await asyncio.sleep(0.1)
                await guild.create_role(name=role)
                print(f"{Fore.LIGHTGREEN_EX}[✅]Created a role: {Fore.WHITE}{role}{Fore.LIGHTGREEN_EX} in {guild.name}")
                await asyncio.sleep(0.1)
                await guild.create_role(name=role)
                print(f"{Fore.LIGHTGREEN_EX}[✅]Created a role: {Fore.WHITE}{role}{Fore.LIGHTGREEN_EX} in {guild.name}")
                await asyncio.sleep(0.1)
                await guild.create_role(name=role)
                print(f"{Fore.LIGHTGREEN_EX}[✅]Created a role: {Fore.WHITE}{role}{Fore.LIGHTGREEN_EX} in {guild.name}")
                await asyncio.sleep(0.1)
                await guild.create_role(name=role)
                print(f"{Fore.LIGHTGREEN_EX}[✅]Created a role: {Fore.WHITE}{role}{Fore.LIGHTGREEN_EX} in {guild.name}")
                await asyncio.sleep(0.1)
                await guild.create_role(name=role)
                print(f"{Fore.LIGHTGREEN_EX}[✅]Created a role: {Fore.WHITE}{role}{Fore.LIGHTGREEN_EX} in {guild.name}")
                await asyncio.sleep(0.1)
                await guild.create_role(name=role)
                print(f"{Fore.LIGHTGREEN_EX}[✅]Created a role: {Fore.WHITE}{role}{Fore.LIGHTGREEN_EX} in {guild.name}")
                await asyncio.sleep(0.1)
                await guild.create_role(name=role)
                print(f"{Fore.LIGHTGREEN_EX}[✅]Created a role: {Fore.WHITE}{role}{Fore.LIGHTGREEN_EX} in {guild.name}")
                await asyncio.sleep(0.1)
                await guild.create_role(name=role)
                print(f"{Fore.LIGHTGREEN_EX}[✅]Created a role: {Fore.WHITE}{role}{Fore.LIGHTGREEN_EX} in {guild.name}")
                await asyncio.sleep(0.1)
                for user in guild.members:
                    try:
                        await user.edit(nick=newnick)
                        print(
                            f"{Fore.LIGHTGREEN_EX}[✅]Changed {Fore.WHITE}{user}\'s {Fore.LIGHTGREEN_EX}nickname in {guild.name} to: {Fore.WHITE}{newnick}")
                        await asyncio.sleep(0.1)
                    except Exception as e:
                        print(
                            f"{Fore.RED}[❌]Couldn\'t change {Fore.WHITE}{user}\'s{Fore.RED} nickname in {guild.name} to {Fore.WHITE}{newnick}{Fore.RED} - {e}")
        print(f'{Fore.LIGHTGREEN_EX}⚡All tasks completed⚡')
        input(f"\n{Fore.WHITE}Thanks for using {Fore.YELLOW}长闩尺ㄩ爪闩\nPress Enter to return to the main menu")
        await main()
    print(f'''
{Fore.BLUE}██{Fore.WHITE}╗ {Fore.BLUE} ██{Fore.WHITE}╗ {Fore.BLUE}█████{Fore.WHITE}╗ {Fore.BLUE}██████{Fore.WHITE}╗ {Fore.BLUE}██{Fore.WHITE}╗   {Fore.BLUE}██{Fore.WHITE}╗{Fore.BLUE}███{Fore.WHITE}╗   {Fore.BLUE}███{Fore.WHITE}╗ {Fore.BLUE}█████{Fore.WHITE}╗
{Fore.BLUE}██{Fore.WHITE}║ {Fore.BLUE}██{Fore.WHITE}╔╝{Fore.BLUE}██{Fore.WHITE}╔══{Fore.BLUE}██{Fore.WHITE}╗{Fore.BLUE}██{Fore.WHITE}╔══{Fore.BLUE}██{Fore.WHITE}╗{Fore.BLUE}██{Fore.WHITE}║   {Fore.BLUE}██{Fore.WHITE}║{Fore.BLUE}████{Fore.WHITE}╗ {Fore.BLUE}████{Fore.WHITE}║{Fore.BLUE}██{Fore.WHITE}╔══{Fore.BLUE}██{Fore.WHITE}╗
{Fore.BLUE}█████{Fore.WHITE}═╝ {Fore.BLUE}███████{Fore.WHITE}║{Fore.BLUE}██████{Fore.WHITE}╔╝{Fore.BLUE}██{Fore.WHITE}║   {Fore.BLUE}██{Fore.WHITE}║{Fore.BLUE}██{Fore.WHITE}╔{Fore.BLUE}████{Fore.WHITE}╔{Fore.BLUE}██{Fore.WHITE}║{Fore.BLUE}███████{Fore.WHITE}║
{Fore.BLUE}██{Fore.WHITE}╔═{Fore.BLUE}██{Fore.WHITE}╗ {Fore.BLUE}██{Fore.WHITE}╔══{Fore.BLUE}██{Fore.WHITE}║{Fore.BLUE}██{Fore.WHITE}╔══{Fore.BLUE}██{Fore.WHITE}╗{Fore.BLUE}██{Fore.WHITE}║   {Fore.BLUE}██{Fore.WHITE}║{Fore.BLUE}██{Fore.WHITE}║╚{Fore.BLUE}██{Fore.WHITE}╔╝{Fore.BLUE}██{Fore.WHITE}║{Fore.BLUE}██{Fore.WHITE}╔══{Fore.BLUE}██{Fore.WHITE}║
{Fore.BLUE}██{Fore.WHITE}║ ╚{Fore.BLUE}██{Fore.WHITE}╗{Fore.BLUE}██{Fore.WHITE}║  {Fore.BLUE}██{Fore.WHITE}║{Fore.BLUE}██{Fore.WHITE}║  {Fore.BLUE}██{Fore.WHITE}║╚{Fore.BLUE}██████{Fore.WHITE}╔╝{Fore.BLUE}██{Fore.WHITE}║ ╚═╝ {Fore.BLUE}██{Fore.WHITE}║{Fore.BLUE}██{Fore.WHITE}║  {Fore.BLUE}██{Fore.WHITE}║
{Fore.WHITE}╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝
{Fore.WHITE}                                   Made by {Fore.YELLOW}hoemotion 
{Fore.WHITE}Check out the github page for updates: {Fore.LIGHTBLUE_EX}https://github.com/hoemotion/Karuma/           
{Fore.LIGHTGREEN_EX}Logged in as {Fore.YELLOW}"{client.user}" {Fore.LIGHTGREEN_EX}(ID:{Fore.YELLOW} {client.user.id}{Fore.LIGHTGREEN_EX})
[1] Mass Dm friends | [2] Mass Embed Dm friends | [3] Nuke
[4] Raid            | [5] Mass Dm               | [6] Mass Embed Dm
[7] Exit Script
''')
    select = input(f"{Fore.LIGHTGREEN_EX}Select>> ")
    if select == '1': # mass dm friends part of the code:
        print(f'{Fore.LIGHTYELLOW_EX}------')
        if chupapi == "yes":
            print("Mass Dm friends does only work with a Human-Token\nPress Enter to return to the main menu")
            await main()
        else:
            pass
        overflow = input(f"Mass Dm friends was selected\n{Fore.LIGHTGREEN_EX}What Should I Send?>> ")
        print(f'{Fore.LIGHTYELLOW_EX}------')
        for user in client.user.friends:
            try:
                await user.send(f"{overflow}")
                print(f"{Fore.LIGHTGREEN_EX}[✅] Sent{Fore.WHITE} {overflow} {Fore.LIGHTGREEN_EX}to {Fore.YELLOW}{user}")
                await asyncio.sleep(0.1)
            except Exception as e:
                print(f"{Fore.RED}[❌] Didn\'t send{Fore.WHITE} {overflow} {Fore.RED}to {Fore.YELLOW}{user}{Fore.RED} - {e}")
        print(f'{Fore.LIGHTGREEN_EX}⚡All tasks completed⚡')
        input(f"\n{Fore.WHITE}Thanks for using {Fore.YELLOW}长闩尺ㄩ爪闩\nPress Enter to return to the main menu")
        await main()
    elif select == '3':
        await Nuke() # runs the nuke part of the code
    elif select == '7':
        await exit() # runs the exit part of the code
    elif select == '4':
        await raid() # runs the raid part of the code
    elif select == '5':
        await massdm() # runs the mass dm part of the code
    elif select == '6':
        await embedmassdm() # runs the embed mass dm part of the code
    elif select == '2':
        await embedmassdmfriends() # runs the embed mass dm friends part of the code
    else:
        print("Invalid option😅\nPress Enter to return to the main menu")
        await main()

# on ready event:
@client.event
async def on_ready():
    await main()

if munanyo == "HUMAN_TOKEN":
    client.run(token, bot=False) # runs the human-token if human-token was selected
elif munanyo == "BOT_TOKEN":
    client.run(token, bot=True) # runs the bot-token if bot-token was selected

# the end
