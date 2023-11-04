import discord
import res

# intents = discord.Intents.default()
# intents.guilds = True
# intents.members = True
# intents.roles = True

# client = discord.Client(intents=intents)

# @client.event
# async def on_ready():
#     guild_id = 123456789012345678 # Замените на ID вашего сервера
#     guild = client.get_guild(guild_id)

#     if guild:
#         roles = guild.roles

#         with open('roles.txt', 'w') as file:
#             for role in roles:
#                 file.write(f'{role.id} - {role.name}\n')
        
#         print('Роли и их ID выгружены в файл roles.txt')

#         await client.close()

# # токен второго бота v2
# client.run(res.token_v2)





######################################################################





# import discord

# intents = discord.Intents.default()
# intents.guilds = True
# intents.members = True
# intents.roles = True

# client = discord.Client(intents=intents)

# roles_data = []

# @client.event
# async def on_ready():
#     # Получаем список серверов, к которым подключен бот
#     for guild in client.guilds:
#         guild_id = guild.id
#         guild_name = guild.name

#         roles = guild.roles

#         roles_info = []

#         for role in roles:
#             roles_info.append({'id': role.id, 'name': role.name})

#         roles_data.append({'guild_id': guild_id, 'guild_name': guild_name, 'roles': roles_info})

#         print(f'Роли и их ID для сервера {guild.name} добавлены в массив')

#         await client.close()

# async def on_message():
    

# # Замените 'YOUR_TOKEN' на ваш собственный токен бота
# client.run('YOUR_TOKEN')






########################################################################


# import discord

# intents = discord.Intents.default()
# intents.guilds = True
# intents.members = True
# intents.roles = True

# bot = discord.Client(intents=intents)

# roles_data = []

# @bot.event
# async def on_ready():
#     print('Бот v2 готов к работе')

# @bot.event
# async def on_message(message):
#     if message.author == bot.user:
#         return

#     if message.content.startswith('!выгрузить_роли'):
#         guild = message.guild

#         if guild:
#             guild_id = guild.id
#             guild_name = guild.name

#             roles = guild.roles

#             roles_info = []

#             for role in roles:
#                 roles_info.append({'id': role.id, 'name': role.name})

#             roles_data.append({'guild_id': guild_id, 'guild_name': guild_name, 'roles': roles_info})

#             await message.channel.send(f'Роли и их ID для сервера {guild.name} добавлены в массив')
#         else:
#             await message.channel.send('Ошибка: бот не находится на сервере')

# # Token Bot_v2
# client.run(res.token_v2)

intents = discord.Intents.default()
intents.guilds = True
intents.members = True
intents.roles = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    guild_id = 1168950768460640357 # Замените на ID вашего сервера
    guild = client.get_guild(guild_id)

    if guild:
        roles = guild.roles

        with open('roles.txt', 'w') as file:
            for role in roles:
                file.write(f'{role.id} - {role.name}\n')
        
        print('Роли и их ID выгружены в файл roles.txt')

        await client.close()

# Замените 'YOUR_TOKEN' на ваш собственный токен бота
client.run(res.token_v2)