
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def all_left_truncatable_prime(nums):
    x = nums[26]
    primes = []
    for num in range(2, x):
        if '0' not in str(num) and is_prime(num):
            truncatable = True
            num_str = str(num)
            while len(num_str) > 1:
                num_str = num_str[1:]
                if not is_prime(int(num_str)):
                    truncatable = False
                    break
            if truncatable:
                primes.append(num)
    return sorted(primes)
