
def prime_factors(numbers):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    prime_set = set()
    num = numbers[990]
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0 and is_prime(i):
            prime_set.add(i)
    return prime_set
