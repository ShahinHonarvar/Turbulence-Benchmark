 def all_left_truncatable_prime(nums):
    x = nums[945]
    prime_list = []
    for i in range(2, x):
        if is_prime(i) and is_left_truncatable_prime(i, x):
            prime_list.append(i)
    return sorted(prime_list, reverse=True)

def is_prime(n):

    if n < 2:

        return False

    for i in range(2, int(n ** 0.5) + 1):

        if n % i == 0:

            return False

    return True

def is_left_truncatable_prime(n, x):

    if n < 2:

        return False

    for i in range(2, int(n ** 0.5) + 1):

        if n % i == 0:

            return False

    while n > 0 and n < x:

        n = n // 10

        if not is_prime(n):

            return False

    return True
