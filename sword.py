from random import randint
from random import choice
import math

print("\nstrengthening of the sword game project\n\n\n")

# 플래이어 클래스
class player:
    def __init__(self, sword, money, prevention, inventory):
        self.sword = sword
        self.money = money
        self.prevention = prevention
        self.inventory = {"sword": [], "item": []}

# 일반 아이템 클래스
class common_item:
    def __init__(self, name, count):
        self.name = name
        self.count = count

# 판매 아이템 클래스
class shop_item:
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost

# 조합 아이템 클래스
class crafting_item:
    def __init__(self, name, material, material_count):
        self.name = name
        self.material = material
        self.material_count = material_count

# 아이템
# 일반 아이템
item_01 = common_item("국적불분명 철조각", 0)
item_02 = common_item("타우의 뼈 부스러기", 0)
item_03 = common_item("빛 바랜 형광물질", 0)
item_04 = common_item("스워스산 철조각", 0)
item_05 = common_item("불꽃마검 손잡이", 0)
item_06 = common_item("사악한 영혼", 0)
item_07 = common_item("도끼 가루", 0)
item_08 = common_item("투명 물질", 0)
# 판매 아이템
item_11 = shop_item("깨짐 방지권 X 1", 1000000)
item_12 = shop_item("깨짐 방지권 X 3", 2500000)
item_13 = shop_item("+9강 워프권", 1000000)
item_14 = shop_item("+13강 워프권", 7000000)
item_15 = shop_item("+14강 워프권", 10000000)
item_16 = shop_item("+15강 워프권", 15000000)
# 재료 아이템
item_21 = common_item("+19 왕푸야샤", 0)
item_22 = common_item("+20 다색검", 0)
item_23 = common_item("+21 템페스트 골드", 0)
item_24 = common_item("+22 샤프 워커", 0)
item_25 = common_item("+23 삐에로의 쌍검", 0)
item_26 = common_item("+24 도룡도", 0)
item_27 = common_item("+25 안 강해보이는 검", 0)
item_28 = common_item("+26 메두사", 0)
item_29 = common_item("+27 오딧세이 소드", 0)
item_30 = common_item("+28 모자이칼", 0)
# 조합 아이템
item_31 = crafting_item("깨짐 방지권 1개", item_01, 5)
item_32 = crafting_item("깨짐 방지권 1개", item_02, 3)
item_33 = crafting_item("불꽃마검", item_03, 2)
item_34 = crafting_item("깨짐 방지권 2개", item_04, 3)
item_35 = crafting_item("투명검", item_05, 2)
item_36 = crafting_item("깨짐 방지권 4개", item_06, 4)
item_37 = crafting_item("왕푸야샤", item_06, 6)
item_38 = crafting_item("깨짐 방지권 10개", item_07, 6)
item_39 = crafting_item("깨짐 방지권 9개",item_08 , 3)

item_list_1 = [item_01, item_02, item_03, item_04, item_05, item_06, item_07, item_08]
item_list_2 = [item_11, item_12, item_13, item_14, item_15, item_16]
item_list_3 = [item_21, item_22, item_23, item_24, item_25, item_26, item_27, item_28, item_29, item_30]
item_list_4 = [item_31, item_32, item_33, item_34, item_35, item_36, item_37, item_38, item_39]

# 검 클래스
class sword:
    def __init__(self, name, reinforcement_cost, selling_price, success_rate, prevention, required_item, required_item_count, drop_item, drop_item_count):
        self.name = name
        self.reinforcement_cost = reinforcement_cost
        self.selling_price = selling_price
        self.success_rate = success_rate
        self.prevention = prevention
        self.required_item = required_item
        self.required_item_count = required_item_count
        self.drop_item = drop_item
        self.drop_item_count = drop_item_count

# 검 종류
# 검 이름, 강화비용, 판매가격, 성공률, 방지권, 필요아이템, 드랍아이템
sword_0 = sword("+0 낡은 단검", 300, 0, 100, 0, "", 0, "", 0)
sword_1 = sword("+1 쓸만환 단검", 300, 150, 100, 0, "", 0, "", 0)
sword_2 = sword("+2 견고한 단검", 500, 400, 100, 0, "", 0, "", 0)
sword_3 = sword("+3 바이킹 소드", 500, 600, 95, 0, "", 0, "", 0)
sword_4 = sword("+4 불타는 검", 1000, 800, 95, 0, "", 0, "", 0)
sword_5 = sword("+5 냉기의 소드", 1500, 1600, 90, 0, "", 0, "", 0)
# 방지권
sword_6 = sword("+6 양날 검", 2000, 3500, 90, 1, "", 0, item_01, 1)
sword_7 = sword("+7 심판자의 대검", 2000, 6100, 90, 1, "", 0, item_01, 2)
sword_8 = sword("+8 마력의 검", 3000, 10000, 85, 1, "", 0, item_01, 3)
sword_9 = sword("+9 타우 스워드", 5000, 20000, 80, 1, "", 0, item_02, 1)
sword_10 = sword("+10 형광 검", 10900, 35100, 80, 1, "", 0, item_03, 1)
sword_11 = sword("+11 피묻은 검", 20000, 160000, 75, 1, "", 0, item_04, 1)
sword_12 = sword("+12 화염의 쌍검", 35000, 350000, 70, 1, "", 0, item_04, 2)
sword_13 = sword("+13 불꽃 마검", 5000, 2000000, 80, 2, "", 0, item_05, 1)
sword_14 = sword("+14 마검 아포피스", 100000, 3000000, 65, 3, "", 0, item_06, 1)
sword_15 = sword("+15 데몬 배틀 엑스", 180000, 7500000, 60, 4, "", 0, item_07, 1)
sword_16 = sword("+16 투명 검", 300000, 14200000, 60, 7, "", 0, item_08, 1)
sword_17 = sword("+17 날렵한 용검", 300000, 30000000, 55, 9, "", 0, "", 0)
sword_18 = sword("+18 샤이니 소드", 500000, 30000000, 50, 10, "", 0, "", 0)
# 보관
sword_19 = sword("+19 왕푸야샤", 800000, 47500000, 50, 12, "", 0, "", 0)
sword_20 = sword("+20 다색검", 1500000, 68300000, 45, 15, "", 0, "", 0)
sword_21 = sword("+21 템페스트 골드", 0, 101000000, 40, 17, sword_19, 1, "", 0)
sword_22 = sword("+22 샤프 워커", 0, 160000000, 40, 20, sword_21, 2, "", 0)
sword_23 = sword("+23 삐에로의 쌍검", 0, 230000000, 40, 22, item_06, 12, "", 0)
sword_24 = sword("+24 도룡도", 0, 300000000, 40, 23, sword_22, 1, "", 0)
sword_25 = sword("+25 안 강해보이는 검", 0, 400000000, 35, 23, item_07, 15, "", 0)
sword_26 = sword("+26 메두사", 5000000, 1800000000, 50, 0, "", 0, "", 0)
sword_27 = sword("+27 오딧세이 소드", 0, 2500000000, 40, 0, item_08, 2, "", 0)
sword_28 = sword("+28 모자이칼", 0, 0, 15, 0, "", 0, "", 0)
sword_29 = sword("+29 화염에 달군 검", "Unkown", "Unkown", "Unkown", 0, "", 0, "", 0)

sword_list_01 = [sword_0, sword_1, sword_2, sword_3, sword_4, sword_5]
sword_list_02 = [sword_6, sword_7, sword_8, sword_9, sword_10, sword_11, \
                sword_12, sword_13, sword_14, sword_15, sword_16, sword_17, \
                sword_18]
sword_list_03 = [sword_19, sword_20, sword_21, sword_22, sword_23, sword_24, \
                sword_25, sword_26, sword_27, sword_28]
sword_list_11 = [sword_0, sword_1, sword_2, sword_3, sword_4, sword_5, \
                 sword_6, sword_7, sword_8, sword_9, sword_10, sword_11, \
                sword_12, sword_13, sword_14, sword_15, sword_16, sword_17, \
                sword_18]

# 검 업그레이드
def upgrade(player_1):
    if player_1.sword == sword_0:
        player_1.sword = sword_1
    elif player_1.sword == sword_1:
        player_1.sword = sword_2
    elif player_1.sword == sword_2:
        player_1.sword = sword_3
    elif player_1.sword == sword_3:
        player_1.sword = sword_4
    elif player_1.sword == sword_4:
        player_1.sword = sword_5
    elif player_1.sword == sword_5:
        player_1.sword = sword_6
    elif player_1.sword == sword_6:
        player_1.sword = sword_7
    elif player_1.sword == sword_7:
        player_1.sword = sword_8
    elif player_1.sword == sword_8:
        player_1.sword = sword_9
    elif player_1.sword == sword_9:
        player_1.sword = sword_10
    elif player_1.sword == sword_10:
        player_1.sword = sword_11
    elif player_1.sword == sword_11:
        player_1.sword = sword_12
    elif player_1.sword == sword_12:
        player_1.sword = sword_13
    elif player_1.sword == sword_13:
        player_1.sword = sword_14
    elif player_1.sword == sword_14:
        player_1.sword = sword_15
    elif player_1.sword == sword_15:
        player_1.sword = sword_16
    elif player_1.sword == sword_16:
        player_1.sword = sword_17
    elif player_1.sword == sword_17:
        player_1.sword = sword_18
    elif player_1.sword == sword_18:
        player_1.sword = sword_19
    elif player_1.sword == sword_19:
        player_1.sword = sword_20
    elif player_1.sword == sword_20:
        player_1.sword = sword_21
    elif player_1.sword == sword_21:
        player_1.sword = sword_22
    elif player_1.sword == sword_22:
        player_1.sword = sword_23
    elif player_1.sword == sword_23:
        player_1.sword = sword_24
    elif player_1.sword == sword_24:
        player_1.sword = sword_25
    elif player_1.sword == sword_25:
        player_1.sword = sword_26
    elif player_1.sword == sword_26:
        player_1.sword = sword_27
    elif player_1.sword == sword_27:
        player_1.sword = sword_28
    elif player_1.sword == sword_28:
        player_1.sword = sword_29

# 아이템 드랍
def drop_item(player_1, repair):
    if player_1.sword.drop_item_count != 0:
        if player_1.sword.drop_item_count == 1:
            drop_item_count = randint(1,3)
        elif player_1.sword.drop_item_count == 2:
            drop_item_count = randint(2, 4)
        elif player_1.sword.drop_item_count == 3:
            drop_item_count = randint(3, 5)
        player_1.inventory["item"][player_1.inventory["item"].index(player_1.sword.drop_item)].count = \
            player_1.inventory["item"][player_1.inventory["item"].index(player_1.sword.drop_item)].count + drop_item_count
        if repair == "no":
            print(f"\n강화가 실패하여 '{player_1.sword.name}' 이/가 파괴되었습니다. '{player_1.sword.drop_item.name}' 을/를 {drop_item_count} 개 주웠습니다.\n")
            player_1.sword = sword_0
        elif repair == "yes":
            print(f"\n'{player_1.sword.name}' 을/를 성공적으로 복구하였습니다. '{player_1.sword.drop_item.name}' 을/를 {drop_item_count} 개 주웠습니다.\n")
    else:
        if repair == "no":
            print(f"\n강화가 실패하여 '{player_1.sword.name}' 이 파괴되었습니다.\n")
            player_1.sword = sword_0

# 파괴
def recycle(player_1):
    if player_1.sword.prevention != 0:
        print("\n" * 4)
        while True:
            print("파괴하기 (홈화면으로) : a / 복구하기 : s\n\n")
            print(f"깨짐 방지권이 있다면 {player_1.sword.prevention}개를 사용하여 이 '{player_1.sword.name}' 을/를 살릴 수 있습니다.\n나의 깨짐 방지권 개수 : {player_1.prevention}\n")
            answer = input("= ")
            if answer == "a":
                drop_item(player_1, "no")
                break
            elif answer == "s":
                if player_1.prevention >= player_1.sword.prevention:
                    player_1.prevention = player_1.prevention - player_1.sword.prevention
                    drop_item(player_1, "yes")
                    print(f"\n'{player_1.sword.name}' 을/를 성공적으로 복구하였습니다.\n")
                    break
                else:
                    print("\n복구하기위한 깨짐방지권이 부족합니다.\n")
            else:
                print("\n다시 입력해 주십시오.\n")
    elif player_1.sword.prevention == 0:
        drop_item(player_1, "no")

# 강화확률
def percentage(player_1):
    percentage = choice("y" * player_1.sword.success_rate + "n" * (100 - player_1.sword.success_rate))
    if percentage == "y":
        upgrade(player_1)
        print("\n강화에 성공하였습니다.\n")
    elif percentage == "n":
        recycle(player_1)

# 강화하기
def reinforcement(player_1):
    if player_1.sword.reinforcement_cost != 0:
        if player_1.sword.reinforcement_cost <= player_1.money:
            player_1.money -= player_1.sword.reinforcement_cost
            percentage(player_1)
        else:
            print("돈이 부족합니다.\n")
    elif player_1.sword.reinforcement_cost == 0:
        if player_1.sword == sword_21 or player_1.sword == sword_22 or player_1.sword == sword_24:
            inventory_select = "sword"
        elif player_1.sword == sword_23 or player_1.sword == sword_25 or player_1.sword == sword_27:
            inventory_select = "item"
        if player_1.inventory[inventory_select][player_1.inventory[inventory_select].index(player_1.sword.required_item)].count >= player_1.sword.required_item_count:
            player_1.inventory[inventory_select][player_1.inventory[inventory_select].index(player_1.sword.required_item)].count = \
                player_1.inventory[inventory_select][player_1.inventory[inventory_select].index(player_1.sword.required_item)].count - player_1.sword.required_item_count
            upgrade(player_1)
        else:
            print("강화재료가 부족합니다.\n")

# 구매
def buy(player_1, object):
    print("\n" * 9)

    while True:
        type = 0
        print("{0:-^25}".format(" 구매 "))
        print(f"{item_list_2[object].name} : {item_list_2[object].cost}")

        if object == 0 or object == 1:
            print("\n돌아가기 : q / [구매하려면 수량 입력]\n")
            type = 1
        elif object == 2 or object == 3 or object == 4 or object == 5:
            print("\n돌아가기 : q / 구매하기 : w\n")
            type = 2

        answer = input("= ")
        if answer == "q":
            print("\n" * 2)
            break
        elif type == 1:
            try:
                if int(answer) == 0:
                    print("\n" * 2)
                    break
                elif 0 < int(answer):
                    if player_1.money >= item_list_2[object].cost * int(answer):
                        player_1.money = player_1.money - (item_list_2[object].cost * int(answer))
                        if object == 0:
                            player_1.prevention = player_1.prevention + int(answer)
                        elif object == 1:
                            player_1.prevention = player_1.prevention + (int(answer) * 3)
                        print(f"\n({item_list_2[object].name}) {int(answer)}개를 성공적으로 구매하였습니다.\n")
                        break
                    else:
                        print("\n돈이 부족합니다.\n\n")
                elif 0 > int(answer):
                    print("\n올바른 양수값을 입력하여 주십시오.\n\n")
            except:
                print("\n다시 입력해 주십시오.\n\n")
        elif type == 2:
            if answer == "w":
                if player_1.money >= item_list_2[object].cost:
                    player_1.money = player_1.money - item_list_2[object].cost
                    if object == 2:
                        player_1.sword = sword_9
                    elif object == 3:
                        player_1.sword = sword_13
                    elif object == 4:
                        player_1.sword = sword_14
                    elif object == 5:
                        player_1.sword = sword_15
                    print(f"\n{item_list_2[object].name}을/를 성공적으로 구매하였습니다.\n")
                    break
                else:
                    print("\n돈이 부족합니다.\n\n")
        else:
            print("\n다시 입력해 주십시오.\n\n")

# 조합
def crafting(player_1,object):
    print("\n" * 3)

    while True:
        type = 0
        print("{0:-^25}".format(" 조합 "))
        print(f"{item_list_4[object].name} : {item_list_4[object].material.name} X {item_list_4[object].material_count}")

        if object == 0 or object == 1 or object == 3 or object == 5 or object == 7 or object == 8:
            print("\n돌아가기 : q / [구매하려면 수량 입력]\n")
            type = 1
        elif object == 2 or object == 4 or object == 6:
            print("\n돌아가기 : q / 구매하기 : w\n")
            type = 2

        answer = input("= ")
        if answer == "q":
            print("\n" * 2)
            break
        elif type == 1:
            try:
                if int(answer) == 0:
                    print("\n" * 2)
                    break
                elif 0 < int(answer):
                    if player_1.inventory["item"][player_1.inventory["item"].index(item_list_4[object].material)].count >= item_list_4[object].material_count * int(answer):
                        player_1.inventory["item"][player_1.inventory["item"].index(item_list_4[object].material)].count = \
                            player_1.inventory["item"][player_1.inventory["item"].index(item_list_4[object].material)].count - item_list_4[object].material_count * int(answer)
                        if object == 0 or object == 1:
                            player_1.prevention = player_1.prevention + (1 * int(answer))
                        elif object == 3:
                            player_1.prevention = player_1.prevention + (2 * int(answer))
                        elif object == 5:
                            player_1.prevention = player_1.prevention + (4 * int(answer))
                        elif object == 7:
                            player_1.prevention = player_1.prevention + (10 * int(answer))
                        elif object == 8:
                            player_1.prevention = player_1.prevention + (9 * int(answer))
                        print(f"\n({item_list_4[object].name}) {int(answer)}개를 성공적으로 구매하였습니다.\n")
                        break
                    else:
                        print("\n재료가 부족합니다.\n\n")
                elif 0 > int(answer):
                    print("\n올바른 양수값을 입력하여 주십시오.\n\n")
            except:
                print("\n다시 입력해 주십시오.\n\n")
        elif type == 2:
            if answer == "w":
                if player_1.inventory["item"][player_1.inventory["item"].index(item_list_4[object].material)].count >= item_list_4[object].material_count:
                    player_1.inventory["item"][player_1.inventory["item"].index(item_list_4[object].material)].count = \
                        player_1.inventory["item"][player_1.inventory["item"].index(item_list_4[object].material)].count - item_list_4[object].material_count
                    if object == 2:
                        player_1.sword = sword_13
                    elif object == 4:
                        player_1.sword = sword_16
                    elif object == 6:
                        player_1.sword = sword_19
                    print(f"\n{item_list_4[object].name}을/를 성공적으로 구매하였습니다.\n")
                    break
                else:
                    print("\n재료가 부족합니다.\n\n")
        else:
            print("\n다시 입력해 주십시오.\n\n")

# 상점
def shop(player_1,action):
    plag = 0
    n = 3
    print("\n" * 2)

    while True:
        if action == "buy":
            print("{0:=^25}".format(" 상점 (" + str(plag + 1) + " 페이지) "))
        elif action == "crafting":
            print("{0:=^25}".format(" 조합소 (" + str(plag + 1) + " 페이지) "))
        j = plag * n
        for i in range(plag * (n - 1), plag * (n - 1) + n):
            j = j + 1
            try:
                if action == "buy":
                    print(f"{j}. {item_list_2[plag + i].name} : {item_list_2[plag + i].cost}")
                elif action == "crafting":
                    print(f"{j}. {item_list_4[plag + i].name} : {item_list_4[plag + i].material.name} X {item_list_4[plag + i].material_count}")
            except:
                print()

        print("\n돌아가기 : q / 이전 : w / 다음 : e / [아이템을 구매하려면 번호 입력]")

        answer = input("= ")
        if answer == "q":
            print("\n" * 2)
            break
        elif answer == "w":
            if action == "buy":
                if plag == 0:
                    plag = 1
                else:
                    plag = plag - 1
            elif action == "crafting":
                if plag == 0:
                    plag = 2
                else:
                    plag = plag - 1
            print("\n" * 2)
        elif answer == "e":
            if action == "buy":
                if plag == 1:
                    plag = 0
                else:
                    plag = plag + 1
            elif action == "crafting":
                if plag == 2:
                    plag = 0
                else:
                    plag = plag + 1
            print("\n" * 2)
        elif action == "buy" or action == "crafting":
            try:
                if action == "buy" and 1 <= int(answer) <= len(item_list_2):
                    buy(player_1, int(answer) - 1)
                elif action == "crafting" and 1 <= int(answer) <= len(item_list_4):
                    crafting(player_1, int(answer) - 1)
                break
            except:
                pass
        else:
            print("\n다시 입력해 주십시오.\n")

# 판매
def sale(player_1):
    print(f"\n'{player_1.sword.name}' 이/가 성공적으로 판매되었습니다.\n")
    player_1.money = player_1.money + player_1.sword.selling_price
    player_1.sword = sword_0

# 인벤토리
def inventory(player_1):
    plag = 0
    n = 3
    print("\n" * 6)

    while True:
        print("원하는 인벤토리를 선택하세요.\n돌아가기 : q / 보관된 검 : w / 조각 아이템 : e")
        answer = input("= ")

        if answer == "q":
            inventory_select = ""
            print("\n" * 2)
            break
        elif answer == "w":
            inventory_select = "sword"
            break
        elif answer == "e":
            inventory_select = "item"
            break
        else:
            print("\n다시 입력해 주십시오.\n")

    print("\n" * 2)
    while inventory_select != "":
        print("{0:=^25}".format(" 인벤토리 (" + str(plag + 1) + " 페이지) "))
        for i in range(plag * (n - 1), plag * (n - 1) + n):
            try:
                print("({0}) X {1}".format(player_1.inventory[inventory_select][plag + i].name, player_1.inventory[inventory_select][plag + i].count))
            except:
                print()

        print("\n돌아가기 : q / 이전 : w / 다음 : e")

        answer = input("= ")
        if answer == "q":
            print("\n" * 2)
            break
        elif answer == "w":
            if plag == 0:
                if inventory_select == "sword":
                    plag = 3
                elif inventory_select == "item":
                    plag = 2
            else:
                plag = plag - 1
            print("\n" * 2)
        elif answer == "e":
            if inventory_select == "sword" and plag == 3:
                plag = 0
            elif inventory_select == "item" and plag == 2:
                plag = 0
            else:
                plag = plag + 1
            print("\n" * 2)
        else:
            print("\n다시 입력해 주십시오.\n")

# 보관하기
def keep(player_1):
    if player_1.sword == sword_19:
        i = 0
    elif player_1.sword == sword_20:
        i = 1
    elif player_1.sword == sword_21:
        i = 2
    elif player_1.sword == sword_22:
        i = 3
    elif player_1.sword == sword_23:
        i = 4
    elif player_1.sword == sword_24:
        i = 5
    elif player_1.sword == sword_25:
        i = 6
    elif player_1.sword == sword_26:
        i = 7
    elif player_1.sword == sword_27:
        i = 8
    elif player_1.sword == sword_28:
        i = 9

    player_1.inventory["sword"][i].count = player_1.inventory["sword"][i].count + 1
    player_1.sword = sword_0
    print(f"'{player_1.sword.name}' 을/를 성공적으로 보관하였습니다.\n")

# 메인
def main():
    print("(이 게임은 9칸의 로그 화면을 요구합니다.)\n")
    input("게임을 시작하려면 엔터")

    print("\n" * 2)

    player_1 = player(sword_0, 1000000, 0, [])

    player_1.inventory['item'] = list(item_list_1)
    player_1.inventory['sword'] = list(item_list_3)

    while True:
        if player_1.sword == sword_0:
            print("강화하기 : q / 상점 : w / 인벤토리 : e\n\n")
        elif player_1.sword == sword_1:
            print("강화하기 : q / 상점 : w / 조합소 : e\n\n")
        elif player_1.sword == sword_28:
            print("강화하기 : q\n\n")
        elif player_1.sword in sword_list_11:
            print("강화하기 : q / 판매하기 : w\n\n")
        elif player_1.sword in sword_list_03:
            print("강화하기 : q / 판매하기 : w / 보관하기 : e\n\n")

        if player_1.sword.reinforcement_cost == 0 and player_1.sword != sword_28:
            print(f"{player_1.sword.name}\n강화 성공률 : {player_1.sword.success_rate}% / 깅화재료 : ({player_1.sword.required_item.name} X {player_1.sword.required_item_count}) 판매가격 : {player_1.sword.selling_price} \
                  \n방지권 : {player_1.prevention} 돈 : {player_1.money}")
        else:
            print(f"{player_1.sword.name}\n강화 성공률 : {player_1.sword.success_rate}% / 깅화비용 : {player_1.sword.reinforcement_cost} 판매가격 : {player_1.sword.selling_price} \
                \n방지권 : {player_1.prevention} 돈 : {player_1.money}")

        answer = input("= ")
        if player_1.sword != sword_29:
            if answer == "q" or answer == "":
                reinforcement(player_1)
            elif answer == "w":
                if player_1.sword == sword_0:
                    shop(player_1, "buy")
                elif player_1.sword != sword_28:
                    sale(player_1)
                else:
                    print("\n다시 입력해 주십시오.\n")
            elif answer == "e":
                if player_1.sword == sword_0:
                    inventory(player_1)
                elif player_1.sword == sword_1:
                    shop(player_1, "crafting")
                elif player_1.sword in sword_list_03:
                    keep(player_1)
                else:
                    print("\n다시 입력해 주십시오.\n")

            elif answer == "admin":
                player_1.money = math.inf
                player_1.prevention = math.inf
                print("\n" * 2)

            else:
                print("\n다시 입력해 주십시오.\n")
        else:
            print("\n" * 2)

if __name__ == "__main__":
    main()
