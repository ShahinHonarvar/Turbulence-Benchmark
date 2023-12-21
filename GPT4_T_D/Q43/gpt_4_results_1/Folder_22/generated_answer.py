
def find_primes_between_indices(num_list):
    def is_prime(n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        sqr = int(n**0.5) + 1
        for divisor in range(3, sqr, 2):
            if n % divisor == 0:
                return False
        return True

    primes_list = [num for num in num_list[75:86] if is_prime(num)]
    return sorted(primes_list)
