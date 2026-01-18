
from config import *

top_health = 100

hero_stats = {
    "health": 100,
    "attak": 25,
    "defense": 40,
    "level_pers":0,
    "experience":0,
    "X_place": 0,
    "Y_place": 0,
    "hero_symbol": "🧙"
}
inventory = {
    "🍎" : 0,
    "🔮" : 0,
    "📜" : 0,
    "💎" : 0
}

enemies_coordinates = [
    [1,2],[2,2],[4,3],[6,4],[6,17],[8,17],[7,16],[8,29],[11,4],[11,8],[12,15],[12,9],[12,14],[13,6],[13,8],[14,9],[14,1],[3,6],[3,28],[4,9],[4,11],[4,0],[6,24],[6,26],[9,0]
]

vampire_coordinats = [
    [4,5],
    [1,6],
    [1,19],
    [1,28],
    [0,14],
    [0,29],
    [10,8],
    [11,19],
    [11,16],
    [14,4],
    [13,27],
    [0,7],
    [0,8],
    [1,9],
    [2,7],
    [2,8],
    [3,4],[9,19],[9,21],[3,13],[8,13],[5,13]
]

dragon_coordinats = [[9,29]]

heal_coordinates = [
    [4,6],
    [1,7],
    [7,8],
    [3,15],
    [13,28],
    [14,10],
    [10,1],
    [3,5],
    [4,10],
    [3,29]
]

magic_ball = [
    [9,27],
    [7,17],
    [14,5],
    [10,19],
    [11,17],
    [5,0],
    [6,25]
]

scroll_coordinates = [
    [1,14],
    [3,19],
    [9,5],
    [11,29],
    [4,18],
    [8,0],
    [9,20]
]

diamond_coordinates = [
    [1,8],
    [6, 19],
    [8,4],
    [8,7],
    [5, 18],
    [7,1],
    [3,15],
    [14,0],
    [10,0]
]

city_coordinates = [0,1]

store_content = {
    "🛡️": [1, 5, "броня", 1],
    "🔪": [3, 5, "атака", 2],
    "🗡️": [5, 10, "атака", 3],
    "🏹": [10, 20, "атака", 4],
    "🛡️✨": [15, 20, "броня", 5],
    "⚔️": [17, 50, "атака", 6],
}

price = {
   "📜":3,
   "🔮":4
}



def draw(character_X, character_Y,  enemies_coordinates): #функция отрисовки карты 
    
    print("Карта")
    
    map = []

    for i in range(MAP_HEIGHT):
        map_st = []
        for j in range(MAP_WIDTH):
            map_st.append(MAP_SYMBOL)
        map.append(map_st)

    map[character_Y][character_X] = hero_stats["hero_symbol"] #координаты героя  
    
    for en in enemies_coordinates:
        map[en[0]][en[1]] = ENEMY_SYMBOL #координаты противников 

    for heal_iter in heal_coordinates:
        map[heal_iter[0]][heal_iter[1]] = HEAL_SYMBOL #координаты аптечек 

    for ball_iter in magic_ball:
        map[ball_iter[0]][ball_iter[1]] = MAGIC_SYMBOL

    for scroll_iter in scroll_coordinates:
        map[scroll_iter[0]][scroll_iter[1]] = SCROLL_SYMBOL
    
    for diamond_iter in diamond_coordinates:
        map[diamond_iter[0]][diamond_iter[1]] = DIAMOND_SYMBOL

    for vampir_iter in vampire_coordinats:
        map[vampir_iter[0]][vampir_iter[1]] = VAMPIRE_SYMBOL


    if len(dragon_coordinats) != 0:
        map[dragon_coordinats[0][0]][dragon_coordinats[0][1]] = DRAGON_SYMBOL
    

    map[city_coordinates[0]][city_coordinates[1]] = CITY_SYMBOL
    

    for map_iter in map:
        print("".join(map_iter))
    

def calculate_damage(attack, target_defence): #Функция подсчёта урона
    if attack - (attack/100)*target_defence >= 0: #добавил чтобы не было отрицательного урона, если броня сильно больше чем атака 
        return attack - (attack/100)*target_defence
    else:
       return 0 


def fight(character_hp:int, #Функция битвы 
          character_atk:int,
          character_def:int,
          enemy_hp_fight:int,
          enemy_atk_fight:int,
          enemy_def_fight:int,
          verbose:bool):
    
    if verbose:print("Начинается бой!")

    while True:
        
       #удар персонажа

       enemy_hp_fight -= calculate_damage(character_atk, enemy_def_fight)
       if verbose: print(f"Персонаж бьёт с атакой {character_atk} против защиты {enemy_def_fight}, наносит {calculate_damage(character_atk, enemy_def_fight)} урона")
       if enemy_hp_fight == 0 or enemy_hp_fight < 0:
           if verbose: print(f"Победа! У персонажа осталось {character_hp}")
           return character_hp
           break
       
       #удар противника

       character_hp -= calculate_damage(enemy_atk_fight, character_def)
       if verbose: print(f"Противник бьёт с атакой {enemy_atk_fight} против защиты {character_def}, наносит {calculate_damage(enemy_atk_fight, character_def)} урона")
       if character_hp == 0 or character_hp < 0:
           if verbose: print("Поражение! Игра окончена!")
           return 0
           break
       
    if verbose:print(f"У героя осталось {character_hp} очков здоровья")
       
#Функция 

def inventory_contents():#Функция инвентаря
    print("Инвентарь:")
    for inv_key, inv_values in inventory.items():
        print(f"{inv_key} - {inv_values}")

def healing():#Функция аптечки 
    if inventory[HEAL_SYMBOL] > 0 and hero_stats["health"] < top_health:
        if hero_stats["health"] + HEAL_VALUES > top_health: #чтобы здоровье больше TOP_HEALTH не получалось
            hero_stats["health"] = top_health 
        else:
            hero_stats["health"] += HEAL_VALUES
        inventory[HEAL_SYMBOL] -= 1
        print(f"Вы использовали аптечку! Теперь у героя {hero_stats["health"]} очков здоровья.")
    elif inventory[HEAL_SYMBOL] == 0:
        print("У вас нет аптечек!")
    elif hero_stats["health"] == top_health:
        print("Герой здоров! Лечение не требуется!")


def artifact_selection(): #Функция сбора артефактов 
    for mag_sel_iter in magic_ball:
        if hero_stats["X_place"] == mag_sel_iter[1] and hero_stats["Y_place"] == mag_sel_iter[0]:
            inventory[MAGIC_SYMBOL] += 1
            del magic_ball[magic_ball.index(mag_sel_iter)]
            print("Вы подобрали магический шар!")
    
    for scroll_iter in scroll_coordinates:
        if hero_stats["X_place"] == scroll_iter[1] and hero_stats["Y_place"] == scroll_iter[0]:
            inventory[SCROLL_SYMBOL] += 1
            del scroll_coordinates[scroll_coordinates.index(scroll_iter)]
            print("Вы подобрали магический свиток!")


    for diamond_iter in diamond_coordinates:
        if hero_stats["X_place"] == diamond_iter[1] and hero_stats["Y_place"] == diamond_iter[0]:
            inventory[DIAMOND_SYMBOL] += 1
            del diamond_coordinates[diamond_coordinates.index(diamond_iter)]
            print("Вы подобрали алмаз!")


def conflict(): #Функция битвы 
    for conf in enemies_coordinates:
          if hero_stats["X_place"] == conf[1] and hero_stats["Y_place"] == conf[0]:
               print("Столкновение с противником!")
               hero_stats["health"] = fight(character_hp = hero_stats["health"],
                    character_atk = hero_stats["attak"],
                    character_def = hero_stats["defense"],
                    enemy_hp_fight = ENEMY_HP,
                    enemy_atk_fight = ENEMY_ATK,
                    enemy_def_fight = ENEMY_DEF,
                    verbose = True)
               if hero_stats["health"] != 0:
                    hero_stats["experience"] += 5
                    del enemies_coordinates[enemies_coordinates.index(conf)] #убиваем противника(убираем с карты)
    
    for conf_vampire in vampire_coordinats:
          if hero_stats["X_place"] == conf_vampire[1] and hero_stats["Y_place"] == conf_vampire[0]:
               print("Столкновение с противником!")
               hero_stats["health"] = fight(character_hp = hero_stats["health"],
                    character_atk = hero_stats["attak"],
                    character_def = hero_stats["defense"],
                    enemy_hp_fight = VAMPIRE_HP,
                    enemy_atk_fight = VAMPIRE_ATK,
                    enemy_def_fight = VAMPIRE_DEF,
                    verbose = True)
               if hero_stats["health"] != 0:
                    hero_stats["experience"] += 10
                    del vampire_coordinats[vampire_coordinats.index(conf_vampire)] #убиваем противника(убираем с карты)

    
    for conf_dragon in dragon_coordinats:
          if hero_stats["X_place"] == conf_dragon[1] and hero_stats["Y_place"] == conf_dragon[0]:
               print("Столкновение с противником!")
               hero_stats["health"] = fight(character_hp = hero_stats["health"],
                    character_atk = hero_stats["attak"],
                    character_def = hero_stats["defense"],
                    enemy_hp_fight = DRAGON_HP,
                    enemy_atk_fight = DRAGON_ATK,
                    enemy_def_fight = DRAGON_DEF,
                    verbose = True)
               if hero_stats["health"] != 0:
                    del dragon_coordinats[dragon_coordinats.index(conf_dragon)] #убиваем противника(убираем с карты)

    
def city(): #Функция города 
     if hero_stats["X_place"] == city_coordinates[1] and hero_stats["Y_place"] == city_coordinates[0]:
          print("👑Добро пожаловать в город!👑")
          menu_input = 0
          list_val_store = list(store_content.values())
          list_key_store = list(store_content.keys())

            
          while menu_input != 4:
            print("1 - Купить", "2 - Продать", "3 - Прокачаться", "4 - Выход", sep = "\n")
            menu_input = int(input())
          
            print("\n")

            if menu_input == 1:

                print("Магазин оружия")

                store_input = 0

                while store_input != 7:
                    
                    for key_store, value_store in store_content.items():
                        print(f"{value_store[3]}){key_store} - {value_store[0]}💎 ({value_store[2]} + {value_store[1]})")
                    print("7)Выйти")
                    print("\n")

                    store_input = int(input())

                    if store_input == 1 and inventory[DIAMOND_SYMBOL] >= list_val_store[0][0]:
                        inventory[DIAMOND_SYMBOL] -= list_val_store[0][0]
                        hero_stats["defense"] += list_val_store[0][1]
                        del store_content[list_key_store[0]]

                    elif store_input == 2 and inventory[DIAMOND_SYMBOL] >= list_val_store[1][0]:
                        inventory[DIAMOND_SYMBOL] -= list_val_store[1][0]
                        hero_stats["defense"] += list_val_store[1][1]
                        del store_content[list_key_store[1]]

                    elif store_input == 3 and inventory[DIAMOND_SYMBOL] >= list_val_store[2][0]:
                        inventory[DIAMOND_SYMBOL] -= list_val_store[2][0]
                        hero_stats["defense"] += list_val_store[2][1]
                        del store_content[list_key_store[2]]

                    elif store_input == 4 and inventory[DIAMOND_SYMBOL] >= list_val_store[3][0]:
                        inventory[DIAMOND_SYMBOL] -= list_val_store[3][0]
                        hero_stats["defense"] += list_val_store[3][1]
                        del store_content[list_key_store[3]]

                    elif store_input == 5 and inventory[DIAMOND_SYMBOL] >= list_val_store[4][0]:
                        inventory[DIAMOND_SYMBOL] -= list_val_store[4][0]
                        hero_stats["defense"] += list_val_store[4][1]
                        del store_content[list_key_store[4]]

                    elif store_input == 6 and inventory[DIAMOND_SYMBOL] >= list_val_store[5][0]:
                        inventory[DIAMOND_SYMBOL] -= list_val_store[5][0]
                        hero_stats["defense"] += list_val_store[5][1]
                        del store_content[list_key_store[5]]
                    else:
                        print("У вас недостаточно алмазов!")

                    

            elif menu_input == 2:

                print("Магазин артефактов")

                count_pr = 0
                for key_pr, value_pr in price.items():
                    count_pr  += 1
                    print(f"{count_pr}){key_pr} - {value_pr}💎")

                print("3)Выйти")
                print("\n")
                pr_input = ""

                while pr_input != 3:

                    pr_input = int(input())
                    if pr_input == 1 and inventory[SCROLL_SYMBOL] != 0:
                        inventory[SCROLL_SYMBOL] = 0
                        inventory[DIAMOND_SYMBOL] += inventory[SCROLL_SYMBOL] * 3
                    elif pr_input == 1 and inventory[MAGIC_SYMBOL] != 0:
                        inventory[MAGIC_SYMBOL] = 0
                        inventory[DIAMOND_SYMBOL] += inventory[MAGIC_SYMBOL] * 4
                    elif inventory[SCROLL_SYMBOL] == 0 or inventory[MAGIC_SYMBOL] == 0:
                        print("У вас нет этого артефакта.")
                        print("\n")
                    
            
            elif menu_input == 3:
                if hero_stats["level_pers"] < 5: 
                    if hero_stats["experience"] >= 10 and hero_stats["experience"] < 20 and hero_stats["level_pers"] < 1:
                        hero_stats["experience"] -= 10
                        hero_stats["health"] += 10
                        hero_stats["level_pers"] += 1
                        top_health = 130
                        print(f"Вы повысили уровень! Теперь у вас {hero_stats["level_pers"]} уровень")
                    
                    elif hero_stats["experience"] >= 20 and hero_stats["experience"] < 40 and hero_stats["level_pers"] < 2:
                        hero_stats["experience"] -= 20
                        hero_stats["health"] += 20
                        hero_stats["attak"] += 10
                        hero_stats["level_pers"] += 1
                        top_health = 150
                        print(f"Вы повысили уровень! Теперь у вас {hero_stats["level_pers"]} уровень")
                    
                    elif hero_stats["experience"] >= 40 and hero_stats["experience"] < 80 and hero_stats["level_pers"] < 3:
                        hero_stats["experience"] -= 40
                        hero_stats["health"] += 30
                        hero_stats["attak"] += 20
                        hero_stats["level_pers"] += 1
                        top_health = 180
                        print(f"Вы повысили уровень! Теперь у вас {hero_stats["level_pers"]} уровень")
                    
                    elif hero_stats["experience"] >= 80 and hero_stats["experience"] < 100 and hero_stats["level_pers"] < 4:
                        hero_stats["experience"] -= 80
                        hero_stats["health"] += 40
                        hero_stats["attak"] += 20
                        hero_stats["level_pers"] += 1
                        top_health = 220
                        print(f"Вы повысили уровень! Теперь у вас {hero_stats["level_pers"]} уровень")
                    
                    elif hero_stats["experience"] >= 100 and hero_stats["level_pers"] < 5:
                        hero_stats["experience"] -= 100
                        hero_stats["health"] += 100
                        hero_stats["attak"] += 100
                        hero_stats["level_pers"] += 1
                        top_health = 350
                        print(f"Вы повысили уровень! Теперь у вас {hero_stats["level_pers"]} уровень")
                    else:
                        print("У вас недостаточно опыта!")

                else:
                    print("Вы уже достигли максимального уровня!")
            elif menu_input == 4:
                hero_stats["X_place"] = city_coordinates[1] - 1