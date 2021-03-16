# 조건식 에서 or 사용하기 or =  둘 중 하나만 만족해도 True


todays_meal = 1 #오늘 하루 식사 횟 수

if todays_meal >= 1 or todays_meal >=3: 
  print("오늘은 식사를 하셨습니다")
elif todays_meal <1:
  print("오늘은 식사를 안 했습니다")
