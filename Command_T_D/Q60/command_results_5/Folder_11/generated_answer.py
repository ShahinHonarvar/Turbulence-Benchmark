
import itertools

def all_left_right_truncatable_prime(n):
    if not n: return []
    if len(str(n)) < 3: return []
    lst = list(itertools.permutations(str(n)))
    return sorted([int(f"{i}{int(str(n))}{j}") for i in range(len(str(n)) - 1) for j in range(1, len(str(n)) - 1)])
