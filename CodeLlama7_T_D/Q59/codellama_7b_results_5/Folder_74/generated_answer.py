
def all_left_truncatable_prime(tuple):
    x = tuple[36]
    list = []
    for i in range(2, x):
        if is_prime(i) and is_left_truncatable_prime(i):
            list.append(i)
    return sorted(list)

def is_prime(n):

    if n == 1 or n == 0:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


def is_left_truncatable_prime(n):

    if not is_prime(n):

        return False


    digits = [int(digit) for digit in str(n)]

    for i in range(len(digits)):

        number = int("".join(map(str, digits[i:]))))

        if not is_prime(number):

            return False


    return True
