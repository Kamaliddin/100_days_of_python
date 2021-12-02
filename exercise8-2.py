def prime(number):
    res = 0
    for i in range(1, number+1):
        if number % i == 0:
            res+=1
    if res == 2:
        return True 
    return False

print(prime(1))