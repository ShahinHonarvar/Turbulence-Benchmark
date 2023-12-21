
def prime_factors(lst):
    num = lst[59]
    factors = set()
    for i in range(1, num + 1):
        if num % i == 0:
            if i > 1:
                for j in range(2, i):
                    if i % j == 0:
                        break
                else:
                    factors.add(i)
    return factors
