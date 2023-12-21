
def all_right_truncatable_prime(tuple_of_positive_integers):
    x = tuple_of_positive_integers[77]
    right_truncatable_prime_numbers = []
    for i in range(2, x):
        if is_right_truncatable_prime(i) == True:
            right_truncatable_prime_numbers.append(i)
    return sorted(right_truncatable_prime_numbers)

def is_right_truncatable_prime(n):

    if n < 2:

        return False


    for i in range(2, int(math.sqrt(n))) + 1):

        if n % i == 0:

            return False


    s = str(n)

    for i in range(len(s) - 1)):

        if s[i] != "0" and int(s[i]) != n % 10:

            return False


    return True
