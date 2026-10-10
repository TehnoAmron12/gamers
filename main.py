import telebot
from config import BOT_TOKEN
from logic import Pokemon, Gamer

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['go'])
def start_game(message):
    username = message.from_user.username
    if not username:
        bot.reply_to(message, "⚠️ Для игры укажи @username в настройках своего Telegram профиля!")
        return

    if username not in Gamer.gamers:
        Gamer(name=message.from_user.first_name, age=18, nickname=username, email=f"{username}@tg.com")

    if username not in Pokemon.pokemons:
        pokemon = Gamer.catch_pokemon_from_api(username)
        welcome_text = f"🎮 Тренер @{username} успешно зарегистрирован!\n\n🤖 Твой первый покемон:\n{pokemon.info()}"
        if pokemon.rarity == "Легендарный":
            welcome_text += f"\n\n✨ Ты получил 1 Супер-Бонус Жетон за Легендарного покемона!"
        bot.send_message(message.chat.id, welcome_text)
    else:
        bot.reply_to(message, "❌ У тебя уже есть покемон! Используй /my_pokemon, чтобы посмотреть информацию.")


@bot.message_handler(commands=['my_pokemon'])
def show_my_pokemon(message):
    username = message.from_user.username
    if username in Pokemon.pokemons:
        bot.reply_to(message, Pokemon.pokemons[username].info(), parse_mode="Markdown")
    else:
        bot.reply_to(message, "🤷‍♂️ У тебя еще нет покемона. Напиши /go, чтобы поймать его!")


@bot.message_handler(commands=['feed'])
def feed_pokemon(message):
    username = message.from_user.username
    if username in Pokemon.pokemons:
        pok = Pokemon.pokemons[username]
        exp, lvl_up = pok.feed()
        res_msg = f"🍬 Ты покормил покемона {pok.name}!\nПолучено: +{exp} ОП (Всего: {pok.experience} ОП)."
        if lvl_up:
            res_msg += f"\n\n🎉 УРОВЕНЬ ПОВЫШЕН! Теперь у {pok.name} **{pok.level} уровень**! Силы восстановлены!"
            pok.hp += 15
        bot.reply_to(message, res_msg)
    else:
        bot.reply_to(message, "❌ Сначала поймай покемона командой /go")


@bot.message_handler(commands=['attack'])
def attack_handler(message):
    if not message.reply_to_message:
        bot.reply_to(message, "⚠️ Чтобы атаковать, ответь на сообщение другого игрока командой `/attack`.")
        return

    attacker = message.from_user.username
    target = message.reply_to_message.from_user.username

    if not attacker or not target:
        bot.reply_to(message, "❌ У обоих участников дуэли должен быть настроен @username!")
        return

    if attacker == target:
        bot.reply_to(message, "🤨 Зачем атаковать самого себя? Найди соперника!")
        return

    if attacker in Pokemon.pokemons and target in Pokemon.pokemons:
        my_pokemon = Pokemon.pokemons[attacker]
        enemy_pokemon = Pokemon.pokemons[target]
        battle_result = my_pokemon.attack(enemy_pokemon)
        bot.send_message(message.chat.id, battle_result)
    else:
        bot.send_message(message.chat.id, "❌ Сражаться могут только тренеры, у которых созданы покемоны (/go).")


@bot.message_handler(commands=['heal'])
def heal_handler(message):
    username = message.from_user.username
    if username in Pokemon.pokemons:
        pok = Pokemon.pokemons[username]
        heal_msg = pok.heal()
        bot.reply_to(message, heal_msg)
    else:
        bot.reply_to(message, "❌ У тебя нет покемона, которого можно исцелить.")


if __name__ == '__main__':
    bot.infinity_polling()
