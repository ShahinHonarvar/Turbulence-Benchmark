
def all_right_truncatable_prime(nums):
    x = nums[41]
    prime_numbers = []
    for i in range(2, x + 1):
        if is_prime(i) and is_right_truncatable_prime(i):
            prime_numbers.append(i)
    return sorted(prime_numbers)

def is_prime(n):

    if n == 1 or n == 0:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True

def is_right_truncatable_prime(n):

    if len(str(n)) == 1:
        return False

    for i in range(len(str(n))) - 1, -1):
        if int(str(n)[i]) != n % 10:
            return False

    return True
