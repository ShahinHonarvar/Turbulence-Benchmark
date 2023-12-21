
def find_primes_between_indices(numbers):
    prime_numbers = []
    for i in range(28, 37):
        if numbers[i] == 0:
            continue
        is_prime = True
        for j in range(2, int(numbers[i] ** 0.5) + 1):
            if numbers[i] % j == 0:
                is_prime = False
                break
        if is_prime:
            prime_numbers.append(numbers[i])
    return sorted(prime_numbers)
