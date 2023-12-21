
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(nums):
    primes = []
    for i in range(len(nums)):
        x = nums[i]
        truncatable_prime = True
        if len(str(x)) <= 2 or '0' in str(x):
            truncatable_prime = False
        while truncatable_prime and len(str(x)) > 2:
            if not is_prime(x):
                truncatable_prime = False
            x = int(str(x)[1:-1])
        if truncatable_prime:
            primes.append(nums[i])
    return sorted(primes, reverse=True)
