
def prime_factors(my_list):
    return set(factorize(my_list[43])) & prime_numbers(my_list[43])
def factorize(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i == 0:
            factors.append(i)
            n //= i
        else:
            i += 1
    return n if n > 1 else []
def prime_numbers(n):

    return {x for x in range(2, int(n ** 0.5) + 1) if n % x == 0}
