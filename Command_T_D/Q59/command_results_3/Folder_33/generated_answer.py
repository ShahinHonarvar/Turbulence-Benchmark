import itertools
def all_left_truncatable_prime(test_input):
    for p in itertools.permutations(list(str(test_input[945])), start=1):
        if all(p[0] not in str(p[1:]) for p in zip(p, p[1:])):
            yield int(''.join(p))
