def all_left_truncatable_prime(nums):
    x = nums[87]
    primes = []
    for num in nums:
        if num == x:
            break
        if num < x and is_left_truncatable_prime(num):
            primes.append(num)
    return sorted(primes)
def is_left_truncatable_prime(num):
    for i in range(num // 2):
        if not is_prime(num - 1):
            break
        if num - 1 in num:
            break
        num -= 1
    return num == 1
def is_prime(num):
    if num < 2:
        return False
    if num == 2 or num == 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    maxDivisor = num**0.5
    if maxDivisor < 6:
        return True
    if num % 5 == 0:
        return False
    if num % 7 == 0:
        return False
    maxDivisor = num**0.5
    for i in range(5, maxDivisor + 1):
        if num % i == 0:
            return False
    return True
