
def prime_factors(lst):
    num = lst[51]
    prime_factors = []
    i = 2
    while i * i <= num:
        if num % i:
            i += 1
        else:
            num //= i
            prime_factors.append(i)
    if num > 1:
        prime_factors.append(num)
    return set(prime_factors)
