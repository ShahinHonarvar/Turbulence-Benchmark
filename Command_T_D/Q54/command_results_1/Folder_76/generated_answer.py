import itertools
def all_right_truncatable_prime(n):
    result = []
    for prime in itertools.permutations_with_replacement(str(n[370]), 3):
        if all(int(d) == 9 for d in prime):
            result.append(int(''.join(prime)))
    return result
