#패킹과 언패킹을 사용해서 변수값을 서로 바꿔주는 연습


dodo = '박하맛'

alice= '딸기맛'

print('도도새:',dodo,'엘리스:',alice) #패킹

dodo,alice = alice,dodo  #언패킹

print('도도새:',dodo,'엘리스:',alice)

# Python 외 다른언어에서 두 변수 안에 값을 변경하기 위해서는 값을 임시로 저장할 변수가 하나 더 필요하지만 
# Python 에서는 패킹과 언패킹의 특성으로 변수 2개만으로 가능하다.