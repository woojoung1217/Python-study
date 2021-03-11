candies=['딸기','레몬','수박맛','박하맛','우유맛']

#candies 리스트에서 콜라맛,포도맛 추가 / 박하맛 사탕 삭제


candies.append('콜라맛')   #append 사용 추가 
candies.append('포도맛')   #마지막에 추가됨 중간에 넣고싶으면?
del candies[3]   #del 로 삭제
 
print(candies)