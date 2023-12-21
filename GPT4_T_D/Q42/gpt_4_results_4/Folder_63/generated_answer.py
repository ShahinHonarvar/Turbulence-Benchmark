
def prime_factors(integer_list):
    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

    def get_prime_factors(n):
        factors = set()
        for i in range(2, n+1):
            if n % i == 0:
                if is_prime(i):
                    factors.add(i)
        return factors

    if 57 < len(integer_list):
        return get_prime_factors(integer_list[57])
    else:
        return "Index out of range!"
