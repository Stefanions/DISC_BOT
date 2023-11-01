#Файл с основными командами
#Подключение библиотек
import res
import but
import discord
from discord.ext import commands
from discord.ui import Button, View
import numpy as np

#Базовые структуры
class Main(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

bot = Main(command_prefix = ".",intents = discord.Intents.all(),help_command = None)

#При включении бота
@bot.event
async def on_ready():
    channel = bot.get_channel(1168950770364858425)
    #Удаление сообщений
    async for message in channel.history(limit=None):
        if message.author.id == bot.user.id:
            try:
                await message.delete()
            except discord.errors.NotFound:
                pass

    #Начальная кнопка
    print("I am here")
    but_main = but.main_but()
    await channel.send("Я начал работу", view=but_main)
    


#Команды основные
#Тестовая 1
@bot.command()
async def Hi(ctx):
    await ctx.send("ССО хай, это моя первая команда")

#Приветствие в лс
@bot.command()
async def LS(ctx):
    if (ctx.channel.id == 1168950770364858427):
        await ctx.author.send("Приветствую в нашей команде ССО!!!\nПеред тем как начать с нами играть, нам нужно узнать про тебя немнго больше.\nОтветь на пару вопросов.")


bot.run(res.token)
