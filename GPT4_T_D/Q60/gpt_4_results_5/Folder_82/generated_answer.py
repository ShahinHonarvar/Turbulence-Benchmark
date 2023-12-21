
def all_left_right_truncatable_prime(nums):
    x = nums[69]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable(n):
        if '0' in str(n):
            return False
        for i in range(1, len(str(n))):
            left, right = int(str(n)[i:]), int(str(n)[:-i])
            if not is_prime(left) or not is_prime(right):
                return False
        return True

    truncatable_primes = [i for i in range(11, x+1) if is_prime(i) and is_truncatable(i)]
    truncatable_primes.sort(reverse=True)
    return truncatable_primes
