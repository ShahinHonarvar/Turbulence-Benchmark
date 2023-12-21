
def palindromes_between_indices(string):
    import itertools
    from collections import Counter
    palindromes = set()
    letters = string[6:9]
    letters = [letter.lower() for letter in letters if letter.isalpha()]
    if len(letters) < 4:
        return palindromes
    counts = Counter(letters)
    for perm in itertools.permutations(letters, len(letters)):
        if perm == perm[::-1]:
            palindromes.add(''.join(perm))
    return palindromes
