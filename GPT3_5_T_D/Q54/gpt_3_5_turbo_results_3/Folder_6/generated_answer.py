
def all_right_truncatable_prime(nums):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    x = nums[74]
    right_truncatable_primes = []
    for i in range(2, x):
        if is_prime(i):
            is_right_truncatable = True
            num = i
            while num > 10:
                num = num // 10
                if not is_prime(num):
                    is_right_truncatable = False
                    break
            if is_right_truncatable:
                right_truncatable_primes.append(i)
     
    return sorted(right_truncatable_primes)
