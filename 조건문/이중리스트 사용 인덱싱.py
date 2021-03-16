# and 조건을 사용하여 suspects 이중 리스트 중 범인을 탐색하는 소스코드

suspects =[['거위','새','암컷'],['푸들','개','수컷'],['비글','개','암컷']]

for suspect in suspects:
    if suspect[1]=='개' and suspect[2]=='암컷':
        print('범인은',suspect[0],'입니다')