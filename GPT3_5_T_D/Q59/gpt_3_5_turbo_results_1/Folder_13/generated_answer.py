
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def all_left_truncatable_prime(nums):
    x = nums[784]
    truncatable_primes = []
    for i in range(2, x):
        if '0' not in str(i):
            prime = True
            n = str(i)
            while len(n) > 1:
                n = n[1:]
                if not is_prime(int(n)):
                    prime = False
                    break
            if prime:
                truncatable_primes.append(i)
    return truncatable_primes
