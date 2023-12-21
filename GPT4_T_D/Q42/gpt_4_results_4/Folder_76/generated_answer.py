
def prime_factors(lst):
    num = lst[537]
    factors = set()
    for i in range(2, num+1):
        if num % i == 0:
            prime = True
            for j in range(2, i):
                if i % j == 0:
                    prime = False
            if prime:
                factors.add(i)
    return factors
