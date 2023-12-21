
import itertools

def palindromes_between_indices(s):
    s_substring = s[0:8].lower()
    s_set = set(s_substring)
    palindromes_set = set()

    for i in range(7, len(s_substring) + 1):
        combinations = list(itertools.combinations(s_set, i))
        for combination in combinations:
            permuts = list(itertools.permutations(combination, i))
            for perm in permuts:
                perm = "".join(perm)
                if perm == perm[::-1]:
                    palindromes_set.add(perm)

    return palindromes_set
