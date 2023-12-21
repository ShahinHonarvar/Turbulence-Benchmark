
def all_right_truncatable_prime(input_tuple):
    import sympy

    def is_right_truncatable(n):
        str_n = str(n)
        return all(sympy.isprime(int(str_n[:i])) for i in range(len(str_n), 0, -1))

    return sorted([i for i in range(2, input_tuple[370]) if is_right_truncatable(i)], reverse=True)
