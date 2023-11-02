class AnswerView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

        # Добавляем поле ввода
        self.input_field = discord.ui.TextInput(
            placeholder="Введите ваш ответ...",
            min_length=1,  # Минимальная длина ответа (в данном случае, 1 символ)
            max_length=100  # Максимальная длина ответа (в данном случае, 100 символов)
        )
        self.add_item(self.input_field)

@bot.command()
async def ask(ctx):
    # Создаем экземпляр класса с полем для ввода
    view = AnswerView()

    # Отправляем сообщение с полем для ввода в личные сообщения пользователя
    await ctx.author.send("Пожалуйста, введите ваш ответ:", view=view)

    # Ожидаем ответа пользователя
    response = await bot.wait_for("message", check=lambda message: message.author == ctx.author and message.channel.type == discord.ChannelType.private)

    # Печатаем ответ в консоль для демонстрации
    print(f"Получен ответ: {response.content}")

    # Опционально, можно отправить подтверждение о получении ответа
    await ctx.author.send(f"Спасибо за ваш ответ: {response.content}")
