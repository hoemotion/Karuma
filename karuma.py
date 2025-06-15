#!/usr/bin/python
# -*- coding: UTF-8 -*-
import subprocess
try:
    from os import system, name
    import sys, os, json, random, time, asyncio, pyfade, discord
    from datetime import datetime
    from discord.ext import commands
    from colorama import Fore, init, Style; init()
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", '-r', 'requirements.txt'])
    from os import system, name
    import sys, os, json, random, time, asyncio, pyfade, discord
    from datetime import datetime
    from discord.ext import commands
    from colorama import Fore, init, Style; init()

sys.tracebacklimit = 0

class Config:
    def __init__(self):
        self.load_config()
        
    def load_config(self):
        try:
            with open("./config.json", "r") as f:
                config = json.load(f)
                self.minimum_dm = config.get("minimum_dm_delay", 1)
                self.maximum_dm = config.get("maximum_dm_delay", 3)
                self.token = config.get("token", "")
                self.skip_booting = config.get("skip_booting", False)
                self.skip_disclaimer = config.get("skip_disclaimer", False)
                self.min_ban = config.get("minimum_ban_delay", 1)
                self.max_ban = config.get("maximum_ban_delay", 3)
                self.min_general = config.get("minimum_general_delay", 0.5)
                self.max_general = config.get("maximum_general_delay", 1.5)
        except Exception as e:
            print(f"{Fore.RED}Error loading config: {e}")
            sys.exit(1)

config = Config()

def random_cooldown(minimum, maximum):
    return random.uniform(minimum, maximum)

async def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

async def show_disclaimer():
    if not config.skip_disclaimer:
        messages = [
            f"{Fore.LIGHTWHITE_EX}{Style.BRIGHT}DISCLAIMER:",
            f"{Style.RESET_ALL}{Fore.LIGHTWHITE_EX}User automation and spamming are {Fore.LIGHTYELLOW_EX}{Style.BRIGHT}against Discord's TOS!!{Style.RESET_ALL}{Fore.RESET}",
            f"{Fore.LIGHTWHITE_EX}Use this tool only for educational purposes and at your own risk",
            f"{Fore.LIGHTWHITE_EX}Ask the server owner if you're allowed to use this tool",
            f"{Fore.LIGHTGREEN_EX}{Style.BRIGHT}Mass Dm {Style.RESET_ALL}{Fore.RESET}{Fore.LIGHTWHITE_EX}requires {Fore.LIGHTGREEN_EX}{Style.BRIGHT}Privileged Member Intents{Style.RESET_ALL}",
            f"{Fore.LIGHTWHITE_EX}This tool may get your account banned if used improperly"
        ]
        
        for idx, msg in enumerate(messages):
            print(msg)
            await asyncio.sleep(0.8 if idx < len(messages) - 1 else 0)

async def show_boot_animation():
    if not config.skip_booting:
        stages = [
            f"{Style.BRIGHT}{Fore.LIGHTWHITE_EX}Booting {Fore.RED}Karuma {Fore.RESET}{Fore.LIGHTWHITE_EX}Tool",
            f"{Fore.RED}25%",
            f"{Fore.YELLOW}50%",
            f"{Fore.LIGHTYELLOW_EX}75%",
            f"{Fore.LIGHTGREEN_EX}99%",
            f"{Fore.LIGHTBLUE_EX}Karuma Tool ready"
        ]
        
        delays = [0.3, 0.5, 0.6, 0.7, 1, 1]
        
        for stage, delay in zip(stages, delays):
            print(stage)
            await asyncio.sleep(delay)

class KarumaBot(discord.Client):
    def __init__(self, *args, **kwargs):
        intents = discord.Intents.default()
        intents.members = True
        intents.guilds = True
        intents.message_content = True
        super().__init__(intents=intents, *args, **kwargs)
        
    async def on_ready(self):
        await self.change_presence(
            activity=discord.Activity(
                type=discord.ActivityType.watching,
                name="github.com/hoemotion"
            ),
            status=discord.Status.idle
        )
        await clear_console()
        await main_menu(self)

    async def get_guild_by_id(self, guild_id):
        return discord.utils.get(self.guilds, id=guild_id)

async def check_permissions_and_confirm(guild, required_perms, action_name):
    bot_member = guild.get_member(client.user.id)
    missing_perms = [perm for perm, value in required_perms.items() if not getattr(bot_member.guild_permissions, perm)]
    
    if missing_perms:
        print(f"{Fore.YELLOW}Warning: Missing permissions for {action_name}:")
        for perm in missing_perms:
            print(f"- {perm.replace('_', ' ').title()}")
        
        confirm = input(f"{Fore.LIGHTYELLOW_EX}Continue without {action_name}? (yes/no): ").lower()
        if confirm != "yes":
            return False, missing_perms
        return True, missing_perms
    return True, []

async def nuke_server(client, guild_id=None):
    if not guild_id:
        while True:
            try:
                guild_id = int(input(f'{Fore.LIGHTYELLOW_EX}Enter server ID: '))
                break
            except ValueError:
                print(f'{Fore.RED}Invalid ID')
                
    guild = await client.get_guild_by_id(guild_id)
    if not guild:
        print(f"{Fore.RED}Server not found")
        return
        
    bot_member = guild.get_member(client.user.id)
    reason = input("Ban reason (optional): ")
    
    # Define required permissions for each action group
    action_groups = {
        "ban_members": {
            "name": "banning members",
            "perms": {"ban_members": True},
            "func": ban_members,
            "args": (guild, bot_member, reason)
        },
        "manage_channels": {
            "name": "deleting channels",
            "perms": {"manage_channels": True},
            "func": delete_channels,
            "args": (guild,)
        },
        "manage_roles": {
            "name": "deleting roles",
            "perms": {"manage_roles": True},
            "func": delete_roles,
            "args": (guild, bot_member)
        },
        "manage_emojis": {
            "name": "deleting emojis",
            "perms": {"manage_emojis": True},
            "func": delete_emojis,
            "args": (guild,)
        },
        "manage_emojis_and_stickers": {
            "name": "deleting stickers",
            "perms": {"manage_emojis": True},  # Same permission for stickers
            "func": delete_stickers,
            "args": (guild,)
        }
    }
    
    # Process each action group with permission checks
    for action in action_groups.values():
        proceed, missing = await check_permissions_and_confirm(
            guild, 
            action["perms"], 
            action["name"]
        )
        
        if proceed and not missing:
            await action["func"](*action["args"])
    
    print(f"{Fore.LIGHTGREEN_EX}Nuke operations completed")
    input("Press Enter to continue")

async def ban_members(guild, bot_member, reason):
    members = [m for m in guild.members if m != client.user and m.top_role < bot_member.top_role]
    total = len(members)
    
    for idx, member in enumerate(members, 1):
        try:
            await member.ban(reason=reason, delete_message_days=7)
            print(f"{Fore.LIGHTGREEN_EX}[{idx}/{total}] Banned {Fore.YELLOW}{member}")
        except Exception as e:
            print(f"{Fore.RED}[{idx}/{total}] Failed to ban {Fore.YELLOW}{member}: {e}")
        
        if idx < total:
            await asyncio.sleep(random_cooldown(config.min_ban, config.max_ban))

async def delete_channels(guild):
    for channel in guild.channels:
        try:
            await channel.delete()
            print(f"{Fore.LIGHTGREEN_EX}Deleted channel: {Fore.YELLOW}{channel.name}")
        except Exception as e:
            print(f"{Fore.RED}Failed to delete channel {Fore.YELLOW}{channel.name}: {e}")
        await asyncio.sleep(random_cooldown(config.min_general, config.max_general))

async def delete_roles(guild, bot_member):
    for role in guild.roles:
        if role.name != "@everyone" and role.position < bot_member.top_role.position:
            try:
                await role.delete()
                print(f"{Fore.LIGHTGREEN_EX}Deleted role: {Fore.YELLOW}{role.name}")
            except Exception as e:
                print(f"{Fore.RED}Failed to delete role {Fore.YELLOW}{role.name}: {e}")
            await asyncio.sleep(random_cooldown(config.min_general, config.max_general))

async def delete_emojis(guild):
    emojis = await guild.fetch_emojis()
    if not emojis:
        print(f"{Fore.YELLOW}No emojis to delete")
        return
        
    for emoji in emojis:
        try:
            await emoji.delete()
            print(f"{Fore.LIGHTGREEN_EX}Deleted emoji: {Fore.YELLOW}{emoji.name}")
        except Exception as e:
            print(f"{Fore.RED}Failed to delete emoji {Fore.YELLOW}{emoji.name}: {e}")
        await asyncio.sleep(random_cooldown(config.min_general, config.max_general))

async def delete_stickers(guild):
    stickers = await guild.fetch_stickers()
    if not stickers:
        print(f"{Fore.YELLOW}No stickers to delete")
        return
        
    for sticker in stickers:
        try:
            await sticker.delete()
            print(f"{Fore.LIGHTGREEN_EX}Deleted sticker: {Fore.YELLOW}{sticker.name}")
        except Exception as e:
            print(f"{Fore.RED}Failed to delete sticker {Fore.YELLOW}{sticker.name}: {e}")
        await asyncio.sleep(random_cooldown(config.min_general, config.max_general))

async def raid_server(client, guild_id=None):
    if not guild_id:
        while True:
            try:
                guild_id = int(input(f'{Fore.LIGHTYELLOW_EX}Enter server ID: '))
                break
            except ValueError:
                print(f'{Fore.RED}Invalid ID')
                
    guild = await client.get_guild_by_id(guild_id)
    if not guild:
        print(f"{Fore.RED}Server not found")
        return
        
    bot_member = guild.get_member(client.user.id)
    
    # Define action groups with required permissions
    action_groups = {
        "rename_server": {
            "name": "renaming server",
            "perms": {"manage_guild": True},
            "func": rename_server,
            "args": (guild,)
        },
        "create_channels": {
            "name": "creating channels",
            "perms": {"manage_channels": True},
            "func": create_channels,
            "args": (guild,)
        },
        "create_roles": {
            "name": "creating roles",
            "perms": {"manage_roles": True},
            "func": create_roles,
            "args": (guild,)
        },
        "change_nicks": {
            "name": "changing nicknames",
            "perms": {"manage_nicknames": True},
            "func": change_nicknames,
            "args": (guild, bot_member)
        }
    }
    
    # Get user input for all actions first
    new_name = input("New server name (leave blank to skip): ")
    channel_name = input("Channel name to spam: ")
    channel_count = int(input("Number of channels to create (0 to skip): "))
    role_name = input("Role name to spam: ")
    role_count = int(input("Number of roles to create (0 to skip): "))
    nickname = input("Nickname to set (leave blank to skip): ")
    
    # Prepare arguments based on user input
    action_groups["rename_server"]["args"] = (guild, new_name) if new_name else None
    action_groups["create_channels"]["args"] = (guild, channel_name, channel_count) if channel_count > 0 else None
    action_groups["create_roles"]["args"] = (guild, role_name, role_count) if role_count > 0 else None
    action_groups["change_nicks"]["args"] = (guild, bot_member, nickname) if nickname else None
    
    # Process each action group
    for action in action_groups.values():
        if action["args"] is None:
            continue
            
        proceed, missing = await check_permissions_and_confirm(
            guild, 
            action["perms"], 
            action["name"]
        )
        
        if proceed and not missing:
            await action["func"](*action["args"])
    
    print(f"{Fore.LIGHTGREEN_EX}Raid operations completed")
    input("Press Enter to continue")

async def rename_server(guild, new_name):
    try:
        await guild.edit(name=new_name)
        print(f"{Fore.LIGHTGREEN_EX}Server renamed to {Fore.YELLOW}{new_name}")
    except Exception as e:
        print(f"{Fore.RED}Failed to rename server: {e}")

async def create_channels(guild, channel_name, count):
    for i in range(count):
        try:
            await guild.create_text_channel(f"{channel_name}-{i+1}")
            print(f"{Fore.LIGHTGREEN_EX}Created channel {Fore.YELLOW}{channel_name}-{i+1}")
        except Exception as e:
            print(f"{Fore.RED}Failed to create channel: {e}")
        await asyncio.sleep(random_cooldown(config.min_general, config.max_general))

async def create_roles(guild, role_name, count):
    for i in range(count):
        try:
            await guild.create_role(name=f"{role_name}-{i+1}")
            print(f"{Fore.LIGHTGREEN_EX}Created role {Fore.YELLOW}{role_name}-{i+1}")
        except Exception as e:
            print(f"{Fore.RED}Failed to create role: {e}")
        await asyncio.sleep(random_cooldown(config.min_general, config.max_general))

async def change_nicknames(guild, bot_member, nickname):
    members = [m for m in guild.members if m != client.user and m.top_role < bot_member.top_role]
    for member in members:
        try:
            await member.edit(nick=nickname)
            print(f"{Fore.LIGHTGREEN_EX}Changed nickname for {Fore.YELLOW}{member}")
        except Exception as e:
            print(f"{Fore.RED}Failed to change nickname for {Fore.YELLOW}{member}: {e}")
        await asyncio.sleep(random_cooldown(config.min_general, config.max_general))

async def create_embed():
    embed = discord.Embed()
    
    title = input(f"{Fore.LIGHTGREEN_EX}Embed title (leave blank for none): ")
    if title:
        embed.title = title
    
    description = input(f"{Fore.LIGHTGREEN_EX}Embed description (leave blank for none): ")
    if description:
        embed.description = description
    
    color = input(f"{Fore.LIGHTGREEN_EX}Embed color (hex without #, e.g., FF0000 for red): ")
    if color:
        try:
            embed.color = int(color, 16)
        except:
            embed.color = discord.Color.random()
    
    # Add fields
    while True:
        field_name = input(f"{Fore.LIGHTGREEN_EX}Add field? Enter name (leave blank to stop): ")
        if not field_name:
            break
        field_value = input(f"{Fore.LIGHTGREEN_EX}Field value: ")
        inline = input(f"{Fore.LIGHTGREEN_EX}Inline field? (y/n): ").lower() == 'y'
        embed.add_field(name=field_name, value=field_value, inline=inline)
    
    # Set author
    author_name = input(f"{Fore.LIGHTGREEN_EX}Author name (leave blank for none): ")
    if author_name:
        author_icon = input(f"{Fore.LIGHTGREEN_EX}Author icon URL (leave blank for none): ")
        embed.set_author(name=author_name, icon_url=author_icon if author_icon else None)
    
    # Set footer
    footer_text = input(f"{Fore.LIGHTGREEN_EX}Footer text (leave blank for none): ")
    if footer_text:
        footer_icon = input(f"{Fore.LIGHTGREEN_EX}Footer icon URL (leave blank for none): ")
        embed.set_footer(text=footer_text, icon_url=footer_icon if footer_icon else None)
    
    # Set thumbnail
    thumbnail = input(f"{Fore.LIGHTGREEN_EX}Thumbnail URL (leave blank for none): ")
    if thumbnail:
        embed.set_thumbnail(url=thumbnail)
    
    # Set image
    image = input(f"{Fore.LIGHTGREEN_EX}Image URL (leave blank for none): ")
    if image:
        embed.set_image(url=image)
    
    return embed

async def mass_dm_users(users):
    message_type = input(f"{Fore.LIGHTGREEN_EX}Message type (text/embed/both): ").lower()
    
    text_content = None
    embed_content = None
    
    if message_type in ['text', 'both']:
        text_content = input(f"{Fore.LIGHTGREEN_EX}Enter text message: ")
    
    if message_type in ['embed', 'both']:
        embed_content = await create_embed()
    
    if not text_content and not embed_content:
        print(f"{Fore.RED}No message content provided")
        return
    
    total = len(users)
    for idx, user in enumerate(users, 1):
        try:
            # Skip if user is the bot itself
            if user.id == client.user.id:
                continue
                
            # Skip bots
            if user.bot:
                continue
                
            if text_content and embed_content:
                await user.send(content=text_content, embed=embed_content)
            elif text_content:
                await user.send(content=text_content)
            elif embed_content:
                await user.send(embed=embed_content)
                
            print(f"{Fore.LIGHTGREEN_EX}[{idx}/{total}] Sent to {Fore.YELLOW}{user}")
        except Exception as e:
            print(f"{Fore.RED}[{idx}/{total}] Failed to send to {Fore.YELLOW}{user}: {e}")
        
        if idx < total:
            await asyncio.sleep(random_cooldown(config.minimum_dm, config.maximum_dm))

async def mass_dm_server(client, guild_id=None):
    if not guild_id:
        while True:
            try:
                guild_id = int(input(f'{Fore.LIGHTYELLOW_EX}Enter server ID: '))
                break
            except ValueError:
                print(f'{Fore.RED}Invalid ID')
                
    guild = await client.get_guild_by_id(guild_id)
    if not guild:
        print(f"{Fore.RED}Server not found")
        return
        
    print(f'Target: {Fore.YELLOW}{guild.name}')
    
    members = [m for m in guild.members if not m.bot]  # Exclude bots
    await mass_dm_users(members)

async def mass_dm_all_users(client):
    users = [u for u in client.users if not u.bot]  # Exclude bots
    await mass_dm_users(users)

async def list_servers(client):
    print(f"{Fore.LIGHTGREEN_EX}Connected servers:")
    for guild in client.guilds:
        bot_member = guild.get_member(client.user.id)
        perms = []
        
        # Existing permission checks
        if bot_member.guild_permissions.ban_members:
            perms.append("Ban")
        if bot_member.guild_permissions.manage_channels:
            perms.append("Channels")
        if bot_member.guild_permissions.manage_roles:
            perms.append("Roles")
        if bot_member.guild_permissions.manage_nicknames:
            perms.append("Nicks")
        if bot_member.guild_permissions.manage_emojis:
            perms.append("Emojis")
        if bot_member.guild_permissions.manage_guild:
            perms.append("Server")
        if bot_member.guild_permissions.create_instant_invite:
            perms.append("Invites")

        perm_status = f"{Fore.LIGHTGREEN_EX}Perms: {', '.join(perms)}" if perms else f"{Fore.RED}No key perms"
        
        print(f"\n{Fore.YELLOW}{guild.name} {Fore.LIGHTGREEN_EX}(ID: {guild.id}, Members: {guild.member_count}) {perm_status}")
        
        # Fetch and display permanent invites (non-expiring)
        if bot_member.guild_permissions.manage_guild:
            try:
                invites = await guild.invites()
                permanent_invites = [inv for inv in invites if inv.max_age == 0]  # Filter out expiring invites
                
                if permanent_invites:
                    print(f"{Fore.CYAN}  Permanent Invites:")
                    for invite in permanent_invites:
                        print(f"  - {Fore.LIGHTBLUE_EX}{invite.url} (Uses: {invite.uses}, Created by: {invite.inviter})")
                else:
                    print(f"{Fore.RED}  No permanent invites found.")
            except discord.Forbidden:
                print(f"{Fore.RED}  No invite access (missing 'Manage Server' permission)")
            except Exception as e:
                print(f"{Fore.RED}  Failed to fetch invites: {e}")
    
    input("\nPress Enter to continue...")

async def leave_all_servers(client):
    confirm = input(f"{Fore.RED}Are you sure? (yes/no): ").lower()
    if confirm != "yes":
        return
        
    for guild in client.guilds:
        try:
            await guild.leave()
            print(f"{Fore.LIGHTGREEN_EX}Left {Fore.YELLOW}{guild.name}")
        except Exception as e:
            print(f"{Fore.RED}Failed to leave {Fore.YELLOW}{guild.name}: {e}")
        await asyncio.sleep(1)
    
    print(f"{Fore.LIGHTGREEN_EX}Left all servers")
    input("Press Enter to continue")

async def main_menu(client):
    while True:
        await clear_console()
        print(pyfade.Fade.Horizontal(pyfade.Colors.yellow_to_red, '''
██╗  ██╗ █████╗ ██████╗ ██╗   ██╗███╗   ███╗ █████╗ 
██║ ██╔╝██╔══██╗██╔══██╗██║   ██║████╗ ████║██╔══██╗
█████═╝ ███████║██████╔╝██║   ██║██╔████╔██║███████║
██╔═██╗ ██╔══██║██╔══██╗██║   ██║██║╚██╔╝██║██╔══██║
██║ ╚██╗██║  ██║██║  ██║╚██████╔╝██║ ╚═╝ ██║██║  ██║
╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝'''))
        
        stats = f"Servers: {len(client.guilds)} | Users: {len(client.users)}"
        
        print(f'''{Fore.LIGHTWHITE_EX}                                   Made by {Fore.YELLOW}hoemotion

{Fore.LIGHTWHITE_EX}GitHub: {Fore.LIGHTBLUE_EX}https://github.com/hoemotion/Karuma
{Fore.LIGHTGREEN_EX}Logged in as: {Fore.YELLOW}{client.user}
{Fore.LIGHTGREEN_EX}{stats}

{Fore.LIGHTGREEN_EX}[1] Nuke Server (Ban members, delete channels/roles/emojis/stickers)
{Fore.LIGHTGREEN_EX}[2] Raid Server (Spam channels/roles, change nicks)
{Fore.LIGHTGREEN_EX}[3] Mass DM Server (with embed support)
{Fore.LIGHTGREEN_EX}[4] Mass DM All Users (with embed support)
{Fore.LIGHTGREEN_EX}[5] List Servers (with permission info)
{Fore.LIGHTGREEN_EX}[6] Leave All Servers
{Fore.LIGHTGREEN_EX}[7] Exit
''')
        
        choice = input(f"{Fore.LIGHTGREEN_EX}Select>> ").lower()
        
        if choice == '1':
            await nuke_server(client)
        elif choice == '2':
            await raid_server(client)
        elif choice == '3':
            await mass_dm_server(client)
        elif choice == '4':
            await mass_dm_all_users(client)
        elif choice == '5':
            await list_servers(client)
        elif choice == '6':
            await leave_all_servers(client)
        elif choice in ['7', 'quit', 'exit']:
            print(f"{Fore.LIGHTGREEN_EX}Goodbye!")
            await client.close()
            sys.exit(0)
        else:
            print(f"{Fore.RED}Invalid choice")
            await asyncio.sleep(1)

async def main():
    await show_disclaimer()
    await show_boot_animation()
    
    global client
    client = KarumaBot()
    try:
        await client.start(config.token)
    except discord.LoginFailure:
        print(f"{Fore.RED}Invalid token - check your config.json")
        sys.exit(1)
    except Exception as e:
        print(f"{Fore.RED}Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    asyncio.run(main())
