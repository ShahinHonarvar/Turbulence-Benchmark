
def all_right_truncatable_prime(nums):
    x = nums[97]
    primes = []
    for i in range(2, x+1):
        if is_prime(i) and is_right_truncatable(i):
            primes.append(i)
    return sorted(primes, reverse=True)

def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def is_right_truncatable(n):
    if len(str(n)) <= 1:
        return False
    while len(str(n)) > 1:
        if not is_prime(int(str(n)[:-1])):
            return False
        n //= 10
    return True
