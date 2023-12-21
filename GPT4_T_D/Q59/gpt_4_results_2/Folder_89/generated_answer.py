
from sympy import isprime

def all_left_truncatable_prime(numbers):
    x = numbers[97]
    primes = []

    for i in range(x):
        if i > 10:
            i_str = str(i)
            if '0' not in i_str:
                potential_trunc_primes = [i_str[j:] for j in range(len(i_str))]
                if all(isprime(int(num)) for num in potential_trunc_primes):
                    primes.append(i)

    return sorted(primes, reverse=True)
