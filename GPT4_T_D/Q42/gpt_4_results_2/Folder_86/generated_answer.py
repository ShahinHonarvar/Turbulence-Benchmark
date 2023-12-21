
def prime_factors(list_of_nums):
    num = list_of_nums[194]
    factors = set()
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    for i in range(2, num + 1):
        if num % i == 0:
            if is_prime(i):
                factors.add(i)
    return factors
