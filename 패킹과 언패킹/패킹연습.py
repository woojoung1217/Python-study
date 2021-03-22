#패킹과 언패킹을 사용해서 변수값을 서로 바꿔주는 연습


dodo = '박하맛'

alice= '딸기맛'

print('도도새:',dodo,'엘리스:',alice)

dodo,alice = alice,dodo

print('도도새:',alice,'엘리스:',dodo)