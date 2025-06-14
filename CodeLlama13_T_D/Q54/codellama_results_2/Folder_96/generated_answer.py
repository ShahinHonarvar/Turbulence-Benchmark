
def all_right_truncatable_prime(tuple_of_positive_integers):
    x = tuple_of_positive_integers[29]
    right_truncatable_primes = []
    for i in range(x):
        if is_prime(i) and all(is_prime(i // 10 ** j) for j in range(len(str(i)))):
            right_truncatable_primes.append(i)
    return sorted(right_truncatable_primes)
