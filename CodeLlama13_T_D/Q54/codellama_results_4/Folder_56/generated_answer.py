
def all_right_truncatable_prime(numbers):
    prime_nums = []
    for num in numbers:
        if is_prime(num):
            prime_nums.append(num)
    return sorted(prime_nums)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
