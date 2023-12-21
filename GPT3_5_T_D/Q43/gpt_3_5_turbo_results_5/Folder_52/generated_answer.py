
def find_primes_between_indices(numbers):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    prime_numbers = []
    for num in numbers[33:60]:
        if is_prime(num):
            prime_numbers.append(num)

    return sorted(prime_numbers, reverse=True)
