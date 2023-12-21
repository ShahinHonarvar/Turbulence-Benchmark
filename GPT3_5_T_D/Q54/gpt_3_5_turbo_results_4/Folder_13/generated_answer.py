
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(nums):
    x = nums[784] if len(nums) > 784 else 0
    if x < 10:
        return []
    primes = []
    for i in range(10, x):
        if is_prime(i):
            num_str = str(i)
            is_truncatable = True
            while num_str:
                if is_prime(int(num_str)):
                    num_str = num_str[:-1]
                else:
                    is_truncatable = False
                    break
            if is_truncatable:
                primes.append(i)
    return sorted(primes)
