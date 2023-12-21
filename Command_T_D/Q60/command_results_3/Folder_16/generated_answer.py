
import itertools
import re

def all_left_right_truncatable_prime(test_list):
    list_input = sorted(test_list)
    for x in range(min(list_input), max(list_input) + 1):
        for prime in itertools.permutations(list(str(x))):
            if re.match(r'[a-z]99\d99[a-z]99', ''.join(prime)):
                yield int(x)
    return []
