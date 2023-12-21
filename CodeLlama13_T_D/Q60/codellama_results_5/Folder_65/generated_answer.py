
def all_left_right_truncatable_prime(nums):
    x = nums[32]
    primes = []
    for i in range(2, x+1):
        if is_prime(i) and is_truncatable(i):
            primes.append(i)
    return sorted(primes)

def is_prime(n):
    if n == 1 or n % 2 == 0:
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True

def is_truncatable(n):
    digits = list(str(n))
    while len(digits) > 1:
        if not is_prime(int(''.join(digits))):
            return False
        digits.pop()
    return True
