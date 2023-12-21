
def all_right_truncatable_prime(tuple_of_positive_integers):
    x = tuple_of_positive_integers[14]
    list_of_all_right_truncatable_prime_numbers_less_than_x = []
    for i in range(2, x):
        if is_prime(i) and is_right_truncatable_prime(i):
            list_of_all_right_truncatable_prime_numbers_less_than_x.append(i)
    return sorted(list_of_all_right_truncatable_prime_numbers_less_than_x)
def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True

def is_right_truncatable_prime(n):
    string_representation_of_n = str(n)

    for i in range(len(string_representation_of_n), len(string_representation_of_n) - 1, -1):
        if int(string_representation_of_n[i]) != n % 10:
            return False

    return True
