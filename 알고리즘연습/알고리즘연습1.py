#알고리즘 연습 소수를 구하는 방법 
#1~100 까지의 소수를 구한다


n=100

def is_Prime(a):
  if(a<2):
    return False
  for i in range(2,a):
    if(a%i==0):
      return False
  return True

for i in range(n+1):
  if(is_Prime(i)):
    print(i)
