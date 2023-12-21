
from sympy import isprime

def all_right_truncatable_prime(numbers):
    x = numbers[126]
    all_nums = [num for num in range(2, x)]
    right_truncatable_primes = []

    for num in all_nums:
        temp_num = num
        while temp_num > 0:
            if isprime(temp_num):
                temp_num = temp_num // 10
            else:
                break
        if temp_num == 0:
            right_truncatable_primes.append(num)
    
    right_truncatable_primes.sort(reverse=True)
    return right_truncatable_primes
