
def find_primes_between_indices(numbers):
    primes = []
    for i in range(16, min(72, len(numbers))):
        num = numbers[i]
        if num > 1:
            is_prime = True
            for j in range(2, int(num ** 0.5) + 1):
                if num % j == 0:
                    is_prime = False
                    break
            if is_prime:
                primes.append(num)
    return sorted(primes)
