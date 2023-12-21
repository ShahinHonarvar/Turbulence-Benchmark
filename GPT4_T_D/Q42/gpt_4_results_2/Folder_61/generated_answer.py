
def prime_factors(lst):
    num = lst[8]
    factors = set()
    i = 2
    while i < num:
        if num % i:
            i += 1
        else:
            factors.add(i)
            num //= i
    if num > 1:
        factors.add(num)
    prime_factors = [i for i in factors if all(i%j != 0 for j in range(2,int(i**0.5)+1))]
    return set(prime_factors)
