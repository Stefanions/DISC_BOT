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
    # Создаем объект Embed
    title1 = discord.Embed(
        title="Добро пожаловать в Академию ССО!",
        description=(
            "Прежде чем мы с тобой начнем взаимодействовать, нам нужно подробнее узнать о тебе. "
            "\n\nГляди! Я снизу отправил тебе вопросы, ответь на них. Затем, нажми кнопку - 'завершить знакомство' и ты получишь доступ к Академии!\n\n"
            "p.s После прохождения формы, ты получишь доступ к Академии. Что тебе там делать?\n\n"
            "1) Жди тренировок.\n Их ты можешь найти в канале анонс-тренировок. Обязательно отмечайся!\n\n"
            "2) Просто присоединяйся в канал.\n Знакомься, но обязательно скажи, что ты только присоединился, что бы ребята понимали, что, возможно, тебе нужно помочь освоится."
        ),
        color=discord.Color.from_rgb(255, 255, 255) # ебашим белой полосочкой, иначе некрасиво)
    )
    await user.send(embed=title1)

    #Тут создаю окошечко для наших
    s = View()
    
    #6 вопрос
    e6 = discord.Embed(
        title="Выбери одну роль (стрелковую специальность), номер один для тебя?",
        color=discord.Color.from_rgb(139, 187, 236)
        )
    s6 = question.q6()
    s.add_item(s6)
    await user.send(embed=e6, view = s)
    s.clear_items()

    #7 вопрос
    e7 = discord.Embed(
        title="Выбери дополнительные 2 или более роли, помимо основной",
        color=discord.Color.from_rgb(139, 187, 236)
        )
    s7 = question.q7()
    s.add_item(s7)
    await user.send(embed=e7, view = s)
    s.clear_items()





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

