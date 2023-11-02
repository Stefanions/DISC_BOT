#Изменеие 2
#Изменеие 2
#Файл с основными командами
#Подключение библиотек
# await message.author.edit(nick=new_nickname) изменение никнейма

import res
import discord
from discord.ext import commands
from discord.ui import Button, View, Select
import numpy as np
import question
import embed

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

    #Тут создаю окошечко для наших селектов и строк
    s = View()

    #Приветственное сообщение
    await user.send(embed=embed.emb_1)

    #1 вопрос
    await question.q_1(user, bot)
    
    #4 вопрос
    s.add_item(question.q_4())
    await user.send(embed=embed.emb_4, view = s)

    #6 вопрос
    s.clear_items()
    s.add_item(question.q_6())
    await user.send(embed=embed.emb_6, view = s)

    #7 вопрос
    s.clear_items()
    s.add_item(question.q_7())
    await user.send(embed=embed.emb_7, view = s)
    
    #8 вопрос
    s.clear_items()
    await question.q_8(user, bot)

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

