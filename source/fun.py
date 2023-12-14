import random
import sqlite3
import time
import ranks


def getRoles(author):
    roles = ""
    for i in range(len(author.roles)):
        roles += str(author.roles[i]) + " "
    return roles


# Пассивные фунции

def mess(com):
    print("Выполнена комманда " + com)


def checkmessage(message_):
    # преобразование текста в массив слов.

    message_ += ' '
    messagewords = get_array_of_words(message_)

    text = open('../data/words.dat', 'r', encoding='utf-8')
    l = text.read()
    badwords = get_array_of_words(l)
    text.close()

    i = 0
    for i in range(len(messagewords)):
        j = 0
        for j in range(len(badwords)):
            if messagewords[i] == badwords[j]:
                return True


def uprank(name):
    # получение массива списска рангов и очков для ранга.
    _ranks = ranks.r
    _score = ranks.scores
    # узнать ранг чела
    sql.execute(f"SELECT xp,rank FROM users WHERE nicknames = \"{name}\"")
    s = sql.fetchone()
    user_xp, user_rank = s[0], s[1]

    if user_rank == 'Титан':
        return [False, '']  # если у чела максимальный ранк остановить функцию(ЭТО ВАЖНО)

    i = 0
    while user_xp >= _score[i]:
        i += 1
    i -= 1

    if user_rank != _ranks[i]:
        sql.execute(f"""UPDATE users SET rank = \"{_ranks[i]}\" WHERE nicknames = \"{name}\"""")
        db.commit()
        return [True, _ranks[i]]
    else:
        return [False, '']


# Функции комманд

# Топ 10 сообщений
def topmessages():
    count_of_printed_users = 0
    maxm = 0
    data = []
    for v in sql.execute("SELECT * FROM users"):
        if maxm < v[1]:
            maxm = v[1]
    for i in range(maxm, 0, -1):
        sql.execute(f"SELECT nicknames, messages,rank FROM users WHERE messages = {i}")
        x = sql.fetchone()
        if x != None:
            count_of_printed_users += 1
            data.append(x)
            if count_of_printed_users == 10:
                break
    s = "```\n"
    for i in range(len(data)):
        s += f"{i + 1}. {data[i][2]} {data[i][0]} - {data[i][1]}\n"
    s += "```"
    return s


# обо мне
def me(author):
    sql.execute(f"SELECT * FROM users WHERE nicknames = \"{author}\"")
    s = sql.fetchone()
    info = f"```{s[6]} {s[0]}.\nРоли на сервере: {getRoles(author)}\nКоличество сообщений: {s[1]}\nМинут в войс чатах: {s[2]} \nКоличество очков опыта: {s[5]}\nС нами с: {s[3]}```"
    return info


# орел или решка
def flip():
    if (random.randrange(2) == 0):
        flips = "*ОРЁЛ*"
    else:
        flips = "*РЕШКА*"

    return flips


# случайное число от 0 до 100
def roll(*args):
    try:
        return random.randrange(int(args[0][0]), int(args[0][1]) + 1)
    except:
        try:
            return random.randrange(int(args[0][0]) + 1)
        except:
            return random.randrange(101)


def prediction():
    s = ranks.predictions[random.randrange(len(ranks.predictions))]
    return s


# Помощь
def help():
    s = "flip - подбросить монетку\nroll - рандомное число от 0 до 100\ntop - топ 10 участников по сообщениям\nme - вся информация о тебе\nprediction - бот получил способности прорицания)\nhelp - а это я, команда - помощник))"
    return s


def main():
    pass


if __name__ == "__main__":
    main()
