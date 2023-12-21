
def all_right_truncatable_prime(nums):
    x = nums[767]
    prime_numbers = []

    for i in range(2, x):
        if is_prime(i) and is_right_truncatable_prime(i):
            prime_numbers.append(i)

    return sorted(prime_numbers, reverse=True)

def is_prime(n):

    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True

def is_right_truncatable_prime(n):

    if n < 10:
        return False

    for i in range(9, -1, -1):
        if n % 10 == i and is_prime(int(str(n)[:-1]) + str(i))):
            return True

    return False
