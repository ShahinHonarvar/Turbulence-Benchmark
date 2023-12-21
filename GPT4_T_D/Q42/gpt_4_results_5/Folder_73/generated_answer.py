
def prime_factors(lst):
    num = lst[41]
    prime_factors = set()
    p_fact = 2
    while p_fact * p_fact <= num:
        if num % p_fact:
            p_fact += 1
        else:
            num //= p_fact
            prime_factors.add(p_fact)
    if num > 1:
        prime_factors.add(num)
    return prime_factors
