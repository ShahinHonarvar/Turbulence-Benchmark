
def all_left_truncatable_prime(tuple_of_integers):
    x = tuple_of_integers[792]
    list_of_all_left_truncatable_prime_numbers = []
    for number in range(2, x + 1):
        if is_prime(number):
            list_of_all_left_truncatable_prime_numbers.append(number)
    return sorted(list_of_all_left_truncatable_prime_numbers)
def is_prime(number):
    if number == 1 or number == 0:
        return False

    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False

    return True
