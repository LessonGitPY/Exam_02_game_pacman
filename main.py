import os
import time
from random import randint


# # COLORS TEXT
# Black = 30      # Чёрный
# Red = 31        # Красный
# Green = 32      # Зелёный
# Yellow = 33     # Жёлтый
# Blue = 34       # Синий
# Purple = 35     # Фиолетовый
# Turquoise = 36  # Бирюзовый
# White = 37      # Белый
#
# # COLORS Fon
# F_Black = 40      # Чёрный
# F_Red = 41        # Красный
# F_Green = 42      # Зелёный
# F_Yellow = 43     # Жёлтый
# F_Blue = 44       # Синий
# F_Purple = 45     # Фиолетовый
# F_Turquoise = 46  # Бирюзовый
# F_White = 47      # Белый

# objects
Length_object = len("[0;34;44mX[0m")
Edge_map = "\033[0;34;44m#\033[0m"
Enemy = "\033[0;33;43mE\033[0m"
Player = "\033[0;34;44mP\033[0m"


# OPTIONS
WIDTH = 40
HEIGHT = 12
SIZE_MAP = (WIDTH, HEIGHT)


def create_map(size):
    with open("map.txt", "w", encoding="utf-8") as f:
        f.write("\033[0;34;44m" + "#" * size[0] + "\033[0m" + "\n")
        for j in range(1, size[1]):
            f.write(Edge_map + "." * (size[0]-2) + Edge_map + "\n")
        f.write("\033[0;34;44m" + "#" * size[0] + "\033[0m" + "\n")


def read_map(map_name):
    with open(map_name, "r", encoding="utf-8") as f:
        f_map = f.readlines()
    return f_map


def player_move():
    pass


def enemy_move():
    pass


def place_enemy_on_map(f_map: list, count: int = 1):
    assert count <= 10, "Слишком много Enemy (count)"
    while count > 0:
        rand = randint(Length_object+1, len(f_map[1]) - Length_object)
        f_map[1] = f_map[1][:rand] + "E" + f_map[1][rand+1:]
        count -= 1
    return True


def place_player_on_map(size_map: tuple, f_map: list):
    rand = randint(Length_object + 1, len(f_map[size_map[1]-1]) - Length_object)
    f_map[size_map[1]-1] = str(f_map[size_map[1]-1][:rand]) + "P" + str(f_map[size_map[1]-1][rand + 1:])
    return True


if __name__ == "__main__":
    create_map(SIZE_MAP)
    List_str_MAP = read_map("map.txt")

    Enemy_placed = place_enemy_on_map(f_map=List_str_MAP, count=10)
    Player_placed = place_player_on_map(size_map=SIZE_MAP, f_map=List_str_MAP)

    if Enemy_placed and Player_placed:
        while True:
            os.system('cls')  # Отчищаем консоль
            for i in List_str_MAP:
                print(i, end="")
            time.sleep(1)
