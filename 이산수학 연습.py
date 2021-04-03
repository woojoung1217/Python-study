
n=int(input(" 입 력 -> "))
count=0
def is_prime(n):
    for i in range(1,n+1):
        if n%i==0:
            return False
    return True
    count=count+1


print(count)

