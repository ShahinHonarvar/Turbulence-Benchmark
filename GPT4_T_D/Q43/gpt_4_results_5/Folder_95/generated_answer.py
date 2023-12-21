
def find_primes_between_indices(numbers):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    primes_in_range = [num for num in numbers[19:72] if is_prime(num)]
    primes_in_range.sort()

    return primes_in_range
