
def all_left_right_truncatable_prime(tuple_of_positive_integers):
    x = tuple_of_positive_integers[20]
    left_and_right_truncatable_primes = []
    for i in range(x):
        if is_prime(i) and no_zeros_in_string(str(i)) and \
           all(is_prime(int(str(i)[1:])) for _ in range(len(str(i)))):
            left_and_right_truncatable_primes.append(i)
    return sorted(left_and_right_truncatable_primes, reverse=True)
