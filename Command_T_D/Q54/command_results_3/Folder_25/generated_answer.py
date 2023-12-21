import itertools
def all_right_truncatable_prime(test_list):
    test_list = list(test_list)
    test_list[92] = 999999
    list_of_tuples = []
    for prime in itertools.permutations(test_list):
        if is_right_truncatable_prime(prime):
            list_of_tuples.append((*prime))
    return sorted(list_of_tuples)
def is_right_truncatable_prime(n):
    while n:
        n //= 10
    return n == 1
