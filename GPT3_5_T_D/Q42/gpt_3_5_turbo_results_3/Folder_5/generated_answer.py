
def prime_factors(lst):
    num = lst[67]
    factors = set()
    for i in range(2, int(num/2)+1):
        if num % i == 0:
            for j in range(2, i):
                if i % j == 0:
                    break
            else:
                factors.add(i)
    return factors
