
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(nums):
    def truncate_prime(n):
        str_num = str(n)
        primes = []
        for i in range(1, len(str_num)+1):
            left = int(str_num[:i])
            right = int(str_num[-i:])
            if is_prime(left) and is_prime(right):
                primes.append(n)
        return primes

    all_trunc_primes = []
    for num in nums:
        if '0' not in str(num):
            all_trunc_primes += truncate_prime(num)
    return sorted(all_trunc_primes, reverse=True)
