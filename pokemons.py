from logic import Wizard, Fighter

if __name__ == "__main__":
    print("--- Создание покемонов для тренеров ---")
    wizard_pika = Wizard(name="Pikachu", pokemon_type="Electric", trainer_name="john_wizard")
    fighter_char = Fighter(name="Charizard", pokemon_type="Fire", trainer_name="alex_fighter")

    print(wizard_pika.info())
    print("-" * 30)
    print(fighter_char.info())
    print("-" * 30)

    print("\n--- Начало сражения ---")
    print(fighter_char.attack(wizard_pika))
    print()
    print(wizard_pika.attack(fighter_char))
    
    print("\n--- Проверка восстановления ---")
    print(wizard_pika.heal())
