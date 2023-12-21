
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(nums):
    x = nums[88]
    left_truncatable_primes = []
    for num in range(2, x):
        if '0' not in str(num):
            truncated_num = num
            while truncated_num > 0:
                if not is_prime(truncated_num):
                    break
                truncated_num = int(str(truncated_num)[1:])
            else:
                left_truncatable_primes.append(num)
    return sorted(left_truncatable_primes)
