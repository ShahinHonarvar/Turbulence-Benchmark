
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(nums):
    def is_truncatable_prime(num):
        if '0' in str(num):
            return False
        while len(str(num)) > 2:
            if not is_prime(num):
                return False
            num = int(str(num)[1:-1])
        return is_prime(num)

    x = nums[74]
    truncatable_primes = []
    for i in range(2, x + 1):
        if is_truncatable_prime(i):
            truncatable_primes.append(i)

    return truncatable_primes
