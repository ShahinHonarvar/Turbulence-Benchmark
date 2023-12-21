
def prime_factors(integer_lst):
    num = integer_lst[42]
    factors = set()
    for i in range(2, num+1):
        if num % i == 0:
            for j in range(2, i):
                if i % j == 0:
                    break
            else:
                factors.add(i)
    return factors
