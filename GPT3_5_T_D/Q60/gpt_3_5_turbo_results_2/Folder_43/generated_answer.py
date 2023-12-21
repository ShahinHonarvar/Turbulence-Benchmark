
def all_left_right_truncatable_prime(nums):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(n):
        if '0' in str(n):
            return False
        num_str = str(n)
        for i in range(1, len(num_str)):
            left_truncated = int(num_str[:i])
            right_truncated = int(num_str[i:])
            if not is_prime(left_truncated) or not is_prime(right_truncated):
                return False
        return True

    x = nums[89]
    truncatable_primes = []
    for num in range(2, x + 1):
        if is_prime(num) and is_truncatable_prime(num):
            truncatable_primes.append(num)
    truncatable_primes.sort(reverse=True)
    return truncatable_primes
