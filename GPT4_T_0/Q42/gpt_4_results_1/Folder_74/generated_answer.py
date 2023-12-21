
def prime_factors(lst):
    num = lst[48]
    prime_factors = set()
    i = 2
    while i * i <= num:
        if num % i:
            i += 1
        else:
            num //= i
            prime_factors.add(i)
    if num > 1:
        prime_factors.add(num)
    return prime_factors
