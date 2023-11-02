#Подключение библиотек
import res
import discord
from discord.ext import commands
from discord.ui import Button, View, Select
import numpy as np



##############################################Селекты и не только + разные конструкции##############################################

# # шаблон
# class q_?(Select):
#     def __init__(self): 
#         super().__init__(
#         placeholder="?", 
#         options=[
#         discord.SelectOption(label="0-50 часов", value="hours_1"),
#         discord.SelectOption(label="50+ часов", value="hours_2")
#         ], 
#         custom_id="s_?")
#     async def callback(self, interaction):
#         await interaction.response.defer()
#         print("Ответ?")



####### 1 вопрос #######
async def q_1(user, bot):
    mes = await bot.wait_for('message')
    #print(f"Ваш никнейм : {mes.content}")


####### 2 вопрос #######
class q_2(Select):
    def __init__(self): 
        super().__init__(
        placeholder="В какое время относительно МСК ты играешь в основном?", 
        min_values = 2,
        max_values = 4,
        options=[
        discord.SelectOption(label="Утром по МСК", value="prime_1"),
        discord.SelectOption(label="Денём по МСК", value="prime_2"),
        discord.SelectOption(label="Вечером по МСК", value="prime_3"),
        discord.SelectOption(label="Ночью по МСК", value="prime_4")
        ], 
        custom_id="s_2")
    async def callback(self, interaction):
        await interaction.response.defer()
        print("Ответ2")


####### 3 вопрос #######
class q_3(Select):
    def __init__(self): 
        super().__init__(
        placeholder="Какой у тебя часовой пояс?", 
        options=[
        discord.SelectOption(label="UTC-12:00 (Антивампирский остров)"),
        discord.SelectOption(label="UTC-11:00 (Самоа)"),
        discord.SelectOption(label="UTC-10:00 (Гавайи)"),
        discord.SelectOption(label="UTC-09:00 (Аляска)"),
        discord.SelectOption(label="UTC-08:00 (Тихоокеанское время - Северная Америка)"),
        discord.SelectOption(label="UTC-07:00 (Горное время - Северная Америка)"),
        discord.SelectOption(label="UTC-06:00 (Центральное время - Северная Америка)"),
        discord.SelectOption(label="UTC-05:00 (Восточное время - Северная Америка)"),
        discord.SelectOption(label="UTC-04:00 (Атлантическое время - Северная Америка)"),
        discord.SelectOption(label="UTC-03:00 (Бразилиа, Буэнос-Айрес)"),
        discord.SelectOption(label="UTC-02:00 (Среднеатлантическое время)"),
        discord.SelectOption(label="UTC-01:00 (Азорские острова, о. Зеленого Мыса)"),
        discord.SelectOption(label="UTC±00:00 (Западноевропейское время - Гринвич)"),
        discord.SelectOption(label="UTC+01:00 (Центральноевропейское время)"),
        discord.SelectOption(label="UTC+02:00 (Восточноевропейское время, Калининград)"),
        discord.SelectOption(label="UTC+03:00 (Московское время)"),
        discord.SelectOption(label="UTC+03:30 (Иранское время)"),
        discord.SelectOption(label="UTC+04:00 (Азербайджанское время, Грузинское время, Самарское время)"),
        discord.SelectOption(label="UTC+04:30 (Афганистанское время)"),
        discord.SelectOption(label="UTC+05:00 (Пакистанское время, Екатеринбургское время)"),
        discord.SelectOption(label="UTC+05:30 (Индийское стандартное время, Шри-Ланка)"),
        discord.SelectOption(label="UTC+05:45 (Непальское время)"),
        discord.SelectOption(label="UTC+06:00 (Омское время, Бангладешское время)"),
        discord.SelectOption(label="UTC+06:30 (Кокосовые острова, Мьянма)"),
        discord.SelectOption(label="UTC+07:00 (Красноярское время, Индокитайское время)"),
        discord.SelectOption(label="UTC+08:00 (Иркутское время, Китайское время, Западноавстралийское время)"),
        discord.SelectOption(label="UTC+08:45 (Юго-западное Западноавстралийское время)"),
        discord.SelectOption(label="UTC+09:00 (Якутское время, Японское стандартное время, Корейское время)"),
        discord.SelectOption(label="UTC+09:30 (Центральное австралийское время)"),
        discord.SelectOption(label="UTC+10:00 (Восточное австралийское время)"),
        discord.SelectOption(label="UTC+10:30 (Лорд-Хаулендский остров)"),
        discord.SelectOption(label="UTC+11:00 (Соломоновы острова, Вануату)"),
        discord.SelectOption(label="UTC+11:30 (Норфолкское время)"),
        discord.SelectOption(label="UTC+12:00 (Фиджи, Камчатское время)"),
        discord.SelectOption(label="UTC+12:45 (Чатемское время)"),
        discord.SelectOption(label="UTC+13:00 (Тонга)"),
        discord.SelectOption(label="UTC+14:00 (Линия перемены даты)")
        ], 
        custom_id="s_3")
    async def callback(self, interaction):
        await interaction.response.defer()
        print("Ответ3")


####### 4 вопрос #######
class q_4(Select):
    def __init__(self): 
        super().__init__(
        placeholder="Сколько у тебя часов в SQUAD?", 
        options=[
        discord.SelectOption(label="0-50 часов", value="hours_1"),
        discord.SelectOption(label="50+ часов", value="hours_2"),
        discord.SelectOption(label="100+ часов", value="hours_3"),
        discord.SelectOption(label="250+ часов", value="hours_4"),
        discord.SelectOption(label="500+ часов", value="hours_5"),
        discord.SelectOption(label="1000+ часов", value="hours_6"),
        discord.SelectOption(label="2000+ часов", value="hours_7")
        ], 
        custom_id="s_4")
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
        custom_id="s_6")
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

####### 9 вопрос #######
async def q_9(user, bot):
    mes = await bot.wait_for('message')

####### 14 вопрос #######
async def q_14(user, bot):
    mes = await bot.wait_for('message')