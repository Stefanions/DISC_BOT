import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Bot is ready: {bot.user.name}')

@bot.command()
async def question1(ctx):
    # Шаг 1: Создать и вывести эмбед сообщение
    embed = discord.Embed(title="Введите вопрос 1 сюда", color=discord.Color.blue())
    msg = await ctx.send(embed=embed)

    # Шаг 2: Создать выпадающий список
    options = ["Вариант 1", "Вариант 2", "Вариант 3"]
    for i, option in enumerate(options):
        await msg.add_reaction(f'🔢')

    def check(reaction, user):
        return user == ctx.author and str(reaction.emoji) in ['1️⃣', '2️⃣', '3️⃣']

    reaction, user = await bot.wait_for('reaction_add', check=check)

    # Шаг 3: Написать в личные сообщения тому, кто выбрал вариант
    choice = options[int(reaction.emoji) - 1]
    user = await bot.fetch_user(user.id)
    await user.send(f'Вы выбрали вариант: {choice}')

    # Шаг 4: Написать "я кончил"
    await ctx.author.send('Я кончил')

bot.run("MTE2ODk1NDM0MDI3OTU5OTE4NA.GFLeyp.u6qIKhSmz0fQHM4k3DlHv2C9XbRginkbKExqEo")