
def prime_factors(my_list):
    return set(prime_factorize(my_list[478]))

def prime_factorize(n):
    i = 2
    while i * i <= n:
        if n % i == 0:
            return [i] + prime_factorize(n // i)
        i += 1

    return [n]
