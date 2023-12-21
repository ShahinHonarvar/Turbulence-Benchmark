
def find_primes_between_indices(lst):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    prime_indices = []
    for i in range(23, 60):
        if is_prime(lst[i]):
            prime_indices.append(i)

    prime_indices.sort(reverse=True)
    prime_numbers = [lst[i] for i in prime_indices]
    return prime_numbers
