
def all_left_truncatable_prime(tuple_of_positive_integers):
    x = tuple_of_positive_integers[86]
    return sorted([int(''.join(str(x)[i:])) for i in range(len(str(x)))], key=lambda n: n) if all(n%2 for n in range(3, int(x**0.5)+1, 2)) else []
