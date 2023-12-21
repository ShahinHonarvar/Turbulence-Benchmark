
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(nums):
    x = nums[97]
    primes = []
    for i in range(2, x):
        if '0' not in str(i):
            truncated_num = str(i)
            while truncated_num:
                if not is_prime(int(truncated_num)):
                    break
                truncated_num = truncated_num[1:]
            else:
                primes.append(i)
    primes.sort(reverse=True)
    return primes
