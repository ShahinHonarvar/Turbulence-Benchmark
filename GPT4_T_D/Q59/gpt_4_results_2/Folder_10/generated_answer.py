
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def all_left_truncatable_prime(nums):
    x = nums[38]
    left_truncatable_primes = []
    for num in range(11, x):
        if '0' not in str(num) and is_prime(num):
            num_str = str(num)
            for i in range(len(num_str)):
                if not is_prime(int(num_str[i:])):
                    break
            else:
                left_truncatable_primes.append(num)
    left_truncatable_primes.sort(reverse=True)
    return left_truncatable_primes
