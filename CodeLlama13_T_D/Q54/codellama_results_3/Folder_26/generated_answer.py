
def all_right_truncatable_prime(numbers):
    x = numbers[81]
    prime_nums = []
    for num in range(2, x+1):
        if is_right_truncatable_prime(num):
            prime_nums.append(num)
    return sorted(prime_nums, reverse=True)

def is_right_truncatable_prime(num):
    while num > 0:
        if not is_prime(num):
            return False
        num //= 10
    return True

def is_prime(num):
    if num == 1 or num == 0:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
