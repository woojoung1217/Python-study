#리스트에서 무작위로 사용자를 선택하여 무작위로 사용자를 뽑는다 한번 뽑은 사용자는 리스트에서 삭제되고 리스트에 사용자가 없을 때 까지 반복한다

import random

players_list =['player1','playrer2','player3']

while True :
    select_players=random.choice(players_list)
    print(select_players)
    if select_players==players_list[0]:
        del players_list[0]
    elif select_players==players_list[1]:
        del players_list[1]
    else :
        del players_list[2]
    print('남은 플레이어',players_list)
    if select_players==0:
        break
