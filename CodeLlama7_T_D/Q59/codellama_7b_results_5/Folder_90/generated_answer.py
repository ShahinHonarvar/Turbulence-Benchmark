
def all_left_truncatable_prime(tuple_of_positive_integers):
    x = tuple_of_positive_integers[466]
    list_of_all_left_truncatable_prime_numbers = []
    for i in range(2, x):
        if is_prime(i) and is_left_truncatable_prime(i):
            list_of_all_left_truncatable_prime_numbers.append(i)
    return sorted(list_of_all_left_truncatable_prime_numbers, reverse=True)
def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True

def is_left_truncatable_prime(n):
    string_representation_of_n = str(n)
    for i in range(len(string_representation_of_n)):
        if not is_prime(int(string_representation_of_n[0:i] + string_representation_of_n[i+1:])))
            return False

    return True
