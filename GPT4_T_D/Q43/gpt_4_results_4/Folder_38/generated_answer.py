
def find_primes_between_indices(int_list):
    def is_prime(n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n%2 == 0:
            return False
        sqr = int(n**0.5) + 1
        for divisor in range(3, sqr, 2):
            if n%divisor == 0:
                return False
        return True

    return sorted([num for num in int_list[55:88] if is_prime(num)])
