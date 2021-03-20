# 사용자에게 입력 받은 숫자로 카운트 다운을 시작한다 (단 입력 받은 숫자는 -> 정수 )
# 카운터 다운 된 뒤 <발사!!> 문자를 출력 해준다..
# 실제 시간을 측정하기 위한 도구로는 사용 될 수 없지만 while의 기본구조와 조건문을 이해하기 위함 ^ㅡ^

start=int(input("Count down 설정 값 : "))

while 1<start:
    start=start-1
    print(start,"초 전 입니다")
print("발사 !")