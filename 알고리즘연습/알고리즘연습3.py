# 난수를 생성하여 UP & DOWN 게임
from random import *

random_num = randint(1,100) # 1부터10사이에 난수


while True:
    player_pick=int(input("숫자 입력 - > "))
    if player_pick==random_num:
        print("정답입니다 !")
        break
    elif player_pick > random_num:
        print(player_pick,'보다 낮습니다.')
    else :
        print(player_pick,'보다 높습니다.')