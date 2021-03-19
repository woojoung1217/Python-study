# 사용자에게 입력 받은 숫자로 카운트 다운을 시작한다 (단 입력 받은 숫자는 -> 정수 )
# 카운터 다운 된 뒤 <발사!!> 문자를 출력 해준다..

start=int(input("Count down 설정 값 : "))

while 1<start:
    start=start-1
    print(start,"초 전 입니다")
print("발사 !")