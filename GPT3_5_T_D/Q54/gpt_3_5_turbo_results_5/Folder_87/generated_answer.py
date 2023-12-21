
def all_right_truncatable_prime(integers):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    x = integers[39]
    results = []

    def generate_right_truncatable_primes(p, digits):
        if len(digits) == 0:
            results.append(p)
        else:
            for d in digits:
                new_p = p * 10 + d
                if is_prime(new_p):
                    generate_right_truncatable_primes(new_p, digits[:-1])

    for digit in range(1, 10):
        if is_prime(digit):
            generate_right_truncatable_primes(digit, list(range(1, 10)))

    return sorted(results, reverse=True)
