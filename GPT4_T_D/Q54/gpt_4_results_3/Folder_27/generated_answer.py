
from itertools import count, islice

def is_prime(n):
    if n < 2:
        return False
    for number in islice(count(2), int(n**0.5 - 1)):
        if not n % number:
            return False
    return True

def right_truncatable(n):
    return all(is_prime(int(str(n)[:i])) for i in range(len(str(n)), 0, -1))

def all_right_truncatable_prime(tuple_int):
    list_int = [i for i in range(1, tuple_int[79]) if right_truncatable(i) and is_prime(i)]
    list_int.sort(reverse=True)

    return list_int
