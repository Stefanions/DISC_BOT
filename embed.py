#Подключение библиотек
import res
import discord
from discord.ext import commands
from discord.ui import Button, View, Select
import numpy as np

##############################################Эмбеды##############################################

######### Первый эмбед приветствия
emb_1 = discord.Embed(
    title="Добро пожаловать в Академию ССО!",
    description=
    (
        "Прежде чем мы с тобой начнем взаимодействовать, нам нужно подробнее узнать о тебе. "
        "\n\nГляди! Я снизу отправил тебе вопросы, ответь на них. Затем, нажми кнопку - 'завершить знакомство' и ты получишь доступ к Академии!\n\n"
        "p.s После прохождения формы, ты получишь доступ к Академии. Что тебе там делать?\n\n"
        "1) Жди тренировок.\n Их ты можешь найти в канале анонс-тренировок. Обязательно отмечайся!\n\n"
        "2) Просто присоединяйся в канал.\n Знакомься, но обязательно скажи, что ты только присоединился, что бы ребята понимали, что, возможно, тебе нужно помочь освоится."
    ),
        color=discord.Color.from_rgb(255, 255, 255) # ебашим белой полосочкой, иначе некрасиво)
    )


# class emb_1():
#     def __init__(self, zagolovok):
#         super().__init__(
#                 emb = discord.Embed(
#             title=zagolovk
#             color=discord.Color.from_rgb(139, 187, 236)
#                 )
#         )

# class emb_1():
#     def __init__(self, zagolovok):
#         self.zagolovok = zagolovok
        
#     emb = discord.Embed(
#     title=zagolovk,
#     color=discord.Color.from_rgb(139, 187, 236)
#         )
                

#эмбед 2 вопроса

# emb_2 = discord.Embed(
#     title="?",
#     color=discord.Color.from_rgb(139, 187, 236)
#     )

######### эмбед 3 вопроса

# emb_3 = discord.Embed(
#     title="?",
#     color=discord.Color.from_rgb(139, 187, 236)
#     )

######### эмбед 4 вопроса

emb_4 = discord.Embed(
    title="Сколько у тебя часов в SQUAD?",
    color=discord.Color.from_rgb(139, 187, 236)
    )

######### эмбед 5 вопроса

# emb_5 = discord.Embed(
#     title="?",
#     color=discord.Color.from_rgb(139, 187, 236)
#     )

######### эмбед 6 вопроса

emb_6 =  discord.Embed(
    title="Выбери одну роль (стрелковую специальность), номер один для тебя?",
    color=discord.Color.from_rgb(139, 187, 236)
    )

######### эмбед 7 вопроса

emb_7 = discord.Embed(
    title="Выбери дополнительные 2 или более роли, помимо основной",
    color=discord.Color.from_rgb(139, 187, 236)
    )

######### эмбед 8 вопроса

# emb_8 = discord.Embed(
#     title="?",
#     color=discord.Color.from_rgb(139, 187, 236)
#     )

######### эмбед 9 вопроса

# emb_9 = discord.Embed(
#     title="?",
#     color=discord.Color.from_rgb(139, 187, 236)
#     )

######### эмбед 10 вопроса

# emb_10 = discord.Embed(
#     title="?",
#     color=discord.Color.from_rgb(139, 187, 236)
#     )

######### эмбед 11 вопроса

# emb_11 = discord.Embed(
#     title="?",
#     color=discord.Color.from_rgb(139, 187, 236)
#     )

######### эмбед 12 вопроса

# emb_13 = discord.Embed(
#     title="?",
#     color=discord.Color.from_rgb(139, 187, 236)
#     )

######### эмбед 13 вопроса

# emb_13 = discord.Embed(
#     title="?",
#     color=discord.Color.from_rgb(139, 187, 236)
#     )

######### эмбед 14 вопроса

# emb_14 = discord.Embed(
#     title="?",
#     color=discord.Color.from_rgb(139, 187, 236)
#     )