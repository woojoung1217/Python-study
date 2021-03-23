# list에서는 .append 를 사용해 추가했지만 딕셔너리에는 append 가 사용되지 않는다.
# 딕셔너리 에서는 딕셔너리[추가할_키] = 추가할_값 방식이다.

my_dict1={'이름':'윤우중','나이':'24'}

print(my_dict1)
my_dict1['나이']='25'
print(my_dict1)
