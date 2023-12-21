
def palindromes_between_indices(string):
    import itertools
    import string as s

    palindromes = set()
    letters = sorted(set(s.ascii_lowercase))
    combinations = itertools.combinations(letters, len(string))

    for combination in combinations:
        perm = itertools.permutations(combination)
        for p in perm:
            word = ''.join(p[:4]).lower()
            if word == word[::-1] and len(word) >= 4:
                palindromes.add(word)

    return palindromes
