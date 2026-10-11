import random

class Pokemon:
    def __init__(self, name: str, pokemon_type: str, rarity: str = "Обычный"):
        self.name = name
        self.pokemon_type = pokemon_type
        self.rarity = rarity
        self.level = 1
        self.experience = 0
        self.fed_count = 0

    def feed(self):
        self.fed_count += 1
        gained_exp = random.randint(15, 35)
        
        if self.rarity == "Легендарный":
            gained_exp += 20  
            print(f"✨ СУПЕР-БОНУС! Легендарный {self.name} получает дополнительный опыт!")
            
        self.experience += gained_exp
        print(f"🍬 Вы покормили {self.name}. Получено {gained_exp} ОП. Всего: {self.experience} ОП.")
        
        if self.experience >= self.level * 50:
            self.level += 1
            print(f"🎉 СУПЕР! {self.name} вырос до {self.level}-го уровня!")
            self.check_achievements()

    def check_achievements(self):
        if self.level == 5:
            print(f"🏆 ДОСТИЖЕНИЕ: 'Начинающий тренер' — {self.name} достиг 5 уровня!")
        elif self.level == 10:
            print(f"🏆 ДОСТИЖЕНИЕ: 'Мастер эволюции' — {self.name} достиг 10 уровня!")


class Gamer:
    def __init__(self, name, age, nickname, email):
        self.name = name
        self.age = age
        self.nickname = nickname
        self.email = email
        self.games = []
        self.pokemons = []
        self.super_bonus_tokens = 0

    def add_game(self, game):
        self.games.append(game)

    def introduce(self):
        return (
            f"Привет, меня зовут {self.name}, мне {self.age} лет. "
            f"Всегда на связи по {self.email}. "
            f"Ищи меня в игре по нику {self.nickname}"
        )

    def catch_pokemon_from_api(self):
        print(f"\n🔍 {self.nickname} отправляет запрос к PokeAPI для поиска покемона...")
        
        mock_api_pool = [
            {"name": "Pikachu", "type": "Electric"},
            {"name": "Charizard", "type": "Fire"},
            {"name": "Bulbasaur", "type": "Grass"},
            {"name": "Mewtwo", "type": "Psychic"}
        ]
        
        chosen = random.choice(mock_api_pool)
        
        roll = random.randint(1, 100)
        if roll > 75:
            rarity = "Легендарный"
            self.super_bonus_tokens += 1
            bonus_msg = f"🌟 ВАУ! Выпал ЛЕГЕНДАРНЫЙ покемон! Получен 1 Супер-Бонус Жетонов (Всего: {self.super_bonus_tokens})!"
        else:
            rarity = "Обычный"
            bonus_msg = "Вам попался обычный дикий покемон."

        new_pokemon = Pokemon(name=chosen["name"], pokemon_type=chosen["type"], rarity=rarity)
        self.pokemons.append(new_pokemon)
        
        print(f"🎮 Пойман покемон: {new_pokemon.name} ({new_pokemon.pokemon_type}). Редкость: {new_pokemon.rarity}!")
        print(bonus_msg)
        return new_pokemon
    pass

if __name__ == "__main__":
    gamer1 = Gamer("Иван", 14, "John", "john@gmail.com")
    
    gamer1.add_game("Minecraft")
    gamer1.add_game("Dota 2")
    
    print(gamer1.introduce())
    print(f"{gamer1.name} любит игры: {', '.join(gamer1.games)}")
    
    my_pokemon = gamer1.catch_pokemon_from_api()
    print(f"\n--- Начинаем прокачку {my_pokemon.name} ---")
    for _ in range(4):
        my_pokemon.feed()
