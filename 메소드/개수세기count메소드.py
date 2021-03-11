cards=['하트','클로버','다이아','하트']

value = cards.count('하트')  #count 메소드를 사용하여 리스트안에 하트를 찾아 value 변수의 대입 
print(value)

cards.append('하트')    #append 로 끝에 하트를 추가 
value = cards.count('하트') #count로 개수 세기 
print(value)  
del cards[3]  #del 메소드로 4번째 요소 삭제 
value = cards.count('하트')
print(value)
