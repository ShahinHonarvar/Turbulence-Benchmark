
from sympy import isprime
def all_left_right_truncatable_prime(numbers):
    x = numbers[7]
    results = []
    for num in range(2, x + 1):
        if '0' in str(num):
            continue
        num_str = str(num)
        left_right_truncatable = True
        for i in range(len(num_str)):
            left_truncated = int(num_str[i:])
            right_truncated = int(num_str[:len(num_str) - i])
            if not isprime(left_truncated) or not isprime(right_truncated):
                left_right_truncatable = False
                break
        if left_right_truncatable:
            results.append(num)
    results.sort()
    return results
