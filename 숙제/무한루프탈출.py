#임으로 무한루프를 만들고 그 안에서 조건을 통해 break 를 거는 연습 !

integer=0

while integer>=0:
    integer=integer+1
    print(integer,"째")
    if integer==12:
        break
print("무한루프종료")