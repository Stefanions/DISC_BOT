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
#Функция прохождения первого собеседования в личных сообщенях
async def Intro_LS(user):

    #Тут создаю окошечко для наших селектов и строк
    s = View()

    #Приветственное сообщение
    await user.send(embed=embed.emb_1)

    #### 1 вопрос
    await question.q_1(user, bot)


    #### 2 вопрос
    # s.clear_items()
    # s.add_item(question.q_2())
    # await user.send(embed=embed.emb_2, view = s)

    #### 3 вопрос    
    s.clear_items()

    #### 4 вопрос
    s.clear_items()
    s.add_item(question.q_4())
    e_4 = embed.emb_2("Сколько у тебя часов в SQUAD?")
    await user.send(embed=e_4.emb, view = s)


    #### 5 вопрос    
    s.clear_items()

    #### 6 вопрос
    s.clear_items()
    s.add_item(question.q_6())
    e_6 = embed.emb_2("Выбери одну роль (стрелковую специальность), номер один для тебя?")
    await user.send(embed=e_6.emb, view = s)


    #### 7 вопрос
    s.clear_items()
    s.add_item(question.q_7())
    e_7 = embed.emb_2("Выбери дополнительные 2 или более роли, помимо основной. Напиши их ниже.")
    await user.send(embed=e_7.emb, view = s)
    

    #### 8 вопрос
    s.clear_items()
    await question.q_8(user, bot)


    #### 9 вопрос    
    s.clear_items()


    #### 10 вопрос
    s.clear_items()


    #### 11 вопрос
    s.clear_items()


    #### 12 вопрос
    s.clear_items()


    #### 13 вопрос
    s.clear_items()


    #### 14 вопрос
    s.clear_items()



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

