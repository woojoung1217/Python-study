# 무한루프를 사용하여 올바른 답을 고를 때 가지 반복하기 


while True :
    answer=input("런던,파리,서울 중 영국의 수도는 어디 일까요?")
    if answer =='런던':
        print("그렇죠 정답이에요 ")
        break
    elif answer =='서울':
        print("서울은 대한민국의 수도 입니다")
    elif answer=='파리' :
        print("파리는 프랑스의 수도 입니다")
    else :
        print("보기중에서 골라주세요 ")
