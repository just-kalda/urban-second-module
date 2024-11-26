numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []

for num in numbers:
    is_prime = True
    
    for check_num in range(2, num):
        if num % check_num == 0:
            is_prime = False
            break
    
    if num == 1:
        continue    
    elif is_prime == True:
        primes.append(num)
    else:
        not_primes.append(num)
        
print(f"Простые числа: {primes}")
print(f"Не простые числа: {not_primes}"
