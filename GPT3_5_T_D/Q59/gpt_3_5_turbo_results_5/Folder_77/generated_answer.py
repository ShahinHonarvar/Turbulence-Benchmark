
def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def all_left_truncatable_prime(nums):
    x = nums[767]
    primes = []
    for i in range(2, x):
        if '0' not in str(i):
            is_left_truncatable = True
            for j in range(2, len(str(i)) + 1):
                if not is_prime(int(str(i)[j - 1:])):
                    is_left_truncatable = False
                    break
            if is_left_truncatable:
                primes.append(i)
    return sorted(primes, reverse=True)
