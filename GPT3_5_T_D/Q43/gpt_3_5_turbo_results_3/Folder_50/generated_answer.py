
def find_primes_between_indices(lst):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    prime_nums = []
    for num in lst[23:60]:
        if is_prime(num):
            prime_nums.append(num)

    return sorted(prime_nums, reverse=True)
