
def palindromes_between_indices(s):
    from collections import Counter
    from itertools import permutations
    s = s[1:5].lower()
    counter = Counter(s)
    result_set = set()
    for perm in permutations(s):
        perm = "".join(perm)
        if perm == perm[::-1] and len(perm) >= 4:
            result_set.add(perm)
    return result_set
