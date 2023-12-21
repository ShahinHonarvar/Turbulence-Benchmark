
from itertools import permutations

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[92]
    primes = []
    for num in range(10, x + 1):
        num_str = str(num)
        if '0' in num_str:
            continue
        prime = True
        for i in range(len(num_str)):
            if not is_prime(int(num_str[i:])):
                prime = False
                break
            if not is_prime(int(num_str[:i+1])):
                prime = False
                break
        if prime:
            primes.append(num)
    return primes
