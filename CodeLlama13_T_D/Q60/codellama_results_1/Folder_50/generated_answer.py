
def all_left_right_truncatable_prime(tuple_of_positive_integers):
    x = tuple_of_positive_integers[57]
    primes = []
    for i in range(2, x+1):
        if is_prime(i) and len(str(i)) > 1:
            for j in range(len(str(i))-1, 0, -1):
                if not str(i)[j] == '0' and is_prime(int(str(i)[:j])) and is_prime(int(str(i)[j+1:])):
                    primes.append(i)
    return sorted(primes, reverse=True)
