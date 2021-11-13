import time, sys, os, subprocess, asyncio, json # modules in the standard library

sys.tracebacklimit = 0
try:
    import discord, colorama, pyfade
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'discord.py'])
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'colorama'])
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'pyfade'])

import discord, pyfade
from colorama import Fore, init, Style
# module imports

init() # required for some windows users

# member intents:
intents = discord.Intents().default()
intents.members = True
client = discord.Client(intents=intents)

# disclaimer:
print(f"{Fore.LIGHTWHITE_EX}{Style.BRIGHT}DISCLAIMER:")
time.sleep(0.5)
print(f"{Style.RESET_ALL}{Fore.LIGHTWHITE_EX}User automation and spamming are {Fore.LIGHTYELLOW_EX}{Style.BRIGHT}against Discord's TOS!!{Style.RESET_ALL}{Fore.RESET}")
time.sleep(0.8)
print(f"{Fore.LIGHTWHITE_EX}Use this tool only for educational purposes and at your own risk")
time.sleep(0.8)
print(f"{Fore.LIGHTWHITE_EX}Ask the server owner if you're allowed to use this tool")
print(f'''{Fore.LIGHTGREEN_EX}{Style.BRIGHT}Mass Dm {Style.RESET_ALL}{Fore.RESET}{Fore.LIGHTWHITE_EX}will only work with a {Fore.LIGHTGREEN_EX}{Style.BRIGHT}Bot-Token{Style.RESET_ALL}{Fore.RESET}{Fore.LIGHTWHITE_EX} which has enabled{Style.BRIGHT}{Fore.LIGHTGREEN_EX} member intents{Style.RESET_ALL}{Fore.RESET}{Fore.LIGHTWHITE_EX}.
This does also count for {Style.BRIGHT}{Fore.LIGHTGREEN_EX}Mass Ban{Fore.RESET}{Style.RESET_ALL}{Fore.LIGHTWHITE_EX} (in the Nuke part of the code) and {Fore.LIGHTGREEN_EX}{Style.BRIGHT}Mass Nickname{Style.RESET_ALL}{Fore.RESET}{Fore.LIGHTWHITE_EX} (in the Raid part of the code).
{Fore.LIGHTGREEN_EX}{Style.BRIGHT}Mass Dm friends {Style.RESET_ALL}{Fore.RESET}{Fore.LIGHTWHITE_EX}will only work with a {Style.BRIGHT}{Fore.LIGHTGREEN_EX}Human-Token{Style.RESET_ALL}{Fore.LIGHTWHITE_EX}.
''')


def forceinput(prompt: str, *options: str) -> str:
    i = input(prompt)
    while i not in options:
        print(f"{Fore.RED}Invalid option!\nPlease enter: {options}\n")
        i = input(prompt)

    return i


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def getguild():
    while True:
        try:
            guild_id = int(input('Enter the server ID\n> '))
            break
        except ValueError:
            print(f'{Fore.RED}ID Must be a Number!')

        guild = client.get_guild(guild_id)
        if guild is None:
            print(f"Guild ID \"{guild_id}\" not found!")
        
        return guild

# obtain token:
token_type = "bot" if forceinput(
    f'{Fore.LIGHTWHITE_EX}Are you using a Bot token? (yes/no)\n> ', 'yes', 'no') == "yes" else "human"
token = input(pyfade.Fade.Horizontal(
     pyfade.Colors.col, f"Enter your token\n> "))

# main
async def main():
    # mass dm part of the code:
    async def massdm():
        print(f'{Fore.LIGHTYELLOW_EX}------')
        if token_type == "human":
            input(
                f"{Fore.RED}Mass Dm doesn't work with a Human-Token\nPress Enter to return to the main menu")
            return
        print(f'{Fore.LIGHTYELLOW_EX}Mass Dm selected')
        guild = getguild()
        
        membercount = len(guild.members)
        print(
            f'Server: {guild} | ID: {guild_id} | Members: {membercount}')
        print('------')
        message = input(f"{Fore.GREEN}Enter message to DM\n> ")
        for index, member in enumerate(guild.members):
            try:
                await member.send(message)
                print(
                    f"{Fore.LIGHTGREEN_EX}[✅] {index}/{membercount} Sent{Fore.WHITE} {message} {Fore.LIGHTGREEN_EX}to {Fore.YELLOW}{member}")
                await asyncio.sleep(0.1)
            except Exception as e:
                print(
                    f"{Fore.RED}[❌] {index}/{membercount} Didn\'t send{Fore.WHITE} {message} {Fore.RED}to {Fore.YELLOW}{member}{Fore.RED} - {e}")
        print(f'{Fore.LIGHTGREEN_EX}⚡All tasks completed⚡')
        input(
            f"\nPress Enter to return to the main menu")
        return

    async def embedmassdmfriends():
        print(f'{Fore.LIGHTYELLOW_EX}------')
        if token_type == "bot":
            input(
                f"{Fore.RED}Embed Mass Dm friends doesn\'t work with a Bot-Token\nPress Enter to return to the main menu")
            return
        print(f'{Fore.LIGHTYELLOW_EX}Embed Mass Dm friends was selected')
        print(f'{Fore.LIGHTYELLOW_EX}------')
        print('------')
        title = input(f"{Fore.LIGHTGREEN_EX}What Should Be The Title?>>  ")
        desc = input(
            f"{Fore.LIGHTGREEN_EX}What Should Be The Description(leave blank for none)?>>  ")
        thumb = input(
            f"{Fore.LIGHTGREEN_EX}What Should Be The Thumbnail(Enter the url and leave blank for none)?>>  ")
        img = input(
            f"{Fore.LIGHTGREEN_EX}What Should Be The Image(Enter the url and leave blank for none)?>>  ")
        footer = input(
            f"{Fore.LIGHTGREEN_EX}What Should Be The Footer(leave blank for none)?>>  ")
        footer_icon = input(
            f"{Fore.LIGHTGREEN_EX}What Should Be The Footer-Icon(Enter the url and leave blank for none)?>>  ")
        author = input(
            f"{Fore.LIGHTGREEN_EX}Who Should Be The Message Author(leave blank for none)?>>  ")
        icn = input(
            f"{Fore.LIGHTGREEN_EX}What Should Be The Message Author Icon(Enter the url leave blank for none)?>>  ")
        if title and desc and thumb and img and footer and footer_icon and author and icn is None:
            input(
                f"{Fore.RED}You can\'t set everything to none!\nPress Enter to return to the main menu")
            return
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
        friendcounter = len(client.user.friends)
        for index, user in enumerate(client.user.friends):
            try:
                await user.send(embed=karma)
                print(
                    f"{Fore.LIGHTGREEN_EX}[✅] {index}/{friendcounter} Sent{Fore.WHITE} the embed {Fore.LIGHTGREEN_EX}to {Fore.YELLOW}{user}")
                await asyncio.sleep(0.1)
            except Exception as e:
                print(
                    f"{Fore.RED}[❌] {index}/{friendcounter} Didn\'t send{Fore.WHITE} the embed {Fore.RED}to {Fore.YELLOW}{user}{Fore.RED} - {e}")
        print(f'{Fore.LIGHTGREEN_EX}⚡All tasks completed⚡')
        input(
            f"\nPress Enter to return to the main menu")
        clear()
        return
    # embed mass dm part of the code:

    async def embedmassdm():
        print(f'{Fore.LIGHTYELLOW_EX}------')
        if token_type == "human":
            input(
                f"{Fore.RED}Embed Mass Dm doesn\'t work with a Human-Token\nPress Enter to return to the main menu")
            return
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
                print(
                    'Discord server "{}" was selected as a target...'.format(guild.name))
                print('------')
                hanime_tv = input(
                    f"{Fore.LIGHTGREEN_EX}What Should Be The Title(leave blank for none)?>>  ")
                hentai = input(
                    f"{Fore.LIGHTGREEN_EX}What Should Be The Description(leave blank for none)?>>  ")
                seggs = input(
                    f"{Fore.LIGHTGREEN_EX}What Should Be The Thumbnail(Enter the url and leave blank for none)?>>  ")
                incest = input(
                    f"{Fore.LIGHTGREEN_EX}What Should Be The Image(Enter the url and leave blank for none)?>>  ")
                knockknockknock = input(
                    f"{Fore.LIGHTGREEN_EX}What Should Be The Footer(leave blank for none)?>>  ")
                fbi = input(
                    f"{Fore.LIGHTGREEN_EX}What Should Be The Footer-Icon(Enter the url and leave blank for none)?>>  ")
                opn = input(
                    f"{Fore.LIGHTGREEN_EX}Who Should Be The Message Author(leave blank for none)?>>  ")
                up = input(
                    f"{Fore.LIGHTGREEN_EX}What Should Be The Message Author Icon(Enter the url leave blank for none)?>>  ")
                if hanime_tv and hentai and seggs and incest and knockknockknock and fbi and opn and up is None:
                    input(
                        f"{Fore.RED}You can\'t set everything to none!\nPress Enter to return to the main menu")
                    return
                else:
                    pass
                kamehameha = discord.Embed(
                    title=f"{hanime_tv}",
                    description=f'{hentai}',
                    color=discord.Colour.purple())
                kamehameha.set_thumbnail(url=f'{seggs}'),
                kamehameha.set_image(url=f"{incest}")
                kamehameha.set_footer(
                    text=f"{knockknockknock}", icon_url=f"{fbi}")
                kamehameha.set_author(name=f"{opn}", icon_url=f"{up}")
                membercount = len(guild.members)
                index = 0
                for member in guild.members:
                    index += 1
                    try:
                        await member.send(embed=kamehameha)
                        print(
                            f"{Fore.LIGHTGREEN_EX}[✅] {index}/{membercount} Sent{Fore.WHITE} the embed {Fore.LIGHTGREEN_EX}to {Fore.YELLOW}{member}")
                        await asyncio.sleep(0.1)
                    except Exception as e:
                        print(
                            f"{Fore.RED}[❌] {index}/{membercount} Didn\'t send{Fore.WHITE} the embed {Fore.RED}to {Fore.YELLOW}{member}{Fore.RED} - {e}")
        print(f'{Fore.LIGHTGREEN_EX}⚡All tasks completed⚡')
        input(
            f"\nPress Enter to return to the main menu")
        clear()
        return
    # nuke part of the code:

    async def Nuke():
        print(f'{Fore.LIGHTYELLOW_EX}------')
        print('Nuke was selected')
        if token_type == "human":
            print(f"{Fore.RED}Mass Ban will not work with a Human-Token")
        else:
            pass
        while True:
            try:
                server_id = int(
                    input(f'{Fore.LIGHTYELLOW_EX}Enter the server ID: '))
                break
            except ValueError:
                print(f'{Fore.RED}Invalid option😅')
                continue
        print(f'{Fore.LIGHTYELLOW_EX}------')
        for guild in client.guilds:
            if guild.id == server_id:
                print(
                    'Discord server "{}" was selected as a target...'.format(guild.name))
                print('------')
                print(
                    'Before we start, is there a ban reason? (Leave blank for no reason)')
                ban_reason = input('Enter ban reason: ')
                print('------')
                index = 0
                guildinvites = len(await guild.invites())
                for invite in await guild.invites():
                    index += 1
                    try:
                        await invite.delete()
                        print(
                            f"{Fore.LIGHTGREEN_EX}[✅] {index}/{guildinvites} [INVITE DELETED] {Fore.WHITE}{invite}{Fore.LIGHTGREEN_EX} in '{guild.name}'")
                    except Exception as e:
                        print(
                            f"{Fore.RED}[❌]  {index}/{guildinvites} [INVITE NOT DELETED] {Fore.WHITE}{invite}{Fore.RED} in '{guild.name}' - {e}")
                index = 0
                guildchannels = len(guild.channels)
                for channel in guild.channels:
                    index += 1
                    try:
                        await channel.delete()
                        print(
                            f"{Fore.LIGHTGREEN_EX}[✅] {index}/{guildchannels} [CHANNEL DELETED] {Fore.WHITE}{channel.name}{Fore.LIGHTGREEN_EX} in '{guild.name}'")
                        await asyncio.sleep(0.1)
                    except Exception as e:
                        print(
                            f"{Fore.RED}[❌] {index}/{guildchannels} [CHANNEL NOT DELETED] {Fore.WHITE}{channel.name}{Fore.RED} in '{guild.name}' - {e}")
                index = 0
                guildroles = len(guild.roles)
                for role in guild.roles:
                    index += 1
                    try:
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
                    index += 1
                    try:
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
                    index += 1
                    print(emoji)
                    try:
                        await emoji.delete()
                        print(
                            f"{Fore.LIGHTGREEN_EX}[✅] {index}/{guildemojis} [EMOJI DELETED] {Fore.WHITE}{emoji.name}{Fore.LIGHTGREEN_EX} in '{guild.name}'")
                        await asyncio.sleep(0.1)
                    except Exception as e:
                        print(
                            f"{Fore.RED}[❌] {index}/{guildemojis} [EMOJI NOT DELETED] {Fore.WHITE}{emoji.name}{Fore.RED} in '{guild.name}' - {e}")
        print(f'{Fore.LIGHTGREEN_EX}⚡All tasks completed⚡')
        input(
            f"\nPress Enter to return to the main menu")
        clear()
        return

    async def embed_dm_all_client_users():
        users = len(client.users)
        index = 0
        print(f'{Fore.LIGHTYELLOW_EX}------')
        if token_type == "human":
            input(
                f"{Fore.RED}Embed Mass Dm doesn\'t work with a Human-Token\nPress Enter to return to the main menu")
            clear()
            return
        else:
            pass
        print(f'{Fore.LIGHTYELLOW_EX}Embed Mass Dm Client Users was selected')
        print(f'{Fore.LIGHTYELLOW_EX}------')
        for user in client.users:
            hanime_tv = input(
                f"{Fore.LIGHTGREEN_EX}What Should Be The Title(leave blank for none)?>>  ")
            hentai = input(
                f"{Fore.LIGHTGREEN_EX}What Should Be The Description(leave blank for none)?>>  ")
            seggs = input(
                f"{Fore.LIGHTGREEN_EX}What Should Be The Thumbnail(Enter the url and leave blank for none)?>>  ")
            incest = input(
                f"{Fore.LIGHTGREEN_EX}What Should Be The Image(Enter the url and leave blank for none)?>>  ")
            knockknockknock = input(
                f"{Fore.LIGHTGREEN_EX}What Should Be The Footer(leave blank for none)?>>  ")
            fbi = input(
                f"{Fore.LIGHTGREEN_EX}What Should Be The Footer-Icon(Enter the url and leave blank for none)?>>  ")
            opn = input(
                f"{Fore.LIGHTGREEN_EX}Who Should Be The Message Author(leave blank for none)?>>  ")
            up = input(
                f"{Fore.LIGHTGREEN_EX}What Should Be The Message Author Icon(Enter the url leave blank for none)?>>  ")
            if hanime_tv and hentai and seggs and incest and knockknockknock and fbi and opn and up is None:
                input(
                    f"{Fore.RED}You can\'t set everything to none!\nPress Enter to return to the main menu")
                return
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
            usercount = len(client.users)
            index = 0
            for user in client.users:
                index += 1
                try:
                    await user.send(embed=kamehameha)
                    print(
                        f"{Fore.LIGHTGREEN_EX}[✅] {index}/{usercount} Sent{Fore.WHITE} the embed {Fore.LIGHTGREEN_EX}to {Fore.YELLOW}{user}")
                    await asyncio.sleep(0.1)
                except Exception as e:
                    print(
                        f"{Fore.RED}[❌] {index}/{usercount} Didn\'t send{Fore.WHITE} the embed {Fore.RED}to {Fore.YELLOW}{user}{Fore.RED} - {e}")
        print(f'{Fore.LIGHTGREEN_EX}⚡All tasks completed⚡')
        input(
            f"\nPress Enter to return to the main menu")
        clear()

    if token_type == "human":
        Connected = f"Guild Counter: {len(client.guilds)} | Friend Counter {len(client.user.friends)}"
    else:
        Connected = f"Guild Counter: {len(client.guilds)} | User Counter: {len(client.users)}"
    print(pyfade.Fade.Horizontal(pyfade.Colors.yellow_to_red, '''
██╗  ██╗ █████╗ ██████╗ ██╗   ██╗███╗   ███╗ █████╗ 
██║ ██╔╝██╔══██╗██╔══██╗██║   ██║████╗ ████║██╔══██╗
█████═╝ ███████║██████╔╝██║   ██║██╔████╔██║███████║
██╔═██╗ ██╔══██║██╔══██╗██║   ██║██║╚██╔╝██║██╔══██║
██║ ╚██╗██║  ██║██║  ██║╚██████╔╝██║ ╚═╝ ██║██║  ██║
╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝
'''))
    print(f'''
{Fore.LIGHTWHITE_EX}                                   Made by {Fore.YELLOW}hoemotion 
{Fore.LIGHTWHITE_EX}Check out the github page for updates: {Fore.LIGHTBLUE_EX}https://github.com/hoemotion/Karuma/           
{Fore.LIGHTGREEN_EX}Logged in as {Fore.YELLOW}"{client.user}" {Fore.LIGHTGREEN_EX}(ID:{Fore.YELLOW} {client.user.id}{Fore.LIGHTGREEN_EX})
{Connected}
[1] Nuke                 | [2] Raid                  | [3] Mass Dm Client Users
[4] Mass Embed Dm        | [5] Mass Embed Dm friends | [6] Mass Embed Dm Client Users 
[7] Mass Dm              | [8] Mass Dm Friends       | [9] Leave all Servers
[10] Display all Servers | [11] Exit
''')
    option = input(f"{Fore.LIGHTGREEN_EX}Select>> ")
    if option == '1':
        await Nuke()
    elif option == '2': # raid
        print(f'{Fore.LIGHTYELLOW_EX}------')
        print('Raid was selected')
        guild = getguild()
        print(
            f'Discord server {guild.name} was selected as a target...')
        print('------')
        servername = input(
            f"{Fore.LIGHTGREEN_EX}Please enter a guild name>> ")
        role = input(
            f"{Fore.LIGHTGREEN_EX}Please enter a role name>> ")
        role_amount = int(
            input(f"{Fore.LIGHTGREEN_EX}Please enter how many Roles should be created>> "))
        text_channel = input(
            f"{Fore.LIGHTGREEN_EX}Please enter a text channel name>> ")
        channel_amount = int(input(
            f"{Fore.LIGHTGREEN_EX}Please enter how many text channels should be created>> "))
        if token_type == "bot":
            newnick = input(
            f"{Fore.LIGHTGREEN_EX}Please enter a kind nickname for all the members>> ")
        if servername:
            await guild.edit(name=servername)
            print(f"[✅]Renamed the guild to: {Fore.WHITE}{servername}")

        for index in range(channel_amount):
            await guild.create_text_channel(text_channel)
            print(
                f"{Fore.LIGHTGREEN_EX}[✅] {index}/{channel_amount} Created a text channel: {Fore.WHITE}{text_channel}{Fore.LIGHTGREEN_EX}")
            await asyncio.sleep(0.1)

        for index in range(role_amount):
            await guild.create_role(name=role)
            print(
                f"{Fore.LIGHTGREEN_EX}[✅] {index}/{role_amount} Created role: {Fore.WHITE}{role}{Fore.LIGHTGREEN_EX}")
            await asyncio.sleep(0.1)
        usercount = len(guild.members)
        if token_type == "bot":
            for index, member in enumerate(guild.members):
                try:
                    await member.edit(nick=newnick)
                    print(
                        f"{Fore.LIGHTGREEN_EX}[✅] {index}/{usercount} Changed {Fore.WHITE}{member}\'s {Fore.LIGHTGREEN_EX}nickname to: {Fore.WHITE}{newnick}")
                    await asyncio.sleep(0.1)
                except Exception as e:
                    print(
                        f"{Fore.RED}[❌] {index}/{usercount} Couldn't change {Fore.WHITE}{member}\'s{Fore.RED} nickname to {Fore.WHITE}{newnick}{Fore.RED} - {e}")
        print(f'{Fore.LIGHTGREEN_EX}⚡All tasks completed⚡')
        input(
            f"\nPress Enter to return to the main menu")
            
        return
    elif option == '3': # mass dm client users
        print(f'{Fore.LIGHTYELLOW_EX}------')
        if token_type == "human":
            input(
                f"{Fore.RED}Mass Dm Client Users doesn't work with a Human-Token\nPress Enter to return to the main menu")
            return
        print(f'{Fore.LIGHTYELLOW_EX}Mass Dm Client Users was selected')
        print(f'{Fore.LIGHTYELLOW_EX}------')
        message = input(f"{Fore.GREEN}Enter message to DM\n> ")
        usercount = len(client.users)
        for index, user in enumerate(client.users):
            try:
                await user.send(message)
                print(
                    f"{Fore.LIGHTGREEN_EX}[✅] {index}/{usercount} Sent{Fore.WHITE} {message} {Fore.LIGHTGREEN_EX}to {Fore.YELLOW}{user}")
                await asyncio.sleep(0.1)
            except Exception as e:
                print(
                    f"{Fore.RED}[❌] {index}/{usercount} Didn't send{Fore.WHITE} {Fore.RED}to {Fore.YELLOW}{user}{Fore.RED} - {e}")
        print(f'{Fore.LIGHTGREEN_EX}⚡All tasks completed⚡')
        input(
            f"\nPress Enter to return to the main menu")
        return
    elif option == '4':
        await embedmassdm()
    elif option == '5':
        await embedmassdmfriends()
    elif option == '6':
        await embed_dm_all_client_users()
    elif option == '7':
        await massdm()
    elif option == '8':  # mass dm friends
        print(f'{Fore.LIGHTYELLOW_EX}------')
        if token_type == "bot":
            input(
                "Mass Dm friends does only work with a Human-Token\nPress Enter to return to the main menu")
            return
        else:
            pass
        overflow = input(
            f"Mass Dm friends was selected\n{Fore.LIGHTGREEN_EX}What Should I Send?>> ")
        print(f'{Fore.LIGHTYELLOW_EX}------')
        friendcounter = len(client.user.friends)
        for index, user in enumerate(client.user.friends):
            try:
                await user.send(f"{overflow}")
                print(
                    f"{Fore.LIGHTGREEN_EX}[✅] {index}/{friendcounter} Sent{Fore.WHITE} {overflow} {Fore.LIGHTGREEN_EX}to {Fore.YELLOW}{user}")
                await asyncio.sleep(0.1)
            except Exception as e:
                print(
                    f"{Fore.RED}[❌] {index}/{friendcounter} Didn\'t send{Fore.WHITE} {overflow} {Fore.RED}to {Fore.YELLOW}{user}{Fore.RED} - {e}")
        print(f'{Fore.LIGHTGREEN_EX}⚡All tasks completed⚡')
        input(f"Press Enter to return to the main menu")

    elif option == '9': # leave all servers
        if forceinput(
            f"{Fore.LIGHTYELLOW_EX}Are you sure that you want to leave all servers? (yes/no)\n> ", "yes", "no") == "yes":
            guild_counter = len(client.guilds)
            for index, guild in enumerate(client.guilds):
                try:
                    await guild.leave()
                    print(
                        f"{Fore.LIGHTGREEN_EX}[{index}/{guild_counter}] Left {Fore.YELLOW}{guild.name}")
                except Exception as e:
                    print(
                        f"{Fore.RED}[{index}/{guild_counter}] Couldn't leave {Fore.YELLOW}{guild.name}{Fore.RED} - {e}")

        else:
            input("Operation cancelled\nPress Enter to return to the main menu")
            return

    elif option == '10': # server id displayer
        for guild in client.guilds:
            invite = ""
            if token_type == "bot":
                invites = await guild.invites()
                if invites:
                    invite = f" | Serverinvite: {invites[0]}"
                else:
                    for channel in guild.channels:
                        if channel.position == 1:
                            try:
                                INVITE = f" | Serverinvite: {await channel.create_invite()}"
                                break
                            except:
                                pass
            if not invite:
                invite = f" | Serverinvite: {Fore.RED}Couldn't fetch an Invite"
            print(
                f"{Fore.LIGHTGREEN_EX}[{index}/{len(client.guilds)}] {Fore.YELLOW}{guild.name}{Fore.LIGHTGREEN_EX} - {Fore.YELLOW}{guild.id}{Fore.LIGHTGREEN_EX} | Total members: {Fore.YELLOW}{len(guild.members)}{Fore.LIGHTGREEN_EX}{INVITE}")
        print(f'{Fore.LIGHTGREEN_EX}⚡All tasks completed⚡')
        input(
            f"\nPress Enter to return to the main menu")
        return

    elif option == '11':
        await client.close()
        print(f"{Fore.WHITE}Thank you for using {Fore.YELLOW}长闩尺ㄩ爪闩")
        sys.exit()

    else:
        input(f"{Fore.RED}Invalid option\nPress Enter to return to the main menu")

def start():
    @client.event
    async def on_ready():
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="github.com/hoemotion"))
        await client.change_presence(status=discord.Status.idle)
        clear()
        while True:
            await main()

start()

if token_type == "human":
    client.run(token, bot=False)
elif token_type == "bot":
    client.run(token)