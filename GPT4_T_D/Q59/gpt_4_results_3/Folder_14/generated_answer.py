
from sympy import isprime

def all_left_truncatable_prime(numbers):
    x = numbers[78]
    result = []
    for number in range(11, x):
        num_str = str(number)
        if '0' in num_str:
            continue
        left_truncate_nums = [int(num_str[i:]) for i in range(len(num_str))]
        if all(isprime(num) for num in left_truncate_nums):
            result.append(number)
    return sorted(result, reverse=True)
