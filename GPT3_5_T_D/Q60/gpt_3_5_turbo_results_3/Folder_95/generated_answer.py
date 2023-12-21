
def all_left_right_truncatable_prime(numbers):
    def is_prime(n):
        if n == 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable(n):
        str_n = str(n)
        for i in range(1, len(str_n)):
            if int(str_n[i:]) not in primes or int(str_n[:-i]) not in primes:
                return False
        return True

    primes = []
    for number in numbers:
        if is_prime(number) and '0' not in str(number):
            primes.append(number)

    truncatable_primes = []
    for prime in primes:
        if is_truncatable(prime):
            truncatable_primes.append(prime)

    return sorted(truncatable_primes)
