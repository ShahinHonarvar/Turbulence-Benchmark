
def palindromes_between_indices(string):
    import itertools

    letters = [ch for ch in string if ch.isalpha()]
    letters = [ch.lower() for ch in letters]

    palindromes = set()
    for length in range(7, len(letters) + 1):
        for perm in itertools.permutations(letters, length):
            if perm == perm[::-1]:
                palindromes.add(''.join(perm))

    return palindromes
