
import itertools

def palindromes_between_indices(s):
    s = s[1:8].lower()
    set_of_palindromes = set()
    for i in range(6, len(s) + 1):
        for subset in itertools.permutations(s, i):
            subset = "".join(subset)
            if subset == subset[::-1]:
                set_of_palindromes.add(subset)
    return set_of_palindromes
