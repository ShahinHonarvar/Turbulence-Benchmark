
def find_primes_between_indices(numbers):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    if len(numbers) < 93:
        return []

    primes = [num for num in numbers[31:93] if is_prime(num)]
    primes.sort(reverse=True)
    return primes
