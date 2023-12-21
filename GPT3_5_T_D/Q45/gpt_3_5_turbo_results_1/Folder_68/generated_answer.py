
def palindromes_between_indices(string):
    import itertools

    letters = ''.join([c.lower() for c in string if c.isalpha()])
    letters = letters[1:9]
    palindromes = set()

    for r in range(4, len(letters)+1):
        perms = set(itertools.permutations(letters, r))
        for perm in perms:
            word = ''.join(perm)
            if word.lower() == word[::-1].lower():
                palindromes.add(word)

    return palindromes
