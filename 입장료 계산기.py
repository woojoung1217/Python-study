#입장료 계산기 for 문과 리스트 사용  20세 이상 :8000원 10세 이상 : 5000원 10세 미만 : 2500원 

total_price = 0

ages=[22,21,17,32,4,28,19,8]

for age in ages:
    if age >=20:
        total_price=total_price+8000
    elif age >=10:
        total_price=total_price+5000
    else:
        total_price=total_price+2500
print("총 입장료는",total_price,"원 입니다")