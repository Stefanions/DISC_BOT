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
#         placeholder="Список большой, листай вниз!", 
#         options=[
#         discord.SelectOption(label="0-50 часов", value="hours_1"),
#         discord.SelectOption(label="50+ часов", value="hours_2")
#         ], 
#         custom_id="s_?")
#     async def callback(self, interaction):
#         await interaction.response.defer()
#         print("Ответ?")


# async def check(user):
#     if user.id == message.author.id:
#         return True


####### 1 вопрос #######
async def q_1(user, bot):
    mes = await bot.wait_for('message', check=check(user))
    #await bot.wait_for('message', check=check(user, mes))
    #print(f"Ваш никнейм : {mes.content}")


####### 2 вопрос #######
class q_2(Select):
    def __init__(self):
        super().__init__(
        placeholder="Список большой, листай вниз!", 
        min_values = 1,
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
        placeholder="Список большой, листай вниз!", 
        options=[
        # discord.SelectOption(label="UTC-12:00 (Антивампирский остров)"),
        # discord.SelectOption(label="UTC-11:00 (Самоа)"),
        # discord.SelectOption(label="UTC-10:00 (Гавайи)"),
        # discord.SelectOption(label="UTC-09:00 (Аляска)"),
        # discord.SelectOption(label="UTC-08:00 (Тихоокеанское время - Северная Америка)"),
        # discord.SelectOption(label="UTC-07:00 (Горное время - Северная Америка)"),
        # discord.SelectOption(label="UTC-06:00 (Центральное время - Северная Америка)"),
        # discord.SelectOption(label="UTC-05:00 (Восточное время - Северная Америка)"),
        # discord.SelectOption(label="UTC-04:00 (Атлантическое время - Северная Америка)"),
        # discord.SelectOption(label="UTC-03:00 (Бразилиа, Буэнос-Айрес)"),
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
        discord.SelectOption(label="UTC+12:00 (Фиджи, Камчатское время)")
        # discord.SelectOption(label="UTC+12:45 (Чатемское время)"),
        # discord.SelectOption(label="UTC+13:00 (Тонга)"),
        # discord.SelectOption(label="UTC+14:00 (Линия перемены даты)")
        ], 
        custom_id="s_3")
    async def callback(self, interaction):
        await interaction.response.defer()
        print("Ответ3")


####### 4 вопрос #######
class q_4(Select):
    def __init__(self): 
        super().__init__(
        placeholder="Список большой, листай вниз!", 
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


####### 5 вопрос #######
class q_5(Select):
    def __init__(self): 
        super().__init__(
        placeholder="Список большой, листай вниз!", 
        options=[
        discord.SelectOption(label="CMD подразделение", value="podraz_1"),
        discord.SelectOption(label="Атакующее подразделение", value="podraz_2"),
        discord.SelectOption(label="ДРГ подразделение", value="podraz_3"),
        discord.SelectOption(label="Оборонительное подразделение", value="podraz_4"),
        discord.SelectOption(label="Стройбат подразделение", value="podraz_5"),
        discord.SelectOption(label="Минометное подразделение", value="podraz_6"),
        discord.SelectOption(label="Техническое подразделение", value="podraz_7"),
        discord.SelectOption(label="Пилотное подразделение", value="podraz_8")
        ], 
        custom_id="s_5")
    async def callback(self, interaction):
        await interaction.response.defer()
        print("Ответ5")


####### 6 вопрос #######
class q_6(Select):
    def __init__(self): 
        super().__init__(
        placeholder="Список большой, листай вниз!", 
        options=[
        discord.SelectOption(label="CMD", value="osn_stg_cmd"),
        discord.SelectOption(label="Сквадной", value="osn_stg_sl"),
        discord.SelectOption(label="Лидер Фаер Тимы", value="osn_stg_flt"),
        discord.SelectOption(label="Обычный стрелок", value="osn_stg_rfl"),
        discord.SelectOption(label="Стрелок ГП", value="osn_stg_gl"),
        discord.SelectOption(label="Труба", value="osn_stg_rpg"),
        discord.SelectOption(label="Медик", value="osn_stg_med"),
        discord.SelectOption(label="Пулеметчик", value="osn_stg_mach"),
        discord.SelectOption(label="Такнкист-командир", value="osn_stg_tank_sl"),
        discord.SelectOption(label="Танкист-водитель", value="osn_stg_tnak_mehv"),
        discord.SelectOption(label="Танкист-стрелок", value="osn_stg_tank_bash"),
        discord.SelectOption(label="Пилот", value="osn_stg_pilt")
        ], 
        custom_id="s_6")
    async def callback(self, interaction):
        await interaction.response.defer()
        print("Ответ6")


####### 7 вопрос
class q_7(Select):
    def __init__(self): 
        super().__init__(
        placeholder="Список большой, листай вниз!", 
        min_values = 2,
        max_values = 12,
        options=[
        discord.SelectOption(label="CMD", value="dop_stg_cmd"),
        discord.SelectOption(label="Сквадной", value="dop_stg_sl"),
        discord.SelectOption(label="Лидер Фаер Тимы", value="dop_stg_flt"),
        discord.SelectOption(label="Обычный стрелок", value="dop_stg_rfl"),
        discord.SelectOption(label="Стрелок ГП", value="dop_stg_gl"),
        discord.SelectOption(label="Труба", value="dop_stg_rpg"),
        discord.SelectOption(label="Медик", value="dop_stg_med"),
        discord.SelectOption(label="Пулеметчик", value="dop_stg_mach"),
        discord.SelectOption(label="Такнкист-командир", value="dop_stg_tank_sl"),
        discord.SelectOption(label="Танкист-водитель", value="dop_stg_tnak_mehv"),
        discord.SelectOption(label="Танкист-стрелок", value="dop_stg_tank_bash"),
        discord.SelectOption(label="Пилот", value="dop_stg_pilt")
        ], 
        custom_id="s_7")
    async def callback(self, interaction):
        await interaction.response.defer()
        print("Ответ7")


####### 8 вопрос #######
async def q_8(user, bot):
    mes = await bot.wait_for('message')

####### 9 вопрос #######
async def q_9(user, bot):
    mes = await bot.wait_for('message')


####### 10 вопрос
class q_10(Select):
    def __init__(self): 
        super().__init__(
        placeholder="Список большой, листай вниз!", 
        options=[
        discord.SelectOption(label="0"),
        discord.SelectOption(label="1"),
        discord.SelectOption(label="2"),
        discord.SelectOption(label="3"),
        discord.SelectOption(label="4"),
        discord.SelectOption(label="5"),
        discord.SelectOption(label="6"),
        discord.SelectOption(label="7"),
        discord.SelectOption(label="8"),
        discord.SelectOption(label="9"),
        discord.SelectOption(label="10")
        ], 
        custom_id="s_10")
    async def callback(self, interaction):
        await interaction.response.defer()
        print("Ответ10")


####### 11 вопрос
class q_11(Select):
    def __init__(self): 
        super().__init__(
        placeholder="Список большой, листай вниз!", 
        options=[
        discord.SelectOption(label="0"),
        discord.SelectOption(label="1"),
        discord.SelectOption(label="2"),
        discord.SelectOption(label="3"),
        discord.SelectOption(label="4"),
        discord.SelectOption(label="5"),
        discord.SelectOption(label="6"),
        discord.SelectOption(label="7"),
        discord.SelectOption(label="8"),
        discord.SelectOption(label="9"),
        discord.SelectOption(label="10")
        ], 
        custom_id="s_11")
    async def callback(self, interaction):
        await interaction.response.defer()
        print("Ответ11")


####### 12 вопрос
class q_12(Select):
    def __init__(self): 
        super().__init__(
        placeholder="Список большой, листай вниз!", 
        options=[
        discord.SelectOption(label="0"),
        discord.SelectOption(label="1"),
        discord.SelectOption(label="2"),
        discord.SelectOption(label="3"),
        discord.SelectOption(label="4"),
        discord.SelectOption(label="5"),
        discord.SelectOption(label="6"),
        discord.SelectOption(label="7"),
        discord.SelectOption(label="8"),
        discord.SelectOption(label="9"),
        discord.SelectOption(label="10")
        ], 
        custom_id="s_12")
    async def callback(self, interaction):
        await interaction.response.defer()
        print("Ответ12")


####### 13 вопрос
class q_13(Select):
    def __init__(self): 
        super().__init__(
        placeholder="Список большой, листай вниз!", 
        options=[
        discord.SelectOption(label="Да"),
        discord.SelectOption(label="Нет")
        ], 
        custom_id="s_13")
    async def callback(self, interaction):
        await interaction.response.defer()
        print("Ответ13")


####### 14 вопрос #######
async def q_14(user, bot):
    mes = await bot.wait_for('message')