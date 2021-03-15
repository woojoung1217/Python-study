## if 조건 : 
##      실행할_명령1
## else :
##      실행할_명령2

score = 60 

if score < 80:
    print("불합격 입니다")
else:
    print("합격 입니다")    

score =90

if 80<score<=100:
    print("학점은 A 입니다")
elif 60<score<=80:
    print("학점은 B 입니다")
elif 50<score<=70:
    print("학점은 C 입니다")
else:  
    print("학점은 D 입니다")