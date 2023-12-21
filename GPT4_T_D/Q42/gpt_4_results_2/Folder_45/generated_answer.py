
def prime_factors(lst):
    num = lst[33]
    prime_factors_set = set()
    div = 2
    while num > 1:
        if num % div == 0:
            prime_factors_set.add(div)
            num //= div
        else:
            div += 1
    return prime_factors_set
