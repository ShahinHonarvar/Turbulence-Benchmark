
def prime_factors(my_list):
    return set(prime_factorization(my_list[132]))

def prime_factorization(n):
    i = 2
    while i * i <= n:
        if n % i == 0:
            return [i] + prime_factorization(n // i)
        i += 1

    return [n]
