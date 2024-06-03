# Лабораторная работа 2
# Ревва Евгений
# Вариант 8
import telebot
import random

students = {
    'Мурзик': {"attendance": ['Я' if random.randint(0, 1) == 1 else 'Н' for _ in range(7)],
                  "scores": [random.randint(2, 5) for _ in range(7)]},
    'Тимка': {"attendance": ['Я' if random.randint(0, 1) == 1 else 'Н' for _ in range(7)],
                  "scores": [random.randint(2, 5) for _ in range(7)]},
    'Нико': {"attendance": ['Я' if random.randint(0, 1) == 1 else 'Н' for _ in range(7)],
                  "scores": [random.randint(2, 5) for _ in range(7)]}
}

selected_student = None

bot = telebot.TeleBot("6521270940:AAG9kwjpkYBaNoZ4JztlnjlNBEYg-1QSsQY")

@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.reply_to(message, "Привет! Я бот для учета посещаемости и баллов студентов. Используй команду /help для получения списка доступных команд.")

@bot.message_handler(commands=['show'])
def handle_show_students(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True)
    for name in students.keys():
        keyboard.add(name)
    bot.send_message(message.chat.id, "Выберите студента:", reply_markup=keyboard)

@bot.message_handler(func=lambda message: message.text in students.keys())
def handle_select_student(message):
    global selected_student
    selected_student = message.text

    attendance = ', '.join(students[selected_student]["attendance"])
    scores = ', '.join(map(str, students[selected_student]["scores"]))

    response = f"Посещаемость за 7 дней для {selected_student}: {attendance}\n\nОценки за 7 дней для {selected_student}: {scores}"
    bot.reply_to(message, response)

@bot.message_handler(commands=['help'])
def handle_help(message):
    bot.reply_to(message, "Доступные команды:\n/show - показать список студентов\n/help - список команд")

@bot.message_handler(func=lambda message: True)
def handle_unknown(message):
    bot.reply_to(message, "Неизвестная команда. Используй команду /help для получения списка доступных команд.")

bot.polling()