
def all_right_truncatable_prime(nums):
    x = nums[370]
    prime_nums = []
    for i in range(2, x+1):
        if is_prime(i) and is_right_truncatable_prime(i):
            prime_nums.append(i)
    return sorted(prime_nums, reverse=True)

def is_prime(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def is_right_truncatable_prime(n):
    while n > 1:
        if not is_prime(n):
            return False
        n //= 10
    return True
