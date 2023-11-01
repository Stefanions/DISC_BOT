#Файл с основными командами
#Подключение библиотек
import res
import discord
from discord.ext import commands
from discord.ui import Button, View, Select
import numpy as np

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

##############################################Селекты##############################################
s1 = Select(placeholder="Выберите опцию", options=[
    discord.SelectOption(label="Вариант 1", value="option1"),
    discord.SelectOption(label="Вариант 2", value="option2"),
    discord.SelectOption(label="Вариант 3", value="option3")
 ], custom_id="s1")

#### Вопрос 1

# Название вопроса
# Вывод предложеного списка
# Выбор списка
# обработка выбранного
# сохранение выбранного в аргумент
# вызов второго вопроса.

#### конец первого вопроса

#### Вопрос 2
# Название вопроса
# Вывод предложеного списка
# Выбор списка
# обработка выбранного
# сохранение выбранного в аргумент
# вызов третьего вопроса.

#### конец первого вопроса


# @bot.event
# async def on_select(ctx, interaction):
#     if interaction.custom_id == 'menu':
#         selected_option = interaction.values[0]
#         await interaction.response.send_message(f'Вы выбрали: {selected_option}', ephemeral=True)
        
#         # Вызываем другую функцию
#         await some_other_function(ctx, selected_option)



###########################################Функциии разные########################################
#Функция разговора бота в ЛС
async def Intro_LS(user):
    await user.send("Приветсвую тебя в нашей команде ССО!!!\n Пройди небольшой тест.")
    await q1(user)
 
############################## вопрос 1  ######################################

async def q1(user):
    # Шаг 1: Выводим эмбед сообщение
    e = discord.Embed(title="Вопрос 1")
    # Шаг 2: Выводим меню s1
    s1 = Select(placeholder="Выберите опцию", options=[
        discord.SelectOption(label="Вариант 1", value="option1"),
        discord.SelectOption(label="Вариант 2", value="option2"),
        discord.SelectOption(label="Вариант 3", value="option3")
    ])
    s = View()
    s.add_item(s1)
    await user.send(embed=e, view = s)

    # Шаг 3: Ожидаем выбор пользователя и сохраняем в аргумент answer1
    async def check(s1):
        print("HUY1")
        return s1.custom_id == "s1"
    print("asda")
    await bot.wait_for("s1_option", check=check)
    print("HUY2")
    answer1 = interaction.values[0]  # Первый выбранный элемент
    await user.send(answer1)

    # Шаг 4: Вызываем следующую функцию
    #await sleduyushaya_func(ctx, answer1)

##############################вопрос 2######################################
    
# async def my_function(ctx):
#     # Шаг 1: Выводим эмбед сообщение
#     embed = discord.Embed(title="Пример эмбеда", description="Это пример эмбед сообщения.")
#     await ctx.send(embed=embed)

#     # Шаг 2: Выводим меню s1
#     s1 = Select(placeholder="Выберите опцию", options=[
#         discord.SelectOption(label="Вариант 1", value="option1"),
#         discord.SelectOption(label="Вариант 2", value="option2"),
#         discord.SelectOption(label="Вариант 3", value="option3")
#     ])
#     await ctx.send(components=[s1])

#     # Шаг 3: Ожидаем выбор пользователя и сохраняем в аргумент answer1
#     def check(interaction):
#         return interaction.author == ctx.author and interaction.custom_id == "s1"

#     interaction = await bot.wait_for("select_option", check=check)
#     answer1 = interaction.values[0]  # Первый выбранный элемент

#     # Шаг 4: Вызываем следующую функцию
#     await sleduyushaya_func(ctx, answer1)

##################################################################################
       
    
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
    

#Команды основные
#Тестовая 1
@bot.command()
async def Hi(ctx):
    await ctx.send("ССО хай, это моя первая команда")

#Приветствие в лс
@bot.command()
async def LS(ctx):
    if (ctx.channel.id == 1168950770364858427):
        await ctx.author.send("Приветствую в нашей команде ССО!!!\nПеред тем как начать с нами играть, нам нужно узнать про тебя немнго больше.\nОтветь на пару вопросов.")


bot.run(res.token)




