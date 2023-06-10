from deep_green import DeepGreen
from automatic_game import CompWithCompGame

def Game():
    # считываем настройки из файла в переменнуб lines
    f = open('settings.txt', 'r')
    lines = [line.strip() for line in f]
    f.close()
    l = lines[0].split()

    # определяем режим игры: человек-компьютер или компьютер-компьютер
    if l[2] == 'Comp_vs_Comp':
        cwc = CompWithCompGame()
        cwc.Game(lines)
    else:
        dg = DeepGreen()
        dg.Game(lines)

Game()
# 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0
