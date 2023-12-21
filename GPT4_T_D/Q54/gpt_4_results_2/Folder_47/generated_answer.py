
def all_right_truncatable_prime(num_tuple):
    x = num_tuple[49]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable_prime(n):
        s = str(n)
        return all(is_prime(int(s[:i])) for i in range(len(s), 0, -1))

    right_truncatable_primes = [i for i in range(x) if is_right_truncatable_prime(i)]

    return sorted(right_truncatable_primes)
