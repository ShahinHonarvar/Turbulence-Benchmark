
def all_right_truncatable_prime(nums):
    prime_numbers = []
    for num in nums:
        if is_prime(num) and is_truncatable_prime(num):
            prime_numbers.append(num)
    return sorted(prime_numbers)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_truncatable_prime(n):
    if not is_prime(n):
        return False
    while n > 0:
        if not is_prime(n):
            return False
        n //= 10
    return True
