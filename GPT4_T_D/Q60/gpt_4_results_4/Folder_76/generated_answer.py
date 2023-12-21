
from sympy import isprime

def all_left_right_truncatable_prime(numbers):
    x = numbers[370]
    truncatable_primes = []
    for num in range(13, x+1):
        if '0' in str(num): 
            continue
        num_str = str(num)
        length = len(num_str)
        left_right_truncations = [num_str[i:length-i] for i in range(length)]
        if all(isprime(int(num_str)) for num_str in left_right_truncations):
            truncatable_primes.append(num)
    return sorted(truncatable_primes, reverse=True)
