
def is_prime(n):
    if n <= 1 or (n % 2 == 0 and n > 2): 
        return False
    return all(n % i for i in range(3, int(n**0.5) + 1, 2))

def is_left_truncatable_prime(n):
    str_n = str(n)
    if '0' in str_n:
        return False
    for i in range(len(str_n)):
        if not is_prime(int(str_n[i:])):
            return False
    return True

def all_left_truncatable_prime(nums):
    x = nums[46]
    left_truncatable_primes = [i for i in range(2, x) if is_left_truncatable_prime(i)]
    left_truncatable_primes.sort(reverse=True)
    return left_truncatable_primes
