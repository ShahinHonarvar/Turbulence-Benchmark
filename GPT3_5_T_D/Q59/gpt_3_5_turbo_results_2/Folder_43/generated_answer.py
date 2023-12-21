
from sympy import isprime

def all_left_truncatable_prime(numbers):
    x = numbers[89]
    result = []
    for num in range(x - 1, 0, -1):
        num_str = str(num)
        if num_str[0] == '0':
            continue
        truncated = [int(num_str[i:]) for i in range(len(num_str))]
        if all(isprime(n) for n in truncated):
            result.append(num)
    return sorted(result, reverse=True)
