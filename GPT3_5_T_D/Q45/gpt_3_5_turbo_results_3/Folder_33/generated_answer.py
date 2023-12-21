
def palindromes_between_indices(string):
    import itertools

    letters = [x.lower() for x in string[7:10] if x.isalpha()]
    permutations = set(''.join(p) for p in itertools.permutations(letters))

    palindromes = set()
    for permutation in permutations:
        if permutation == permutation[::-1]:
            palindromes.add(permutation)

    return palindromes
