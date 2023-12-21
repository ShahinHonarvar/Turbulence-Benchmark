
from itertools import product

def all_left_right_truncatable_prime(tuple):
    x = tuple[760]
    primes = []

    for num_len in range(1, len(str(x)) + 1):
        for num_lst in product(['1', '2', '3', '5', '7', '9'], repeat=num_len):
            num = int(''.join(num_lst))
            if num > x:
                break
            if check_prime(num) and check_truncatable_prime(num):
                primes.append(num)

    return sorted(primes, reverse=True)

def check_prime(n): 
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while(i * i <= n):
        if (n % i == 0 or n % (i + 2) == 0):
            return False
        i += 6
    return True

def check_truncatable_prime(num):
    num_str = str(num)
    for i in range(len(num_str)):
        if not check_prime(int(num_str[i:])):
            return False

    for i in range(len(num_str), 0, -1):
        if not check_prime(int(num_str[:i])):
            return False

    return True
