
def all_left_right_truncatable_prime(nums):
    primes = []
    for num in nums:
        if is_left_and_right_truncatable_prime(num):
            primes.append(num)
    return sorted(primes, reverse=True)

def is_left_and_right_truncatable_prime(num):
    while num > 1:
        if not is_prime(num):
            return False
        num = remove_last_digit(num)
        if num % 10 == 0:
            return False
    return True

def is_prime(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def remove_last_digit(num):
    return int(str(num)[:-1])
