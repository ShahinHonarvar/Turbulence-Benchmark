
def all_right_truncatable_prime(nums):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    x = nums[10]
    right_truncatable_primes = []

    for num in range(x-1, 1, -1):
        temp = num
        is_right_truncatable_prime = True
        while temp > 0:
            if not is_prime(temp):
                is_right_truncatable_prime = False
                break
            temp //= 10
        if is_right_truncatable_prime:
            right_truncatable_primes.append(num)

    return sorted(right_truncatable_primes, reverse=True)
