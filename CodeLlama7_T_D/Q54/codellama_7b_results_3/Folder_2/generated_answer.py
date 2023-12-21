
def all_right_truncatable_prime(num):
    prime_list = []
    for i in range(1, num + 1):
        if is_prime(i) and is_right_truncatable_prime(i):
            prime_list.append(i)
    return sorted(prime_list)

def is_prime(num):

    if num < 2:

        return False

    for i in range(2, int(num ** 0.5) + 1):

        if num % i == 0:

            return False

    return True


def is_right_truncatable_prime(num):

    num_str = str(num)

    for i in range(len(num_str)):

        if not is_prime(int(num_str[:-i])):

            return False

    return True
