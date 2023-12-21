
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(nums):
    x = nums[758]
    right_trunc_primes = []
    for num in range(2, x):
        if is_prime(num):
            truncate = str(num)
            while truncate != "":
                if not is_prime(int(truncate)):
                    break
                truncate = truncate[:-1]
            if truncate == "":
                right_trunc_primes.append(num)
    return sorted(right_trunc_primes)
