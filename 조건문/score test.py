# 스코어 리스트 안에 점수가 70점 이상 인 경우 합격자 명 수를 출력 

stu_score = [100,20,30,40,60,70,99]

#결과 3명 입니다.

value =0
for score in stu_score:
    if score >= 70:
        value = value+1
print('합격자는',value,'명 입니다')    

