
def prime_factors(lst):
    num = lst[10]
    prime_factors_set = set()
    if num < 2:
        return prime_factors_set

    i = 2
    while i * i <= num:
        if num % i:
            i += 1
        else:
            num //= i
            prime_factors_set.add(i)

    if num > 1:
        prime_factors_set.add(num)
    return prime_factors_set
