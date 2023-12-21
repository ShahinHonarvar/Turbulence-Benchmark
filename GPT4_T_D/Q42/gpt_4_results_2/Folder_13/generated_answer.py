
def prime_factors(int_list):
    def is_prime(n):
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def factors(n):
        result = set()
        for i in range(2, n + 1):
            if n % i == 0:
                if is_prime(i):
                    result.add(i)
        return result

    return factors(int_list[126])
