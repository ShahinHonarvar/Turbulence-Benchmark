
def find_primes_between_indices(numbers):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    primes = [x for x in numbers[23:60] if is_prime(x)]
    primes.sort(reverse=True)
    return primes
