
from itertools import permutations

def all_left_right_truncatable_prime(input_tuple):
    x = input_tuple[39]
    prime_list = list_of_primes(x)
    truncatable_primes = []
    for prime in prime_list:
        if is_left_right_truncatable(prime):
            truncatable_primes.append(prime)
    return truncatable_primes

def list_of_primes(n):
    sieve = [True] * (n+1)
    for x in range(2, int(n**0.5) + 1):
        if sieve[x]:
            for i in range(x*x, n + 1, x):
                sieve[i] = False
    return [x for x in range(2, n+1) if sieve[x]]

def is_prime(n):
    if n<2: 
        return False
    if n==2 or n==3: 
        return True
    if n%2==0 or n%3==0: 
        return False
    for i in range(5,int(n**0.5)+1,6):
        if n%i==0 or n%(i+2)==0:
            return False
    return True

def is_left_right_truncatable(n):
    n_str = str(n)
    if '0' in n_str:
        return False
    for i in range(1, len(n_str)):
        if not is_prime(int(n_str[i:])) or not is_prime(int(n_str[:i])):
            return False
    return True
