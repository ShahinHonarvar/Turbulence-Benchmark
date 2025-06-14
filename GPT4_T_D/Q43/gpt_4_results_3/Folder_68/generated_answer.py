
def find_primes_between_indices(numbers):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

    primes = [num for num in numbers[1:6] if is_prime(num)]
    primes.sort()
    return primes
