
def find_primes_between_indices(numbers):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return True

    if len(numbers) < 26:
        return []

    primes_between_indices = [number for number in numbers[16:26] if is_prime(number)]
    primes_between_indices.sort(reverse=True)

    return primes_between_indices
