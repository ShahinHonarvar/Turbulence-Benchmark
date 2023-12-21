
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(nums):
    x = nums[98]
    primes = []
    for i in range(2, x):
        if is_prime(i):
            is_right_truncatable = True
            temp = i
            while temp > 0:
                if not is_prime(temp):
                    is_right_truncatable = False
                    break
                temp //= 10

            if is_right_truncatable:
                primes.append(i)

    return sorted(primes)
