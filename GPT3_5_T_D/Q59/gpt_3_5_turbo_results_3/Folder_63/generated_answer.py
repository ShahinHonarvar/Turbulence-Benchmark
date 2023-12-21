
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(nums):
    x = nums[88]
    primes = []
    for num in range(2, x):
        if '0' not in str(num):
            is_left_truncatable_prime = True
            for i in range(len(str(num))):
                if not is_prime(int(str(num)[i:])):
                    is_left_truncatable_prime = False
                    break
            if is_left_truncatable_prime:
                primes.append(num)
    return primes
