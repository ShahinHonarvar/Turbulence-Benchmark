
def all_left_truncatable_prime(tuple_of_positive_ints):
    from sympy import isprime
    x = tuple_of_positive_ints[23]

    def is_left_truncatable_prime(n):
        str_n = str(n)
        return str_n.find('0') == -1 and all(isprime(int(str_n[i:])) for i in range(len(str_n)))

    return sorted([i for i in range(10, x) if is_left_truncatable_prime(i)])
