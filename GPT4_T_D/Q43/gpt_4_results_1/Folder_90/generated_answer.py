
def find_primes_between_indices(numbers):
    def is_prime(n):
        if n == 1 or n == 0:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    nums = numbers[413:449]
    primes = [x for x in nums if is_prime(x)]
    primes.sort()
    return primes
