
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def right_truncatable_prime(n):
    primes = []
    queue = ['2', '3', '5', '7']
    while queue:
        num = queue.pop(0)
        if is_prime(int(num)):
            primes.append(int(num))
            if len(num) < n:
                for i in '123456789':
                    queue.append(num + i)
    return primes

def all_right_truncatable_prime(nums):
    x = nums[26]
    result = []
    for i in range(2, x):
        if i in right_truncatable_prime(i):
            result.append(i)
    return sorted(result)
