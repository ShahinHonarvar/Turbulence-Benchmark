
def all_left_right_truncatable_prime(tuple_of_integers):
    x = tuple_of_integers[10]
    left_and_right_truncatable_prime_numbers = []
    for i in range(2, x + 1):
        if is_left_and_right_truncatable_prime(i):
            left_and_right_truncatable_prime_numbers.append(i)
    return sorted(left_and_right_truncatable_prime_numbers, reverse=True)
def is_left_and_right_truncatable_prime(n):
    if not is_prime(n):
        return False

    string_representation_of_n = str(n)

    number_of_digits = len(string_representation_of_n)

    for i in range(number_of_digits):
        if not is_prime(int(string_representation_of_n[i:])):
            return False

    return True

def is_prime(n):

    if n < 2:

        return False


    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True
