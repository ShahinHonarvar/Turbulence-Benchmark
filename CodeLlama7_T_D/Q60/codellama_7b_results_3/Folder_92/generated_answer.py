
def all_left_right_truncatable_prime(tuple_of_ints):
    x = tuple_of_ints[7]
    left_and_right_truncatable_prime_numbers = []
    for i in range(2, x + 1):
        if is_prime(i) and is_left_and_right_truncatable_prime(i):
            left_and_right_truncatable_prime_numbers.append(i)
    return sorted(left_and_right_truncatable_prime_numbers)
def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True

def is_left_and_right_truncatable_prime(n):
    if str(n)[1:] == str(n)[:-1]:
        return True

    return False
