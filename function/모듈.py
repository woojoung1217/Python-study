# 모듈은 이미 많은 모듈이 존재해 가져다 쓰면 빠른시간내 프로그램 작성이 가능함
# random 이 가장 기본적인 모듈 
#random.choice(무작위로 하나를 정하고) random.sample(리스트,뽑을개수)
import random  #random 모듈을 import 함으로서 사용가능해진다
    
numbers=[1,2,3,4,5,6] #넘버 리스트에서 난수를 생성할 수 있어진다.

print(random.choice(numbers)) # 무작위로 하나
print(random.sample(numbers,3)) # 리스트중에 3개를 무작위로
print(random.randint(1,100)) # 정수형 중에서 범위에서 무작위로