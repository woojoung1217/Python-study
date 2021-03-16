# 반복문 과 조건문을 사용  / 리스트 안 숫자가 10 이상이면 삭제하고 출력 


number=[1,2,10,4,5,12]

# 출력값  : [1,2,4,5]

for i in number[:]: #카피 값 사용 number 의 인덱스는 건들지 않고 삭제 해야함
   if 10 <= i:
       number.remove(i)
        

print(number)