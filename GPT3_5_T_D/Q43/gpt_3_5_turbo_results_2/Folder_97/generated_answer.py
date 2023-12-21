
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_primes_between_indices(lst):
    prime_nums = [num for num in lst[295:456] if is_prime(num)]
    return sorted(prime_nums, reverse=True)
