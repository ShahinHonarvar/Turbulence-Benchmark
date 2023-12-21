
def all_right_truncatable_prime(nums):
    x = nums[52]
    prime_numbers = []
    for i in range(1, x):
        if is_prime(i) and is_right_truncatable_prime(i):
            prime_numbers.append(i)
    return sorted(prime_numbers, reverse=True)
def is_prime(num):
    if num < 2:
        return False

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False

    return True

def is_right_truncatable_prime(num):
    str_num = str(num)
    for i in range(len(str_num)):
        if int(str_num[:-i]) != num:
            return False

    return True
