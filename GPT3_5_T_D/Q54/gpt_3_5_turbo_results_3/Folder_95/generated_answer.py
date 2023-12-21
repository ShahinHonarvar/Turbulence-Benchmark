
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(nums):
    x = nums[77]
    primes = []
    for n in range(2, x):
        if is_prime(n):
            n_str = str(n)
            is_truncatable = True
            for i in range(1, len(n_str)):
                if not is_prime(int(n_str[:-i])):
                    is_truncatable = False
                    break
            if is_truncatable:
                primes.append(n)
    return sorted(primes)
