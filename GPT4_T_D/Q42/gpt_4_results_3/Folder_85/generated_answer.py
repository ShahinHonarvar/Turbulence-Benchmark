
def prime_factors(numbers):
    def is_prime(n):
        if n <= 1 or (n % 2 == 0 and n > 2): 
            return False
        return all(n % i for i in range(3, int(n**0.5) + 1, 2))

    num = numbers[23]
    factors = set()
    for i in range(2, num+1):
        while num % i == 0:
            if is_prime(i):
                factors.add(i)
            num = num // i
    return factors
