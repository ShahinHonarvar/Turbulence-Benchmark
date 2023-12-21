
def all_left_truncatable_prime(numbers):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    x = numbers[14]
    left_truncatable_primes = []
    for n in range(2, x):
        if '0' not in str(n):
            is_truncatable_prime = True
            for i in range(len(str(n))):
                if not is_prime(int(str(n)[i:])):
                    is_truncatable_prime = False
                    break
            if is_truncatable_prime:
                left_truncatable_primes.append(n)
    return sorted(left_truncatable_primes, reverse=True)
