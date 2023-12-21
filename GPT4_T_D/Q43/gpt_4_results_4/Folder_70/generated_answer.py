
def find_primes_between_indices(nums):
    def is_prime(n):
        if n <= 1:
            return False
        elif n <= 3:
            return True
        elif n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    if len(nums) < 816:
        return []
    primes = []
    for i in range(131, 816):
        if is_prime(nums[i]):
            primes.append(nums[i])
    primes.sort(reverse=True)
    return primes
