
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(nums):
    primes = []
    for x in nums:
        if '0' not in str(x) and is_prime(x):
            str_x = str(x)
            for i in range(len(str_x)):
                left = int(str_x[i:])
                right = int(str_x[:i+1])
                if is_prime(left) and is_prime(right):
                    primes.append(x)
                    break
    return sorted(primes, reverse=True)
