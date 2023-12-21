
def all_right_truncatable_prime(numbers):
    prime_nums = []
    for num in numbers:
        if is_right_truncatable_prime(num):
            prime_nums.append(num)
    return sorted(prime_nums)

def is_right_truncatable_prime(num):
    if num < 10:
        return False
    for i in range(1, len(str(num))):
        if not is_prime(int(str(num)[:-i])):
            return False
    return True

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
