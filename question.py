#Подключение библиотек
import res
import discord
from discord.ext import commands
from discord.ui import Button, View, Select
import numpy as np

##############################################Селекты##############################################
#1 вопрос
class q1(Select):
    def __init__(self): 
        super().__init__(
        placeholder="Роли", 
        min_values = 3,
        max_values = 3,
        options=[
        discord.SelectOption(label="Медик", value="option1"),
        discord.SelectOption(label="Сквад лидер", value="option2"),
        discord.SelectOption(label="Тандем", value="option3"),
        discord.SelectOption(label="Труба", value="option4")
        ], 
        custom_id="s1")
    async def callback(self, interaction):
        await interaction.response.defer()
        print("1")

#2 вопрос
class q2(Select):
    def __init__(self): 
        super().__init__(
        placeholder="Выберите опцию", 
        options=[
        discord.SelectOption(label="хуей", value="op1"),
        discord.SelectOption(label="хуей", value="op2"),
        discord.SelectOption(label="хуей", value="op3")
        ], 
        custom_id="s1")
    async def callback(self, interaction):
        await interaction.response.defer()
        print("2")