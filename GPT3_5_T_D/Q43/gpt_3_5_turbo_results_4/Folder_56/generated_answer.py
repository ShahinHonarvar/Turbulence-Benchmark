
def find_primes_between_indices(lst):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    prime_nums = []
    for i in range(40, 69):
        if is_prime(lst[i]):
            prime_nums.append(lst[i])

    return sorted(prime_nums, reverse=True)
