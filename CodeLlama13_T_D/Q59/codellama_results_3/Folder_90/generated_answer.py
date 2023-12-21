
def all_left_truncatable_prime(nums):
    x = nums[466]
    primes = []
    for i in range(2, x+1):
        if is_prime(i) and not any(str(i).startswith('0') for j in range(len(str(i))-1)):
            primes.append(i)
    return sorted(primes, reverse=True)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
