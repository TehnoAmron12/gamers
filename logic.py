import random

class Pokemon:
    pokemons = {}

    def __init__(self, name: str, pokemon_type: str, rarity: str = "Обычный", trainer_name: str = None):
        self.name = name
        self.pokemon_type = pokemon_type
        self.rarity = rarity
        self.level = 1
        self.experience = 0
        self.fed_count = 0
        self.pokemon_trainer = trainer_name
        self.hp = random.randint(50, 100)
        self.power = random.randint(10, 20)
        self.wins = 0

        if trainer_name:
            Pokemon.pokemons[trainer_name] = self

    def info(self):
        return (f"Имя: {self.name} | Тип: {self.pokemon_type}\n"
                f"💎 Редкость: {self.rarity}\n"
                f"❤️ Здоровье (HP): {self.hp}\n"
                f"⚔️ Сила (Power): {self.power}\n"
                f"📊 Уровень: {self.level} | 🏆 Побед: {self.wins}")

    def feed(self):
        self.fed_count += 1
        gained_exp = random.randint(15, 35)
        if self.rarity == "Легендарный":
            gained_exp += 20  
            
        self.experience += gained_exp
        level_up = False
        if self.experience >= self.level * 50:
            self.level += 1
            level_up = True
        return gained_exp, level_up

    def attack(self, enemy):
        if self.hp <= 0:
            return f"❌ @{self.pokemon_trainer}, твой покемон повержен! Исцели его через /heal."
        if enemy.hp <= 0:
            return f"🛡️ Покемон тренера @{enemy.pokemon_trainer} уже без сил! Выбери другого противника."

        if isinstance(enemy, Wizard):
            chance = random.randint(1, 5)
            if chance == 1:
                return f"🔮 Волшебник {enemy.name} (@{enemy.pokemon_trainer}) активировал Магический Щит и заблокировал весь урон!"

        if enemy.hp > self.power:
            enemy.hp -= self.power
            return f"💥 {self.name} (@{self.pokemon_trainer}) атаковал {enemy.name} (@{enemy.pokemon_trainer}) на {self.power} HP! У врага осталось {enemy.hp} HP."
        else:
            enemy.hp = 0
            self.wins += 1
            self.power += 5
            self.hp += 20
            return (f"👑 ПОБЕДА! {self.name} (@{self.pokemon_trainer}) одолел {enemy.name} (@{enemy.pokemon_trainer})!\n"
                    f"🎁 Награда: +5 к силе и +20 к HP!")

    def heal(self):
        if isinstance(self, Wizard):
            max_hp = 150
        elif isinstance(self, Fighter):
            max_hp = 90
        elif isinstance(self, Warlock):
            max_hp = 110
        else:
            max_hp = 100
        
        if self.hp >= max_hp:
            return f"❤️ Твой покемон {self.name} полностью здоров ({self.hp}/{max_hp} HP)!"
        
        self.hp = max_hp
        return f"✨ Регенерация! {self.name} полностью восстановил здоровье до {max_hp} HP!"


class Wizard(Pokemon):
    def __init__(self, name: str, pokemon_type: str, rarity: str = "Обычный", trainer_name: str = None):
        super().__init__(name, pokemon_type, rarity, trainer_name)
        self.hp = random.randint(110, 150)
        self.power = random.randint(8, 15)

    def info(self):
        return "🔮 **Класс: ВОЛШЕБНИК**\n" + super().info()


class Fighter(Pokemon):
    def __init__(self, name: str, pokemon_type: str, rarity: str = "Обычный", trainer_name: str = None):
        super().__init__(name, pokemon_type, rarity, trainer_name)
        self.hp = random.randint(60, 90)
        self.power = random.randint(18, 28)

    def info(self):
        return "🥊 **Класс: БОЕЦ**\n" + super().info()

    def attack(self, enemy):
        if self.hp <= 0:
            return f"❌ @{self.pokemon_trainer}, твой покемон повержен!"
            
        super_power = random.randint(5, 15)
        self.power += super_power
        result = super().attack(enemy)
        self.power -= super_power
        
        if "заблокировал весь урон" not in result and "без сил" not in result:
            return result + f"\n⚡ Боец применил супер-удар силой: +{super_power}!"
        return result


class Warlock(Pokemon):
    def __init__(self, name: str, pokemon_type: str, rarity: str = "Обычный", trainer_name: str = None):
        super().__init__(name, pokemon_type, rarity, trainer_name)
        self.hp = random.randint(80, 110)
        self.power = random.randint(12, 22)

    def info(self):
        return "🧙‍♂️ **Класс: ЧЕРНОКНИЖНИК**\n" + super().info()

    def attack(self, enemy):
        if self.hp <= 0:
               return f"❌ @{self.pokemon_trainer}, твой покемон повержен! Исцели его через /heal."
        if enemy.hp <= 0:
               return f"🛡️ Покемон тренера @{enemy.pokemon_trainer} уже без сил! Выбери другого противника."

        if type(enemy).__name__ == "Wizard":
             chance = random.randint(1, 5)
        if chance == 1:
             return f"🔮 Волшебник {enemy.name} (@{enemy.pokemon_trainer}) активировал Магический Щит и заблокировал весь урон!"

        if enemy.hp > self.power:
                enemy.hp -= self.power
                return f"💥 {self.name} (@{self.pokemon_trainer}) атаковал {enemy.name} (@{enemy.pokemon_trainer}) на {self.power} HP! У врага осталось {enemy.hp} HP."
        else:
            enemy.hp = 0
            self.wins += 1
            self.power += 5
            self.hp += 20
            return (f"👑 ПОБЕДА! {self.name} (@{self.pokemon_trainer}) одолел {enemy.name} (@{enemy.pokemon_trainer})!\n"
                    f"🎁 Награда: +5 к силе и +20 к HP!")
        
        return result


class Gamer:
    gamers = {}

    def __init__(self, name, age, nickname, email):
        self.name = name
        self.age = age
        self.nickname = nickname
        self.email = email
        self.super_bonus_tokens = 0
        Gamer.gamers[nickname] = self

    @staticmethod
    def catch_pokemon_from_api(trainer_username):
        mock_api_pool = [
            {"name": "Pikachu", "type": "Electric"},
            {"name": "Charizard", "type": "Fire"},
            {"name": "Bulbasaur", "type": "Grass"},
            {"name": "Mewtwo", "type": "Psychic"}
        ]
        chosen = random.choice(mock_api_pool)
        
        roll = random.randint(1, 100)
        rarity = "Легендарный" if roll > 75 else "Обычный"
        
        if rarity == "Легендарный" and trainer_username in Gamer.gamers:
            Gamer.gamers[trainer_username].super_bonus_tokens += 1

        class_roll = random.randint(1, 10)
        if class_roll == 1:
            new_pokemon = Wizard(name=chosen["name"], pokemon_type=chosen["type"], rarity=rarity, trainer_name=trainer_username)
        elif class_roll == 2:
            new_pokemon = Fighter(name=chosen["name"], pokemon_type=chosen["type"], rarity=rarity, trainer_name=trainer_username)
        elif class_roll == 3:
            new_pokemon = Warlock(name=chosen["name"], pokemon_type=chosen["type"], rarity=rarity, trainer_name=trainer_username)
        else:
            new_pokemon = Pokemon(name=chosen["name"], pokemon_type=chosen["type"], rarity=rarity, trainer_name=trainer_username)
            
        return new_pokemon
