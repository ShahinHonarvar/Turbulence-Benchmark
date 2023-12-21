
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[94]
    primes = []
    for num in range(2, x + 1):
        if is_prime(num):
            primes.append(num)
    result = []
    for prime in primes:
        prime_str = str(prime)
        truncatable = True
        for i in range(len(prime_str)):
            if prime_str[i] == '0':
                truncatable = False
                break
            truncatable_num = int(prime_str[i:])
            if not is_prime(truncatable_num):
                truncatable = False
                break
            truncatable_num = int(prime_str[:i + 1])
            if not is_prime(truncatable_num):
                truncatable = False
                break
        if truncatable:
            result.append(prime)
    return result
