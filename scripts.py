
from config import *

class Hero:

    def __init__(self):
        self.health =  100
        self.attak =  25
        self.defense =  40
        self.level_pers = 0
        self.experience =0
        self.X_place = 0
        self.Y_place = 0
        self.hero_symbol = "🧙"
        self.top_health = 100
        self.inventory = {
                    "🍎" : 0,
                    "🔮" : 0,
                    "📜" : 0,
                    "💎" : 0
                }
        self.heal_coordinates = [
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

        self.magic_ball = [
                            [9,27],
                            [7,17],
                            [14,5],
                            [10,19],
                            [11,17],
                            [5,0],
                            [6,25]
                        ]

        self.scroll_coordinates = [
                            [1,14],
                            [3,19],
                            [9,5],
                            [11,29],
                            [4,18],
                            [8,0],
                            [9,20]
                        ]
        self.diamond_coordinates = [
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

        
        
    def inventory_contents(self):#метод инвентаря
        print("Инвентарь:")
        for inv_key, inv_values in self.inventory.items():
            print(f"{inv_key} - {inv_values}")
    

    def healing(self):#метод аптечки 
        if self.inventory[HEAL_SYMBOL] > 0 and self.health < self.top_health:
            if self.health + HEAL_VALUES > self.top_health: #чтобы здоровье больше TOP_HEALTH не получалось
                self.health = self.top_health 
            else:
                self.health += HEAL_VALUES
            self.inventory[HEAL_SYMBOL] -= 1
            print(f"Вы использовали аптечку! Теперь у героя {self.health} очков здоровья.")
        elif self.inventory[HEAL_SYMBOL] == 0:
            print("У вас нет аптечек!")
        elif self.health == self.top_health:
            print("Герой здоров! Лечение не требуется!")
    

    def artifact_selection(self): #метод сбора артефактов 
        for mag_sel_iter in self.magic_ball:
            if self.X_place == mag_sel_iter[1] and self.Y_place == mag_sel_iter[0]:
                self.inventory[MAGIC_SYMBOL] += 1
                del self.magic_ball[self.magic_ball.index(mag_sel_iter)]
                print("Вы подобрали магический шар!")
        
        for scroll_iter in self.scroll_coordinates:
            if self.X_place == scroll_iter[1] and self.Y_place == scroll_iter[0]:
                self.inventory[SCROLL_SYMBOL] += 1
                del self.scroll_coordinates[self.scroll_coordinates.index(scroll_iter)]
                print("Вы подобрали магический свиток!")


        for diamond_iter in self.diamond_coordinates:
            if self.X_place == diamond_iter[1] and self.Y_place == diamond_iter[0]:
                self.inventory[DIAMOND_SYMBOL] += 1
                del self.diamond_coordinates[self.diamond_coordinates.index(diamond_iter)]
                print("Вы подобрали алмаз!")


class World(Hero): 

    def __init__(self):

        super().__init__()

        self.enemies_coordinates = [
                                    [1,2],[2,2],[4,3],[6,4],[6,17],[8,17],[7,16],[8,29],[11,4],[11,8],[12,15],[12,9],[12,14],[13,6],[13,8],[14,9],[14,1],[3,6],[3,28],[4,9],[4,11],[4,0],[6,24],[6,26],[9,0]
                                    ]
        self.vampire_coordinats = [
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

        self.dragon_coordinats = [[9,29]]

        self.city_coordinates = [0,1]

        self.store_content = {
            "🛡️": [1, 5, "броня", 1],
            "🔪": [3, 5, "атака", 2],
            "🗡️": [5, 10, "атака", 3],
            "🏹": [10, 20, "атака", 4],
            "🛡️✨": [15, 20, "броня", 5],
            "⚔️": [17, 50, "атака", 6],
        }

        self.price = {
        "📜":3,
        "🔮":4
        }

    def draw(self, character_X, character_Y): #метод отрисовки карты 
    
        print("Карта")
        
        map = []

        for i in range(MAP_HEIGHT):
            map_st = []
            for j in range(MAP_WIDTH):
                map_st.append(MAP_SYMBOL)
            map.append(map_st)

        map[character_Y][character_X] = self.hero_symbol #координаты героя  
        
        for en in  self.enemies_coordinates:
            map[en[0]][en[1]] = ENEMY_SYMBOL #координаты противников 

        for heal_iter in self.heal_coordinates:
            map[heal_iter[0]][heal_iter[1]] = HEAL_SYMBOL #координаты аптечек 

        for ball_iter in self.magic_ball:
            map[ball_iter[0]][ball_iter[1]] = MAGIC_SYMBOL

        for scroll_iter in self.scroll_coordinates:
            map[scroll_iter[0]][scroll_iter[1]] = SCROLL_SYMBOL
        
        for diamond_iter in self.diamond_coordinates:
            map[diamond_iter[0]][diamond_iter[1]] = DIAMOND_SYMBOL

        for vampir_iter in self.vampire_coordinats:
            map[vampir_iter[0]][vampir_iter[1]] = VAMPIRE_SYMBOL


        if len(self.dragon_coordinats) != 0:
            map[self.dragon_coordinats[0][0]][self.dragon_coordinats[0][1]] = DRAGON_SYMBOL
        

        map[self.city_coordinates[0]][self.city_coordinates[1]] = CITY_SYMBOL
        

        for map_iter in map:
            print("".join(map_iter))

    def calculate_damage(self, attack, target_defence): #метод подсчёта урона
        if attack - (attack/100)*target_defence >= 0: #добавил чтобы не было отрицательного урона, если броня сильно больше чем атака 
            return attack - (attack/100)*target_defence
        else:
            return 0 


    def fight(self, character_hp:int, #Функция битвы 
            character_atk:int,
            character_def:int,
            enemy_hp_fight:int,
            enemy_atk_fight:int,
            enemy_def_fight:int,
            verbose:bool):
        
        if verbose:print("Начинается бой!")

        while True:
            
        #удар персонажа

            enemy_hp_fight -= self.calculate_damage(character_atk, enemy_def_fight)
            if verbose: print(f"Персонаж бьёт с атакой {character_atk} против защиты {enemy_def_fight}, наносит {self.calculate_damage(character_atk, enemy_def_fight)} урона")
            if enemy_hp_fight == 0 or enemy_hp_fight < 0:
                if verbose: print(f"Победа! У персонажа осталось {character_hp}")
                return character_hp
                break
            
            #удар противника

            character_hp -= self.calculate_damage(enemy_atk_fight, character_def)
            if verbose: print(f"Противник бьёт с атакой {enemy_atk_fight} против защиты {character_def}, наносит {self.calculate_damage(enemy_atk_fight, character_def)} урона")
            if character_hp == 0 or character_hp < 0:
                if verbose: print("Поражение! Игра окончена!")
                return 0
                break
            
            if verbose:print(f"У героя осталось {character_hp} очков здоровья")
    
    def conflict(self): #Функция битвы 
        for conf in self.enemies_coordinates:
            if self.X_place == conf[1] and self.Y_place == conf[0]:
                print("Столкновение с противником!")
                self.health = self.fight(character_hp = self.health,
                        character_atk = self.attak,
                        character_def = self.defense,
                        enemy_hp_fight = ENEMY_HP,
                        enemy_atk_fight = ENEMY_ATK,
                        enemy_def_fight = ENEMY_DEF,
                        verbose = True)
                if self.health != 0:
                        self.experience += 5
                        del self.enemies_coordinates[self.enemies_coordinates.index(conf)] #убиваем противника(убираем с карты)
        
        for conf_vampire in self.vampire_coordinats:
            if self.X_place == conf_vampire[1] and self.Y_place == conf_vampire[0]:
                print("Столкновение с противником!")
                self.health = self.fight(character_hp = self.health,
                        character_atk = self.attak,
                        character_def = self.defense,
                        enemy_hp_fight = VAMPIRE_HP,
                        enemy_atk_fight = VAMPIRE_ATK,
                        enemy_def_fight = VAMPIRE_DEF,
                        verbose = True)
                if self.health != 0:
                        self.experience += 10
                        del self.vampire_coordinats[self.vampire_coordinats.index(conf_vampire)] #убиваем противника(убираем с карты)

        
        for conf_dragon in self.dragon_coordinats:
            if self.X_place == conf_dragon[1] and self.Y_place == conf_dragon[0]:
                print("Столкновение с противником!")
                self.health = self.fight(character_hp = self.health,
                        character_atk = self.attak,
                        character_def = self.defense,
                        enemy_hp_fight = DRAGON_HP,
                        enemy_atk_fight = DRAGON_ATK,
                        enemy_def_fight = DRAGON_DEF,
                        verbose = True)
                if self.health != 0:
                        del self.dragon_coordinats[self.dragon_coordinats.index(conf_dragon)] #убиваем противника(убираем с карты)

    
    def city(self): #Функция города 
     if self.X_place == self.city_coordinates[1] and self.Y_place == self.city_coordinates[0]:
          print("👑Добро пожаловать в город!👑")
          menu_input = 0
          list_val_store = list(self.store_content.values())
          list_key_store = list(self.store_content.keys())

            
          while menu_input != 4:
            print("1 - Купить", "2 - Продать", "3 - Прокачаться", "4 - Выход", sep = "\n")
            menu_input = int(input())
          
            print("\n")

            if menu_input == 1:

                print("Магазин оружия")

                store_input = 0

                while store_input != 7:
                    
                    for key_store, value_store in self.store_content.items():
                        print(f"{value_store[3]}){key_store} - {value_store[0]}💎 ({value_store[2]} + {value_store[1]})")
                    print("7)Выйти")
                    print("\n")

                    store_input = int(input())

                    if store_input == 1 and self.inventory[DIAMOND_SYMBOL] >= list_val_store[0][0]:
                        self.inventory[DIAMOND_SYMBOL] -= list_val_store[0][0]
                        self.defense += list_val_store[0][1]
                        del self.store_content[list_key_store[0]]

                    elif store_input == 2 and self.inventory[DIAMOND_SYMBOL] >= list_val_store[1][0]:
                        self.inventory[DIAMOND_SYMBOL] -= list_val_store[1][0]
                        self.defense += list_val_store[1][1]
                        del self.store_content[list_key_store[1]]

                    elif store_input == 3 and self.inventory[DIAMOND_SYMBOL] >= list_val_store[2][0]:
                        self.inventory[DIAMOND_SYMBOL] -= list_val_store[2][0]
                        self.defense += list_val_store[2][1]
                        del self.store_content[list_key_store[2]]

                    elif store_input == 4 and self.inventory[DIAMOND_SYMBOL] >= list_val_store[3][0]:
                        self.inventory[DIAMOND_SYMBOL] -= list_val_store[3][0]
                        self.defense += list_val_store[3][1]
                        del self.store_content[list_key_store[3]]

                    elif store_input == 5 and self.inventory[DIAMOND_SYMBOL] >= list_val_store[4][0]:
                        self.inventory[DIAMOND_SYMBOL] -= list_val_store[4][0]
                        self.defense += list_val_store[4][1]
                        del self.store_content[list_key_store[4]]

                    elif store_input == 6 and self.inventory[DIAMOND_SYMBOL] >= list_val_store[5][0]:
                        self.inventory[DIAMOND_SYMBOL] -= list_val_store[5][0]
                        self.defense += list_val_store[5][1]
                        del self.store_content[list_key_store[5]]
                    else:
                        print("У вас недостаточно алмазов!")

                    

            elif menu_input == 2:

                print("Магазин артефактов")

                count_pr = 0
                for key_pr, value_pr in self.price.items():
                    count_pr  += 1
                    print(f"{count_pr}){key_pr} - {value_pr}💎")

                print("3)Выйти")
                print("\n")
                pr_input = ""

                while pr_input != 3:

                    pr_input = int(input())
                    if pr_input == 1 and self.inventory[SCROLL_SYMBOL] != 0:
                        self.inventory[SCROLL_SYMBOL] = 0
                        self.inventory[DIAMOND_SYMBOL] += self.inventory[SCROLL_SYMBOL] * 3
                    elif pr_input == 1 and self.inventory[MAGIC_SYMBOL] != 0:
                        self.inventory[MAGIC_SYMBOL] = 0
                        self.inventory[DIAMOND_SYMBOL] += self.inventory[MAGIC_SYMBOL] * 4
                    elif self.inventory[SCROLL_SYMBOL] == 0 or self.inventory[MAGIC_SYMBOL] == 0:
                        print("У вас нет этого артефакта.")
                        print("\n")
                    
            
            elif menu_input == 3:
                if self.level_pers < 5: 
                    if self.experience >= 10 and self.experience < 20 and self.level_pers < 1:
                        self.experience -= 10
                        self.health += 10
                        self.level_pers += 1
                        self.top_health = 130
                        print(f"Вы повысили уровень! Теперь у вас {self.level_pers} уровень")
                    
                    elif self.experience >= 20 and self.experience < 40 and self.level_pers < 2:
                        self.experience -= 20
                        self.health += 20
                        self.attak += 10
                        self.level_pers += 1
                        self.top_health = 150
                        print(f"Вы повысили уровень! Теперь у вас {self.level_pers} уровень")
                    
                    elif self.experience >= 40 and self.experience < 80 and self.level_pers < 3:
                        self.experience -= 40
                        self.health += 30
                        self.attak += 20
                        self.level_pers += 1
                        self.top_health = 180
                        print(f"Вы повысили уровень! Теперь у вас {self.level_pers} уровень")
                    
                    elif self.experience >= 80 and self.experience < 100 and self.level_pers < 4:
                        self.experience -= 80
                        self.health += 40
                        self.attak += 20
                        self.level_pers += 1
                        self.top_health = 220
                        print(f"Вы повысили уровень! Теперь у вас {self.level_pers} уровень")
                    
                    elif self.experience >= 100 and self.level_pers < 5:
                        self.experience -= 100
                        self.health += 100
                        self.attak += 100
                        self.level_pers += 1
                        self.top_health = 350
                        print(f"Вы повысили уровень! Теперь у вас {self.level_pers} уровень")
                    else:
                        print("У вас недостаточно опыта!")

                else:
                    print("Вы уже достигли максимального уровня!")
            elif menu_input == 4:
                self.X_place = self.city_coordinates[1] - 1


            


                