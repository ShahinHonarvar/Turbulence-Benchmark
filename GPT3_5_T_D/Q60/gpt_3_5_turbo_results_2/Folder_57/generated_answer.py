
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[54]
    truncatable_primes = []
    
    def is_left_truncatable(n):
        if len(str(n)) <= 2:
            return True
        if not is_prime(n):
            return False
        return is_left_truncatable(int(str(n)[1:]))

    def is_right_truncatable(n):
        if len(str(n)) <= 2:
            return True
        if not is_prime(n):
            return False
        return is_right_truncatable(int(str(n)[:-1]))

    for i in range(23, x + 1):
        if '0' in str(i):
            continue
        if is_prime(i) and is_left_truncatable(i) and is_right_truncatable(i):
            truncatable_primes.append(i)

    return sorted(truncatable_primes, reverse=True)
