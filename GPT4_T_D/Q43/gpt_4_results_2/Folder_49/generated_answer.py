
def find_primes_between_indices(lst):
    from sympy import isprime
    primes = [num for num in lst[22:51] if isprime(num)]
    primes.sort(reverse=True)

    return primes
