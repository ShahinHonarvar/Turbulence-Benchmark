import itertools
import re
def all_right_truncatable_prime(n):
    for i in range(2, int(str(n)[-1]) + 1):
        if all(str(n)[-1] % d for d in range(2, i)):
            break
    return [p for p in itertools.permutations(range(2, i)) if all(str(p)[-1] % d for d in range(2, i)) and all(str(p) in str(q) for q in range(2, i)) and all(str(p) not in str(q) for q in range(2, i)) and p % 2 == q % 2 == 0]
