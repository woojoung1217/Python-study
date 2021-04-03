def is_prime(n):
    for i in range(2,n-1):
        if n%i==0:
           return False
        else:
            return True
            print("소수")

print(is_prime(10))
