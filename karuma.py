#!/usr/bin/python
# -*- coding: UTF-8 -*-
import subprocess
try:
    from os import system, name
    import sys, os, json, random, time, asyncio, pyfade, discord
    from datetime import datetime
    from discord.ext import commands
    from colorama import Fore, init, Style;init()
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", '-r' , 'requirements.txt'])
    from os import system, name
    import sys, os, json, random, time, asyncio, pyfade, discord
    from datetime import datetime
    from discord.ext import commands
    from colorama import Fore, init, Style;init()

sys.tracebacklimit = 0
intents = discord.Intents().default()
intents.members = True
client = discord.Client(intents=intents)
setup = json.load(open(f"./config.json", "r"))
minimum_dm, maximum_dm, bot, token, boot, disclaimer, min_ban, max_ban, min_general, max_general = setup["minimum_dm_delay"], setup["maximum_dm_delay"], setup["bot"], setup["token"], setup["skip_booting"], setup["skip_disclaimer"], setup["minimum_ban_delay"], setup["maximum_ban_delay"], setup["minimum_general_delay"], setup["maximum_general_delay"]

def random_cooldown(minimum, maximum):
    cooldown = random.randint(minimum*100000,maximum*100000) / 100000
    return cooldown


to_print_disclaimer = [f"{Fore.LIGHTWHITE_EX}{Style.BRIGHT}DISCLAIMER:",
                       f"{Style.RESET_ALL}{Fore.LIGHTWHITE_EX}User automation and spamming are {Fore.LIGHTYELLOW_EX}{Style.BRIGHT}against Discord's TOS!!{Style.RESET_ALL}{Fore.RESET}",
                       f"{Fore.LIGHTWHITE_EX}Use this tool only for educational purposes and at your own risk",
                       f"{Fore.LIGHTWHITE_EX}Ask the server owner if you're allowed to use this tool",
                       f'''{Fore.LIGHTGREEN_EX}{Style.BRIGHT}Mass Dm {Style.RESET_ALL}{Fore.RESET}{Fore.LIGHTWHITE_EX}will only work with a {Fore.LIGHTGREEN_EX}{Style.BRIGHT}Bot-Token{Style.RESET_ALL}{Fore.RESET}{Fore.LIGHTWHITE_EX} which has enabled{Style.BRIGHT}{Fore.LIGHTGREEN_EX} member intents{Style.RESET_ALL}{Fore.RESET}{Fore.LIGHTWHITE_EX}.
                        This does also count for {Style.BRIGHT}{Fore.LIGHTGREEN_EX}Mass Ban{Fore.RESET}{Style.RESET_ALL}{Fore.LIGHTWHITE_EX} (in the Nuke part of the code) and {Fore.LIGHTGREEN_EX}{Style.BRIGHT}Mass Nickname{Style.RESET_ALL}{Fore.RESET}{Fore.LIGHTWHITE_EX} (in the Raid part of the code).
                        {Fore.LIGHTGREEN_EX}{Style.BRIGHT}Mass Dm friends {Style.RESET_ALL}{Fore.RESET}{Fore.LIGHTWHITE_EX}will only work with a {Style.BRIGHT}{Fore.LIGHTGREEN_EX}Human-Token{Style.RESET_ALL}{Fore.LIGHTWHITE_EX}.
                        ''']
if not disclaimer:
    for index, item in enumerate(to_print_disclaimer):
        to_sleep = {
            0: 0.5,
            1: 0.8,
            2: 0.8,
            3: 0,
            4: 0.8,
        }
        print(item)
        time.sleep(to_sleep[index])

boot_anim = [f"{Style.BRIGHT}{Fore.LIGHTWHITE_EX}Booting {Fore.RED}长闩尺ㄩ爪闩 {Fore.RESET}{Fore.LIGHTWHITE_EX}Bot",
             f"{Fore.RED}25%",
             f"{Fore.YELLOW}50%",
             f"{Fore.LIGHTYELLOW_EX}75%",
             f"{Fore.LIGHTGREEN_EX}99%",
             f"{Fore.LIGHTBLUE_EX}长闩尺ㄩ爪闩 Bot booted"]
if not boot:
    for index, item in enumerate(boot_anim):
        wait_dict = {
            0: 0.3,
            1: 0.5,
            2: 0.6,
            3: 0.7,
            4: 1,
            5: 1,
        }
        print(item)
        time.sleep(wait_dict[index])

async def massdm():
        print(f'{Fore.LIGHTYELLOW_EX}------')
        if not bot:
            input(
                f"{Fore.RED}Mass Dm doesn\'t work with a Human-Token\nPress Enter to return to the main menu")
            os.system('cls' if os.name == 'nt' else 'clear')
            return await main()
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
                membercount = len(guild.members)
                index = 0
                for member in guild.members:
                    cooldown = random_cooldown(minimum_dm, maximum_dm)
                    index += 1
                    try:
                        await member.send(ahegao)
                        print(
                            f"{Fore.LIGHTGREEN_EX}[✅] {index}/{membercount} Sent{Fore.WHITE} {ahegao} {Fore.LIGHTGREEN_EX}to {Fore.YELLOW}{member}")
                        await asyncio.sleep(cooldown)
                    except Exception as e:
                        print(
                            f"{Fore.RED}[❌] {index}/{membercount} Didn\'t send{Fore.WHITE} {ahegao} {Fore.RED}to {Fore.YELLOW}{member}{Fore.RED} - {e}")
        print(f'{Fore.LIGHTGREEN_EX}⚡All tasks completed⚡')
        input(f"\n{Fore.WHITE}Thanks for using {Fore.YELLOW}长闩尺ㄩ爪闩\nPress Enter to return to the main menu")
        return await main()
async def embedmassdmfriends():
        print(f'{Fore.LIGHTYELLOW_EX}------')
        if bot:
            input(
                f"{Fore.RED}Embed Mass Dm friends doesn\'t work with a Bot-Token\nPress Enter to return to the main menu")
            os.system('cls' if os.name == 'nt' else 'clear')
            return await main()
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
        karma = discord.Embed(
            title=f"{title}",
            description=f'{desc}',
            color=discord.Colour.purple())
        karma.set_thumbnail(url=f'{thumb}'),
        karma.set_image(url=f"{img}")
        karma.set_footer(text=f"{footer}", icon_url=f"{footer_icon}")
        karma.set_author(name=f"{author}", icon_url=f"{icn}")
        friendcounter = len(client.user.friends)
        index = 0
        for user in client.user.friends:
            cooldown = random_cooldown(minimum_dm, maximum_dm)
            index += 1
            try:
                await user.send(embed=karma)
                print(f"{Fore.LIGHTGREEN_EX}[✅] {index}/{friendcounter} Sent{Fore.WHITE} the embed {Fore.LIGHTGREEN_EX}to {Fore.YELLOW}{user}")
                await asyncio.sleep(cooldown)
            except Exception as e:
                print(
                    f"{Fore.RED}[❌] {index}/{friendcounter} Didn\'t send{Fore.WHITE} the embed {Fore.RED}to {Fore.YELLOW}{user}{Fore.RED} - {e}")
        print(f'{Fore.LIGHTGREEN_EX}⚡All tasks completed⚡')
        input(f"\n{Fore.WHITE}Thanks for using {Fore.YELLOW}长闩尺ㄩ爪闩\nPress Enter to return to the main menu")
        os.system('cls' if os.name == 'nt' else 'clear')
        return await main()

async def embedmassdm():
        print(f'{Fore.LIGHTYELLOW_EX}------')
        if not bot:
            input(
                f"{Fore.RED}Embed Mass Dm doesn\'t work with a Human-Token\nPress Enter to return to the main menu")
            os.system('cls' if os.name == 'nt' else 'clear')
            await main()
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
                kamehameha = discord.Embed(
                    title=f"{hanime_tv}",
                    description=f'{hentai}',
                    color=discord.Colour.purple())
                kamehameha.set_thumbnail(url=f'{seggs}'),
                kamehameha.set_image(url=f"{incest}")
                kamehameha.set_footer(text=f"{knockknockknock}", icon_url=f"{fbi}")
                kamehameha.set_author(name=f"{opn}", icon_url=f"{up}")
                membercount = len(guild.members)
                index = 0
                for member in guild.members:
                    cooldown = random_cooldown(minimum_dm, maximum_dm)
                    index += 1
                    try:
                        await member.send(embed=kamehameha)
                        print(
                            f"{Fore.LIGHTGREEN_EX}[✅] {index}/{membercount} Sent{Fore.WHITE} the embed {Fore.LIGHTGREEN_EX}to {Fore.YELLOW}{member}")
                        await asyncio.sleep(cooldown)
                    except Exception as e:
                        print(
                            f"{Fore.RED}[❌] {index}/{membercount} Didn\'t send{Fore.WHITE} the embed {Fore.RED}to {Fore.YELLOW}{member}{Fore.RED} - {e}")
        print(f'{Fore.LIGHTGREEN_EX}⚡All tasks completed⚡')
        input(f"\n{Fore.WHITE}Thanks for using {Fore.YELLOW}长闩尺ㄩ爪闩\nPress Enter to return to the main menu")
        os.system('cls' if os.name == 'nt' else 'clear')
        return await main()

async def embedmassdm():
        print(f'{Fore.LIGHTYELLOW_EX}------')
        if not bot:
            input(
                f"{Fore.RED}Embed Mass Dm doesn\'t work with a Human-Token\nPress Enter to return to the main menu")
            os.system('cls' if os.name == 'nt' else 'clear')
            await main()
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
                    return await main()
                kamehameha = discord.Embed(
                    title=f"{hanime_tv}",
                    description=f'{hentai}',
                    color=discord.Colour.purple())
                kamehameha.set_thumbnail(url=f'{seggs}'),
                kamehameha.set_image(url=f"{incest}")
                kamehameha.set_footer(text=f"{knockknockknock}", icon_url=f"{fbi}")
                kamehameha.set_author(name=f"{opn}", icon_url=f"{up}")
                membercount = len(guild.members)
                index = 0
                for member in guild.members:
                    cooldown = random_cooldown(minimum_dm, maximum_dm)
                    index += 1
                    try:
                        await member.send(embed=kamehameha)
                        print(
                            f"{Fore.LIGHTGREEN_EX}[✅] {index}/{membercount} Sent{Fore.WHITE} the embed {Fore.LIGHTGREEN_EX}to {Fore.YELLOW}{member}")
                        await asyncio.sleep(cooldown)
                    except Exception as e:
                        print(
                            f"{Fore.RED}[❌] {index}/{membercount} Didn\'t send{Fore.WHITE} the embed {Fore.RED}to {Fore.YELLOW}{member}{Fore.RED} - {e}")
        print(f'{Fore.LIGHTGREEN_EX}⚡All tasks completed⚡')
        input(f"\n{Fore.WHITE}Thanks for using {Fore.YELLOW}长闩尺ㄩ爪闩\nPress Enter to return to the main menu")
        os.system('cls' if os.name == 'nt' else 'clear')
        return await main()

async def Nuke():
        print(f'{Fore.LIGHTYELLOW_EX}------')
        print('Nuke was selected')
        if not bot:
            print(f"{Fore.RED}Mass Ban will not work with a Human-Token")
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
                    cooldown = random_cooldown(min_general, max_general)
                    index += 1
                    try:
                        await channel.delete()
                        print(
                            f"{Fore.LIGHTGREEN_EX}[✅] {index}/{guildchannels} [CHANNEL DELETED] {Fore.WHITE}{channel.name}{Fore.LIGHTGREEN_EX} in '{guild.name}'")
                        await asyncio.sleep(cooldown)
                    except Exception as e:
                        print(
                            f"{Fore.RED}[❌] {index}/{guildchannels} [CHANNEL NOT DELETED] {Fore.WHITE}{channel.name}{Fore.RED} in '{guild.name}' - {e}")
                index = 0
                guildroles = len(guild.roles)
                for role in guild.roles:
                    cooldown = random_cooldown(min_general, max_general)
                    index += 1
                    try:
                        await role.delete()
                        print(
                            f"{Fore.LIGHTGREEN_EX}[✅] {index}/{guildroles} [ROLE DELETED] {Fore.WHITE}{role.name}{Fore.LIGHTGREEN_EX} in '{guild.name}'")
                        await asyncio.sleep(cooldown)
                    except Exception as e:
                        print(
                            f"{Fore.RED}[❌] {index}/{guildroles} [ROLE NOT DELETED] {Fore.WHITE}{role.name}{Fore.RED} in '{guild.name}' - {e}")
                index = 0
                guildmembers = len(guild.members)
                for member in guild.members:
                    cooldown = random_cooldown(min_ban, max_ban)
                    index += 1
                    try:
                        await guild.ban(member, reason=ban_reason, delete_message_days=7)
                        print(
                            f"{Fore.LIGHTGREEN_EX}[✅] {index}/{guildmembers} [BANNED] {Fore.WHITE}{member}{Fore.LIGHTGREEN_EX} (ID: {member.id}) in '{guild.name}'")
                        await asyncio.sleep(cooldown)
                    except Exception as e:
                        print(
                            f"{Fore.RED}[❌] {index}/{guildmembers} [BAN FAILED] {Fore.WHITE}{member}{Fore.RED} (ID: {member.id}) in '{guild.name}'- {e}")
                index = 0
                guildemojis = len(guild.emojis)
                for emoji in guild.emojis:
                    cooldown = random_cooldown(min_general, max_general)
                    index += 1
                    print(emoji)
                    try:
                        await emoji.delete()
                        print(
                            f"{Fore.LIGHTGREEN_EX}[✅] {index}/{guildemojis} [EMOJI DELETED] {Fore.WHITE}{emoji.name}{Fore.LIGHTGREEN_EX} in '{guild.name}'")
                        await asyncio.sleep(cooldown)
                    except Exception as e:
                        print(
                            f"{Fore.RED}[❌] {index}/{guildemojis} [EMOJI NOT DELETED] {Fore.WHITE}{emoji.name}{Fore.RED} in '{guild.name}' - {e}")
        print(f'{Fore.LIGHTGREEN_EX}⚡All tasks completed⚡')
        input(f"\n{Fore.WHITE}Thanks for using {Fore.YELLOW}长闩尺ㄩ爪闩\nPress Enter to return to the main menu")
        os.system('cls' if os.name == 'nt' else 'clear')
        return await main()


async def server_id_displayer():
        index = 0
        for guild in client.guilds:
            if bot:
                try:
                    if len(await guild.invites()) != 0:
                        senpai = 0
                        for invite in await guild.invites():
                            while senpai < 1:
                                INVITE = f" | Serverinvite: {invite}"
                                senpai += 1
                    else:
                        for channel in guild.channels:
                            if channel.position == 1:
                                try:
                                    INVITE = f" | Serverinvite: {await channel.create_invite()}"
                                except:
                                    INVITE = f" | Serverinvite: {Fore.RED}Couldn\'t fetch an Invite"
                except:
                    INVITE = f" | Serverinvite: {Fore.RED}Couldn\'t fetch an Invite"
            else:
                INVITE = ""
            index += 1
            print(
                f"{Fore.LIGHTGREEN_EX}[{index}/{len(client.guilds)}] {Fore.YELLOW}{guild.name}{Fore.LIGHTGREEN_EX} - {Fore.YELLOW}{guild.id}{Fore.LIGHTGREEN_EX} | Total members: {Fore.YELLOW}{len(guild.members)}{Fore.LIGHTGREEN_EX}{INVITE}")
        print(f'{Fore.LIGHTGREEN_EX}⚡All tasks completed⚡')
        input(f"\n{Fore.WHITE}Thanks for using {Fore.YELLOW}长闩尺ㄩ爪闩\nPress Enter to return to the main menu")
        os.system('cls' if os.name == 'nt' else 'clear')
        return await main()
async def embed_dm_all_client_users():
        users = len(client.users)
        index = 0
        print(f'{Fore.LIGHTYELLOW_EX}------')
        if not bot:
            input(
                f"{Fore.RED}Embed Mass Dm doesn\'t work with a Human-Token\nPress Enter to return to the main menu")
            os.system('cls' if os.name == 'nt' else 'clear')
            await main()
        print(f'{Fore.LIGHTYELLOW_EX}Embed Mass Dm Client Users was selected')
        print(f'{Fore.LIGHTYELLOW_EX}------')
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
            return await main()
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
                cooldown = random_cooldown(minimum_dm, maximum_dm)
                index += 1
                try:
                    await user.send(embed=kamehameha)
                    print(
                        f"{Fore.LIGHTGREEN_EX}[✅] {index}/{usercount} Sent{Fore.WHITE} the embed {Fore.LIGHTGREEN_EX}to {Fore.YELLOW}{user}")
                    await asyncio.sleep(cooldown)
                except Exception as e:
                    print(
                        f"{Fore.RED}[❌] {index}/{usercount} Didn\'t send{Fore.WHITE} the embed {Fore.RED}to {Fore.YELLOW}{user}{Fore.RED} - {e}")
        print(f'{Fore.LIGHTGREEN_EX}⚡All tasks completed⚡')
        input(f"\n{Fore.WHITE}Thanks for using {Fore.YELLOW}长闩尺ㄩ爪闩\nPress Enter to return to the main menu")
        os.system('cls' if os.name == 'nt' else 'clear')
        return await main()
async def dm_all_client_users():
        users = len(client.users)
        index = 0
        print(f'{Fore.LIGHTYELLOW_EX}------')
        if not bot:
            input(
                f"{Fore.RED}Mass Dm Client Users doesn\'t work with a Human-Token\nPress Enter to return to the main menu")
            os.system('cls' if os.name == 'nt' else 'clear')
            return await main()
        print(f'{Fore.LIGHTYELLOW_EX}Embed Mass Dm Client Users was selected')
        print(f'{Fore.LIGHTYELLOW_EX}------')
        yamete_kudasai = input(f"{Fore.LIGHTGREEN_EX}What Should I Send?>> ")
        usercount = len(client.users)
        index = 0
        for user in client.users:
                cooldown = random_cooldown(minimum_dm, maximum_dm)
                index += 1
                try:
                    await user.send(yamete_kudasai)
                    print(
                        f"{Fore.LIGHTGREEN_EX}[✅] {index}/{usercount} Sent{Fore.WHITE} {yamete_kudasai} {Fore.LIGHTGREEN_EX}to {Fore.YELLOW}{user}")
                    await asyncio.sleep(cooldown)
                except Exception as e:
                    print(
                        f"{Fore.RED}[❌] {index}/{usercount} Didn\'t send{Fore.WHITE} the embed {Fore.RED}to {Fore.YELLOW}{user}{Fore.RED} - {e}")
        print(f'{Fore.LIGHTGREEN_EX}⚡All tasks completed⚡')
        input(f"\n{Fore.WHITE}Thanks for using {Fore.YELLOW}长闩尺ㄩ爪闩\nPress Enter to return to the main menu")
        os.system('cls' if os.name == 'nt' else 'clear')
        return await main()

async def guild_leaver():
        last_question = input(f"{Fore.LIGHTYELLOW_EX}Are you sure that you want to leave every guild(enter yes or no)?>> ")
        while last_question.lower() not in ["yes", "no"] :
            print(f'{Fore.RED}Invalid option😅\nPlease Enter yes or no')
            last_question = input(f"{Fore.LIGHTYELLOW_EX}Are you sure that you want to leave every guild(enter yes or no)?>> ")
        if last_question == "yes":
            guild_counter = len(client.guilds)
            index = 0
            for guild in client.guilds:
                index +=1
                try:
                    await guild.leave()
                    print(f"{Fore.LIGHTGREEN_EX}[{index}/{guild_counter}] Left {Fore.YELLOW}{guild.name}")
                except Exception as e:
                    print(f"{Fore.RED}[{index}/{guild_counter}] Couldn\'t leave {Fore.YELLOW}{guild.name}{Fore.RED} - {e}")
            input("nPress Enter to return to the main menu")
        elif last_question == "no":
            input("Phew...\nPress Enter to return to the main menu")
        os.system('cls' if os.name == 'nt' else 'clear')
        return await main()
async def exit():
        await client.close()
        input(f"{Fore.WHITE}Thanks for using {Fore.YELLOW}长闩尺ㄩ爪闩\nPress Enter 5 times to close the program.")
        [input(i) for i in range(4, 0, -1)]
        raise SystemExit
async def raid():
        print(f'{Fore.LIGHTYELLOW_EX}------')
        print('Raid was selected')
        if not bot:
            print(f"{Fore.RED}Mass Nickname does only work with a Bot-Token")
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
                role_ammount = int(input(f"{Fore.LIGHTGREEN_EX}Please enter how many Roles should be created>> "))
                text_channel = input(f"{Fore.LIGHTGREEN_EX}Please enter a text channel name>> ")
                channel_ammount = int(input(f"{Fore.LIGHTGREEN_EX}Please enter how many text channels should be created>> "))
                newnick = input(f"{Fore.LIGHTGREEN_EX}Please enter a kind nickname for all the members>> ")
                if servername == "":
                    servername = guild.name
                try:
                   await guild.edit(name=servername)
                   print(f"[✅]Renamed the guild to: {Fore.WHITE}{servername}")
                except Exception as e:
                    print(e)
                for i in range(channel_ammount):
                   cooldown = random_cooldown(min_general, max_general)
                   try:
                       await guild.create_text_channel(text_channel)
                       print(f"{Fore.LIGHTGREEN_EX}[✅] {i+1}/{channel_ammount} Created a text channel: {Fore.WHITE}{text_channel}{Fore.LIGHTGREEN_EX} in {guild.name}")
                       await asyncio.sleep(cooldown)
                   except Exception as e:
                       print(e)
                for i in range(role_ammount):
                    cooldown = random_cooldown(min_general, max_general)
                    try:
                        await guild.create_role(name=role)
                        print(f"{Fore.LIGHTGREEN_EX}[✅] {i+1}/{role_ammount} Created a role: {Fore.WHITE}{role}{Fore.LIGHTGREEN_EX} in {guild.name}")
                        await asyncio.sleep(cooldown)
                    except Exception as e:
                        print(e)
                usercount = len(guild.members)
                count = 0
                for user in guild.members:
                    cooldown = random_cooldown(min_general, max_general)
                    count += 1
                    if not client.user.id == user.id:
                      try:
                          await user.edit(nick=newnick)
                          print(
                            f"{Fore.LIGHTGREEN_EX}[✅] {count}/{usercount} Changed {Fore.WHITE}{user}\'s {Fore.LIGHTGREEN_EX}nickname in {guild.name} to: {Fore.WHITE}{newnick}")
                          await asyncio.sleep(cooldown)
                      except Exception as e:
                          print(
                            f"{Fore.RED}[❌] {count}/{usercount} Couldn\'t change {Fore.WHITE}{user}\'s{Fore.RED} nickname in {guild.name} to {Fore.WHITE}{newnick}{Fore.RED} - {e}")
        print(f'{Fore.LIGHTGREEN_EX}⚡All tasks completed⚡')
        input(f"\n{Fore.WHITE}Thanks for using {Fore.YELLOW}长闩尺ㄩ爪闩\nPress Enter to return to the main menu")
        os.system('cls' if os.name == 'nt' else 'clear')
        return await main()

async def mdmfriends():
        print(f'{Fore.LIGHTYELLOW_EX}------')
        if bot:
            input("Mass Dm friends does only work with a Human-Token\nPress Enter to return to the main menu")
            os.system('cls' if os.name == 'nt' else 'clear')
            return await main()
        overflow = input(f"Mass Dm friends was selected\n{Fore.LIGHTGREEN_EX}What Should I Send?>> ")
        print(f'{Fore.LIGHTYELLOW_EX}------')
        friendcounter = len(client.user.friends)
        index = 0
        for user in client.user.friends:
            cooldown = random_cooldown(minimum_dm, maximum_dm)
            index += 1
            try:
                await user.send(f"{overflow}")
                print(f"{Fore.LIGHTGREEN_EX}[✅] {index}/{friendcounter} Sent{Fore.WHITE} {overflow} {Fore.LIGHTGREEN_EX}to {Fore.YELLOW}{user}")
                await asyncio.sleep(cooldown)
            except Exception as e:
                print(f"{Fore.RED}[❌] {index}/{friendcounter} Didn\'t send{Fore.WHITE} {overflow} {Fore.RED}to {Fore.YELLOW}{user}{Fore.RED} - {e}")
        print(f'{Fore.LIGHTGREEN_EX}⚡All tasks completed⚡')
        input(f"\n{Fore.WHITE}Thanks for using {Fore.YELLOW}长闩尺ㄩ爪闩\nPress Enter to return to the main menu")
        os.system('cls' if os.name == 'nt' else 'clear')
        return await main()

async def give_admin():
    print(f'{Fore.LIGHTYELLOW_EX}------')
    print('Give Admin to @everyone was selected')
    while True:
        try:
            server_id = int(input(f'{Fore.LIGHTYELLOW_EX}Enter the server ID: '))
            break
        except ValueError:
            print(f'{Fore.RED}Invalid option😅')
            continue
    for guild in client.guilds:
        if guild.id == server_id:
            print('Discord server "{}" was selected as a target...'.format(guild.name))
            print('------')
            try:
                permissions = guild.default_role.permissions
                permissions(kick_members=True)
                await guild.default_role.edit(permissions=permissions)
                print(f"{Fore.LIGHTGREEN_EX}[✅] 1/4 Gave{Fore.WHITE} @everyone {Fore.LIGHTGREEN_EX}perms for {Fore.YELLOW}KICKING USERS")
            except Exception as e:
                print(f"{Fore.RED}[❌] 1/4 {e}")
            try:
                permissions = guild.default_role.permissions
                permissions.update(ban_members=True)
                await guild.default_role.edit(permissions=permissions)
                print(f"{Fore.LIGHTGREEN_EX}[✅] 2/4 Gave{Fore.WHITE} @everyone {Fore.LIGHTGREEN_EX}perms for {Fore.YELLOW}BANNING USERS")
            except Exception as e:
                print(f"{Fore.RED}[❌] 2/4 {e}")
            try:
                permissions = guild.default_role.permissions
                permissions.update(administrator=True)
                await guild.default_role.edit(permissions=permissions)
                print(f"{Fore.LIGHTGREEN_EX}[✅] 3/4 Gave{Fore.WHITE} @everyone {Fore.LIGHTGREEN_EX}perms for {Fore.YELLOW}ADMINISTRATION")
            except Exception as e:
                print(f"{Fore.RED}[❌] 3/4 {e}")
            try:
                permissions = guild.default_role.permissions
                permissions.update(mention_everyone=True)
                await guild.default_role.edit(permissions=permissions)
                print(f"{Fore.LIGHTGREEN_EX}[✅] 4/4 Gave{Fore.WHITE} @everyone {Fore.LIGHTGREEN_EX}perms for {Fore.YELLOW}MENTIONING @everyone")
            except Exception as e:
                print(f"{Fore.RED}[❌] 4/4 {e}")
    print(f'{Fore.LIGHTGREEN_EX}⚡All tasks completed⚡')
    input(f"\n{Fore.WHITE}Thanks for using {Fore.YELLOW}长闩尺ㄩ爪闩\nPress Enter to return to the main menu")
    os.system('cls' if os.name == 'nt' else 'clear')
    return await main()


async def main():
    if not bot:
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
[0] Nuke
[1] Raid                | [2] Mass Dm Client Users  | [3] Mass Embed Dm Client Users
[4] Leave all Servers   | [5] Mass Dm               | [6] Mass Embed Dm
[7] Display all Servers | [8] Mass Dm friends       | [9] Mass Embed Dm friends
[10] Give Admin to @everyone
[11] Unban every banned Member
[quit] Exit Script
''')
    select = input(f"{Fore.LIGHTGREEN_EX}Select>> ").lower()
    if select == '8':
        await mdmfriends()

    elif select == '0':
        await Nuke()
    elif select == 'quit':
        await exit()
    elif select == '1':
        await raid() 
    elif select == '5':
        await massdm()
    elif select == '6':
        await embedmassdm()
    elif select == '9':
        await embedmassdmfriends()
    elif select == '7':
        await server_id_displayer()
    elif select == '4':
        await guild_leaver()
    elif select == '3':
        await embed_dm_all_client_users()
    elif select == '2':
        await dm_all_client_users()
    elif select == '10':
        await give_admin()
    else:
        input(f"{Fore.RED}Invalid option😅\nPress Enter to return to the main menu")
        os.system('cls' if os.name == 'nt' else 'clear')
        return await main()

def start():
    @client.event
    async def on_ready():
        await client.change_presence(status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.watching, name="github.com/hoemotion"))
        os.system('cls' if os.name == 'nt' else 'clear')
        return await main()


start()
try:
    client.run(token, bot=bot)
except Exception as e:
    if "improper token" in str(e).lower():
        print("THe discord token is incorrect please edit config.json and try again")
    else:
        print(e)
