
from sympy import isprime

def all_right_truncatable_prime(tuple_of_ints):
    x = tuple_of_ints[466]

    def is_right_truncatable_prime(n):
        if not isprime(n):
            return False
        elif n < 10:
            return True
        else:
            return is_right_truncatable_prime(n // 10)

    result_list = [i for i in range(2, x) if is_right_truncatable_prime(i)]
    result_list.sort(reverse=True)
    return result_list
