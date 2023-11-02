#Подключение библиотек
import res
import discord
from discord.ext import commands
from discord.ui import Button, View, Select
import numpy as np

##############################################Селекты##############################################

#6 вопрос
class q6(Select):
    def __init__(self): 
        super().__init__(
        placeholder="Оснавная роль", 
        options=[
        discord.SelectOption(label="CMD", value="op1"),
        discord.SelectOption(label="Сквадной", value="op2"),
        discord.SelectOption(label="Лидер Фаер Тимы", value="op3"),
        discord.SelectOption(label="Обычный стрелок", value="op4"),
        discord.SelectOption(label="Стрелок ГП", value="op5"),
        discord.SelectOption(label="Труба", value="op6"),
        discord.SelectOption(label="Медик", value="op7"),
        discord.SelectOption(label="Пулеметчик", value="op8"),
        discord.SelectOption(label="Такнкист-командир", value="op9"),
        discord.SelectOption(label="Танкист-водитель", value="op10"),
        discord.SelectOption(label="Танкист-стрелок", value="op11"),
        discord.SelectOption(label="Пилот", value="op12")
        ], 
        custom_id="s1")
    async def callback(self, interaction):
        await interaction.response.defer()
        print("Ответ6")

#7 вопрос
class q7(Select):
    def __init__(self): 
        super().__init__(
        placeholder="Доп. Роли", 
        min_values = 2,
        max_values = 12,
        options=[
        discord.SelectOption(label="CMD", value="option1"),
        discord.SelectOption(label="Сквадной", value="option2"),
        discord.SelectOption(label="Лидер Фаер Тимы", value="option3"),
        discord.SelectOption(label="Обычный стрелок", value="option4"),
        discord.SelectOption(label="Стрелок ГП", value="option5"),
        discord.SelectOption(label="Труба", value="option6"),
        discord.SelectOption(label="Медик", value="option7"),
        discord.SelectOption(label="Пулеметчик", value="option8"),
        discord.SelectOption(label="Такнкист-командир", value="option9"),
        discord.SelectOption(label="Танкист-водитель", value="option10"),
        discord.SelectOption(label="Танкист-стрелок", value="option11"),
        discord.SelectOption(label="Пилот", value="option12")
        ], 
        custom_id="s1")
    async def callback(self, interaction):
        await interaction.response.defer()
        print("Ответ7")
