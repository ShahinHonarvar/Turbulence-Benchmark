
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(nums):
    x = nums[39]
    truncatable_primes = []

    for i in range(2, x):
        if is_prime(i):
            truncatable = True
            num = str(i)
            for j in range(1, len(num)):
                trunc_num = int(num[:-j])
                if not is_prime(trunc_num):
                    truncatable = False
                    break
            if truncatable:
                truncatable_primes.append(i)

    return sorted(truncatable_primes)
