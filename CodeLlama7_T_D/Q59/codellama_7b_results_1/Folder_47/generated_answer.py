
def all_left_truncatable_prime(tuple_of_ints):
    x = tuple_of_ints[49]
    prime_numbers = []
    for i in range(2, x + 1):
        if is_prime(i) and is_left_truncatable_prime(i):
            prime_numbers.append(i)
    return sorted(prime_numbers)

def is_prime(n):
    if n == 1 or n == 0:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True

def is_left_truncatable_prime(n):
    if n == 1 or n == 0:
        return False

    str_n = str(n)

    for i in range(len(str_n)):
        if str_n[:i] == "":
            continue

        if is_prime(int(str_n[:i])):
            continue

        return False


    return True
