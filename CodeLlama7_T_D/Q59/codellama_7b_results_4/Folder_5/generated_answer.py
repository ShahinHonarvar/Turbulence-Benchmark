
def all_left_truncatable_prime(nums):
    x = nums[55]
    prime_list = []
    for i in range(2, x):
        if is_prime(i) and is_left_truncatable_prime(i):
            prime_list.append(i)
    return sorted(prime_list)

def is_prime(n):

    if n < 2:

        return False


    for i in range(2, int(n ** 0.5) + 1):

        if n % i == 0:

            return False


    return True


def is_left_truncatable_prime(n):

    if str(n)[::-1] == str(n):

        return True


    else:


        for i in range(2, len(str(n)) - 1):

            if is_prime(int(str(n)[:i + 1])):

                return True


        return False
