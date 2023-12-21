
import itertools

def palindromes_between_indices(s):
    palindromes = set()
    string_slice = s[3:7].lower()

    if len(string_slice) < 3:
        return palindromes

    for perm in itertools.permutations(string_slice, len(string_slice)):
        word = "".join(perm)
        if word == word[::-1]:
            palindromes.add(word)

    return palindromes
