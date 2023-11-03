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
import class_novob

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
        print("main_but")
        await Clean_and_Intro_LS(interaction.user)

#Кнопка после ввода ответов на тест
class main_resualt_but(View):
    @discord.ui.button(label = "Посмотреть результат опроса", style=discord.ButtonStyle.danger)
    async def button_callback(self, interaction, button):
        await interaction.response.defer()




###########################################Функциии разные########################################

#Для отслеживания людей, которые не прошли собеседование в личных сообщений бота до конца
mem_not_end_opr = []

#Очистка сообщений + вызов функции
async def Clean_and_Intro_LS(user):

    #Проверка на то что пользователь ещё не проходит тест
    if ((user.id in mem_not_end_opr) and (user.id in mem_data)):
        return
    else:
        mem_not_end_opr.append(user.id)
        question.mem_data[user.id] = class_novob.novob(user.id)

    # #Удаление сообщений
    # await user.send("Привет")
    # channel = bot.get_channel(user.dm_channel.id)
    # async for message in channel.history(limit=None):
    #     if message.author.id == bot.user.id:
    #         try:
    #             await message.delete()
    #         except discord.errors.NotFound:
    #             pass

    await Intro_LS(user)

#Функция прохождения первого собеседования в личных сообщения бота
async def Intro_LS(user):
    #Проверка на выбор селекта 
    def check(interaction):
        custom_id = interaction.data['custom_id']
        return ((interaction.user.id == user.id) and (interaction.channel.id == user.dm_channel.id) and (custom_id == sel))

    #Тут создаю окошечко для наших селектов и строк
    s = View()
    
    #Приветственное сообщение
    await user.send(embed=embed.emb_1)
    
    #### 1 вопрос
    e_1 = embed.emb_2("Напиши свой никнейм в игре.")
    await user.send(embed=e_1.emb)
    await question.q_1(user, bot)

    #### 2 вопрос rdy 
    sel = "s_2"
    s.clear_items()
    e_2 = embed.emb_2("В какое время относительно МСК ты играешь в основном?")
    s.add_item(question.q_2())
    await user.send(embed=e_2.emb, view = s)
    await bot.wait_for('interaction', check=check)

    #### 3 вопрос rdy
    sel = "s_3"
    s.clear_items()
    s.add_item(question.q_3())
    e_3 = embed.emb_2("Какой у тебя часовой пояс?")
    await user.send(embed=e_3.emb, view = s)
    await bot.wait_for('interaction', check=check)



    #### 4 вопрос rdy
    sel = "s_4"
    s.clear_items()
    s.add_item(question.q_4())
    e_4 = embed.emb_2("Сколько у тебя часов в SQUAD?")
    await user.send(embed=e_4.emb, view = s)
    await bot.wait_for('interaction', check=check)

    

    #### 5 вопрос rdy
    sel = "s_5"
    s.clear_items()
    s.add_item(question.q_5())
    e_5 = embed.emb_2("Какое направление тебе нравится больше всего?")
    await user.send(embed=e_5.emb, view = s)
    await bot.wait_for('interaction', check=check)

    # print(question.mem_data[user.id].id_hours)
    # print(question.mem_data[user.id].hours)
    #### 6 вопрос rdy
    sel = "s_6"
    s.clear_items()
    s.add_item(question.q_6())
    e_6 = embed.emb_2("Выбери одну роль (стрелковую специальность), номер один для тебя?")
    await user.send(embed=e_6.emb, view = s)
    await bot.wait_for('interaction', check=check)

    #### 7 вопрос rdy
    sel = "s_7"
    s.clear_items()
    s.add_item(question.q_7())
    e_7 = embed.emb_2("Выбери дополнительные 2 или более роли, помимо основной. Напиши их ниже.")
    await user.send(embed=e_7.emb, view = s)
    await bot.wait_for('interaction', check=check)
    
    #### 8 вопрос
    sel = "s_8"
    s.clear_items()
    e_8 = embed.emb_2("Ты понимаешь, что для того, что бы играть командно, нужно, что бы все делали одинаково?\nЭто \"одинаково\" - мы научим тебя делать, но не все может получатся сразу")
    await user.send(embed=e_8.emb)
    await question.q_8(user, bot)

    #### 9 вопрос   
    sel = "s_9" 
    s.clear_items()
    e_9 = embed.emb_2("Сколько тебе лет?")
    await user.send(embed=e_9.emb)
    await question.q_9(user, bot)

    #### 10 вопрос rdy
    sel = "s_10"
    s.clear_items()
    e_10 = embed.emb_2("Оцени самостоятельно навык твоей стрельбы в SQUAD? от 0 до 10")
    s.add_item(question.q_10())
    await user.send(embed=e_10.emb, view = s)
    await bot.wait_for('interaction', check=check)

    #### 11 вопрос rdy
    sel = "s_11"
    s.clear_items()
    e_11 = embed.emb_2("Насколько ты считаешь себя дисциплинированным игроком, если играешь в отряде? От 0 до 10")
    s.add_item(question.q_11())
    await user.send(embed=e_11.emb, view = s)
    await bot.wait_for('interaction', check=check)

    #### 12 вопрос rdy
    sel = "s_12"
    s.clear_items()
    e_12 = embed.emb_2("Как ты считаешь, насколько ты хорош при радиообмене от 0 до 10?")
    s.add_item(question.q_12())
    await user.send(embed=e_12.emb, view = s)
    await bot.wait_for('interaction', check=check)

    #### 13 вопрос rdy
    sel = "s_13"
    s.clear_items()
    e_13 = embed.emb_2("Ты хочешь играть серьезные игры в SQUAD? (Считай что это киберспорт, но только в скваде)")
    s.add_item(question.q_13())
    await user.send(embed=e_13.emb, view = s)
    await bot.wait_for('interaction', check=check)

    #### 14 вопрос
    sel = "s_14"
    s.clear_items()
    e_14 = embed.emb_2("Откуда вы о нас узнали?\nЕсли вас пригласили, обязательно напишите ник человека, кто это сделал (Хотя бы примерный, мы поймем xD)")
    await user.send(embed=e_14.emb)
    await question.q_14(user, bot)


    #Результирующая кнопка 
    but_rez = main_resualt_but()
    await user.send(view=but_rez)
    #Проверка на нажатие на кнопку результирующую тест
    def check_in_end(interaction):
        return ((interaction.user.id == user.id) and (interaction.channel.id == user.dm_channel.id) and (interaction.data['component_type'] == 2))
    await bot.wait_for('interaction', check=check_in_end)

    #Удаление кнопки
    channel = bot.get_channel(user.dm_channel.id)
    async for message in channel.history(limit=1):
        if message.author.id == bot.user.id:
            try:
                await message.delete()
            except discord.errors.NotFound:
                pass

    # #Эмбед результирующий
    # emb_rez = discord.Embed(
    # title="Вы прошли тест и выбрали следующие результаты",
    # description=
    # (
    #     "Ваши роли\n" 

    #     "Ваши роли\n" ""



        
    #     # f"{question.mem_data[user.id].game_role}"  
    # ),
    #     color=discord.Color.from_rgb(255, 255, 255) # ебашим белой полосочкой, иначе некрасиво)
    # )
    # await user.send(embed=emb_rez)

    del question.mem_data[user.id]
    mem_not_end_opr.remove(user.id)
    return






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
