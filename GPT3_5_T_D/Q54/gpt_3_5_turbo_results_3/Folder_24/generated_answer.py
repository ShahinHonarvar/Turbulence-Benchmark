
def all_right_truncatable_prime(numbers):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    x = numbers[65]
    primes = []
    for num in range(2, x):
        if is_prime(num):
            prime = str(num)
            is_right_truncatable_prime = True
            for i in range(1, len(prime)):
                if not is_prime(int(prime[:-i])):
                    is_right_truncatable_prime = False
                    break
            if is_right_truncatable_prime:
                primes.append(num)
    return sorted(primes, reverse=True)
