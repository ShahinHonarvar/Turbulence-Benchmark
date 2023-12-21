def all_left_truncatable_prime(nums):
    return sorted(list(filter(left_truncatable_prime, range(1, int(nums[30]) + 1))))
def left_truncatable_prime(n):
    if n == 1:
        return True
    while n % 2 == 0:
        n /= 2
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True
