
def find_primes_between_indices(int_list):

    def is_prime(n):
        if n == 1 or n == 0:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    return sorted([x for x in int_list[459:782] if is_prime(x)])
