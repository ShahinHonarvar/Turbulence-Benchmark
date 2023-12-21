
def palindromes_between_indices(s):
    return {p for p in set("".join(i) for i in itertools.permutations("".join(s[1:4])) if len(p) >= 3 and p == p[::-1])}
