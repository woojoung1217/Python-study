#파이선 알고리즘 연습 1부터10까지의 연산을 구하는 알고리즘 결과 값은 : 55 
n=10
s=0
for i in range(1,n+1):
    s=s+i
print(s) 

#2번째 방법

for i in range(1,n+1):
    s*(s+i) /2
print(s)