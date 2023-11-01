#ADSasDASDasdaSDASDaSDaSD
#Asdasdasdasdasdasd
#Файл с основными командами
#Подключение библиотек
import res
import discord
from discord.ext import commands
from discord.ui import Button, View, Select
import numpy as np
import question

#Базовые структуры
class Main(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

bot = Main(command_prefix = ".",intents = discord.Intents.all(),help_command = None)

###########################################Классы кнопок########################################
#Кнопка при вступлении
class main_but(View):
    @discord.ui.button(label = "Пройти опрос", style=discord.ButtonStyle.danger)
    async def button_callback(self, interaction, button):
        await interaction.response.defer()
        await Intro_LS(interaction.user)




###########################################Функциии разные########################################
#Функция разговора бота в ЛС
async def Intro_LS(user):
    await user.send("Приветсвую тебя в нашей команде ССО!!!\n Пройди небольшой тест.")
    #Тут создаю окошечко для наших
    s = View()
    
    #1 вопрос
    e1 = discord.Embed(title="Вопрос 1")
    s1 = question.q1()
    s.add_item(s1)
    await user.send("За какие роли вы в основном играете?(Выбрать 3)", embed=e1, view = s)
    s.clear_items()

    #2 вопрос
    e2 = discord.Embed(title="Вопрос 2")
    s2 = question.q2()
    s.add_item(s2)
    await user.send("Кто", embed=e2, view = s)




#Обработка селекта
@bot.event
async def on_select(ctx, intraction):
    print("Я тут")

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
    but_main = main_but()
    await channel.send("Я начал работу", view=but_main)



bot.run(res.token)

