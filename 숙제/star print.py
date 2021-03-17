#  * 을 순차적으로 증가 시켜 계단식 모양으로 출력하기 단 별의 갯수는 input 으로 사용자에게 입력 받는다 

x=int(input("출력 * 갯수 입력 : "))

for i in range(1,x+1):
    for j in range(i):
        print("*",end="")
    print()
