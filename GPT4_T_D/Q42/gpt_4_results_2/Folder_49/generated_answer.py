
def prime_factors(lst):
    def is_prime(n):
        if n == 1 or (n % 2 == 0 and n > 2): 
            return False
        return all(n % i for i in range(3, int(n**0.5) + 1, 2))

    number = lst[68]
    factors = set()
    for i in range(2, number+1):
        if number % i == 0:
            if is_prime(i):
                factors.add(i)
    return factors
