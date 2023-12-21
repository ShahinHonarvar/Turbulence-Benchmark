
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(nums):
    x = nums[91]
    right_truncatable_primes = []
    for num in range(2, x):
        if is_prime(num):
            num_copy = num
            is_right_truncatable = True
            while num_copy > 0:
                if not is_prime(num_copy):
                    is_right_truncatable = False
                    break
                num_copy = num_copy // 10
            if is_right_truncatable:
                right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes)
