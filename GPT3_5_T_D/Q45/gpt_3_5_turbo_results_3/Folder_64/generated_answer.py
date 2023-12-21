
def palindromes_between_indices(string):
    import itertools
    import string
    palindromes = set()
    letters = ''.join(filter(str.isalpha, string[4:10]))
    for combination in itertools.permutations(letters.upper(), len(letters)):
        candidate = ''.join(combination)
        if candidate == candidate[::-1] and len(candidate) >= 5:
            palindromes.add(candidate.lower())
    return palindromes
