
from itertools import combinations

def all_right_truncatable_prime(num_tuple):
    x = num_tuple[370]
    all_nums = list(range(2, x))

    def is_prime(n):
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable(n):
        num_string = str(n)
        for i in range(1, len(num_string)):
            if not is_prime(int(num_string[:-i])):
                return False
        return True

    prime_nums = filter(is_prime, all_nums)
    right_truncatable_primes = filter(is_right_truncatable, prime_nums)
    return sorted(right_truncatable_primes, reverse=True)
