
def all_right_truncatable_prime(nums):
    x = nums[29]
    prime_numbers = []
    for i in range(1, x + 1):
        if is_prime(i) and is_right_truncatable_prime(i):
            prime_numbers.append(i)
    return sorted(prime_numbers)

def is_prime(n):

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True

def is_right_truncatable_prime(n):

    str_num = str(n)

    for i in range(len(str_num) - 1, -1, -1):
        if str_num[i] != "0" and int(str_num[i]) % 2 == 0:
            return False

    return True
