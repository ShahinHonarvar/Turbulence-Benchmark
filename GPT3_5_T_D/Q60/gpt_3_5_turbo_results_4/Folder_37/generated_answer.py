
def all_left_right_truncatable_prime(nums):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def is_truncatable_prime(num):
        if '0' in str(num):
            return False
        if len(str(num)) <= 2:
            return is_prime(num)
        if not is_prime(num):
            return False
        return is_truncatable_prime(int(str(num)[1:])) and is_truncatable_prime(int(str(num)[:-1]))

    x = nums[35]
    truncatable_primes = [num for num in range(2, x + 1) if is_truncatable_prime(num)]
    truncatable_primes.sort(reverse=True)
    return truncatable_primes
