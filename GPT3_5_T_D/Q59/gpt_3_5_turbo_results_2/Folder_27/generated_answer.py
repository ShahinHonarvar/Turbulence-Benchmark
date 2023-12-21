
def all_left_truncatable_prime(numbers):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def left_truncatable_prime(number):
        if '0' in str(number):
            return False
        while number > 0:
            if not is_prime(number):
                return False
            number = int(str(number)[1:])
        return True

    x = numbers[79]
    primes = []
    for i in range(2, x):
        if left_truncatable_prime(i):
            primes.append(i)
    return sorted(primes, reverse=True)
