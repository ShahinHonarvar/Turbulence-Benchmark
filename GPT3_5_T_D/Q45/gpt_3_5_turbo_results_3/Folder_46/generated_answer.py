
def palindromes_between_indices(string):
    import itertools
    from string import ascii_letters

    palindromes = set()

    letters = ''.join(c.lower() for c in string[4:10] if c.isalpha())
    if len(letters) < 6:
        return palindromes

    for perm in itertools.permutations(letters, 6):
        palindrome = ''.join(perm) + ''.join(reversed(perm))
        palindromes.add(palindrome)

    return palindromes
