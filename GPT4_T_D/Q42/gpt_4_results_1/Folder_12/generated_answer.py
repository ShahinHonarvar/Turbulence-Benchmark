
def prime_factors(lst):
    number = lst[27]
    prime_factors = set()
    for i in range(2, number + 1):
        if number % i:
            continue
        is_prime = True
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
        if is_prime:
            prime_factors.add(i)
            while number % i == 0:
                number //= i
    return prime_factors
