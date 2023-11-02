#Подключение библиотек
import res
import discord
from discord.ext import commands
from discord.ui import Button, View, Select
import numpy as np



##############################################Селекты и не только + разные конструкции##############################################

####### 1 вопрос #######
async def q_1(user, bot):
    await user.send("Напиши свой никнейм в игре.")
    mes = await bot.wait_for('message')
    print(f"Ваш никнейм : {mes.content}")




####### 4 вопрос #######

class q_4(Select):
    def __init__(self): 
        super().__init__(
        placeholder="Сколько у тебя часов в SQUAD?", 
        options=[
        discord.SelectOption(label="0-50 часов", value="otp1"),
        discord.SelectOption(label="50+ часов", value="otp2"),
        discord.SelectOption(label="100+ часов", value="otp3"),
        discord.SelectOption(label="250+ часов", value="otp4"),
        discord.SelectOption(label="500+ часов", value="otp5"),
        discord.SelectOption(label="1000+ часов", value="otp6"),
        discord.SelectOption(label="2000+ часов", value="otp7")
        ], 
        custom_id="s_1")
    async def callback(self, interaction):
        await interaction.response.defer()
        print("Ответ4")

####### 6 вопрос #######
class q_6(Select):
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
        custom_id="s_2")
    async def callback(self, interaction):
        await interaction.response.defer()
        print("Ответ6")

####### 7 вопрос
class q_7(Select):
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
        custom_id="s_4")
    async def callback(self, interaction):
        await interaction.response.defer()
        print("Ответ7")



####### 8 вопрос #######
async def q_8(user, bot):
    await user.send("Ты понимаешь, что для того, что бы играть командно, нужно, что бы все делали одинаково?")
    mes = await bot.wait_for('message')
    print(f"Ваш ответ : {mes.content}")