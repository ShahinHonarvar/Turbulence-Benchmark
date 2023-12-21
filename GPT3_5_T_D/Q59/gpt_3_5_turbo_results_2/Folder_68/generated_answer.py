
def all_left_truncatable_prime(nums):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    primes = []
    for i in range(2, nums[1]):
        if '0' not in str(i):
            truncatable = True
            for j in range(1, len(str(i))):
                if not is_prime(int(str(i)[j:])):
                    truncatable = False
                    break
            if truncatable:
                primes.append(i)
    return sorted(primes, reverse=True)
