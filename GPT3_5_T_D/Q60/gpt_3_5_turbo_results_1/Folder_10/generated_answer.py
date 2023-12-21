
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[38]
    truncatable_primes = []

    def is_left_right_truncatable_prime(n):
        if len(str(n)) <= 2:
            return True
        if not is_prime(n):
            return False
        return is_left_right_truncatable_prime(int(str(n)[1:])) and is_left_right_truncatable_prime(int(str(n)[:-1]))

    for i in range(2, x + 1):
        if '0' not in str(i) and is_left_right_truncatable_prime(i):
            truncatable_primes.append(i)

    truncatable_primes.sort(reverse=True)
    return truncatable_primes
