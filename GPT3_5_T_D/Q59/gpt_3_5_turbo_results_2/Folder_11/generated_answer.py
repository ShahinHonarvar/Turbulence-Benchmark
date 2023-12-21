
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(nums):
    x = nums[86]
    left_truncatable_primes = []
    for num in range(2, x):
        if is_prime(num):
            truncated_num = str(num)
            while truncated_num:
                if not is_prime(int(truncated_num)):
                    break
                truncated_num = truncated_num[1:]
            else:
                left_truncatable_primes.append(num)
    return left_truncatable_primes
