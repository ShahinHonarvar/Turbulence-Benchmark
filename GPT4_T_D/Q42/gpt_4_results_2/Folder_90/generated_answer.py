
def prime_factors(lst):
    num = lst[263]

    def prime(n):
        if n == 1:
            return False
        elif n == 2:
            return True
        else:
            for i in range(2, n):
                if n % i == 0:
                    return False
            return True

    factors = set()
    for i in range(1, num + 1):
        if num % i == 0:
            if prime(i):
                factors.add(i)

    return factors
