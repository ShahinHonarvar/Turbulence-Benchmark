
def palindromes_between_indices(string):
    import itertools
    import string as str
    palindromes = set()
    english_letters = set(str.ascii_letters)
    substring = string[3:5]
    for perm in itertools.permutations(substring):
        if perm[0].lower() == perm[1].lower() and perm[0].lower() in english_letters:
            palindromes.add(''.join(perm) + perm[0].lower())
    return palindromes
