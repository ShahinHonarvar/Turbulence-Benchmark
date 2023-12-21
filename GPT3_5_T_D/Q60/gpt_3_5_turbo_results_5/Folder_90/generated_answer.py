
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(nums):
    primes = []
    for num in nums:
        if is_prime(num) and '0' not in str(num):
            left_truncatable = True
            right_truncatable = True
            for i in range(1, len(str(num))):
                left_truncatable = left_truncatable and is_prime(int(str(num)[i:]))
                right_truncatable = right_truncatable and is_prime(int(str(num)[:-i]))
                if not left_truncatable or not right_truncatable:
                    break
            if left_truncatable or right_truncatable:
                primes.append(num)
    
    return sorted(primes, reverse=True)
