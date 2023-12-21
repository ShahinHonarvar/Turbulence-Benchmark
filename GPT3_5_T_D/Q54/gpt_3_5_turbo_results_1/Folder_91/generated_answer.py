
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(nums):
    x = nums[0]
    primes = []
    for num in range(x-1, 1, -1):
        if is_prime(num):
            current = num
            while current > 0:
                if not is_prime(current):
                    break
                current = current // 10
            else:
                primes.append(num)
    return sorted(primes, reverse=True)
