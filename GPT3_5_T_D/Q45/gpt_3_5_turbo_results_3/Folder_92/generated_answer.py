
def palindromes_between_indices(string):
    import itertools
    import string as s

    # Get all substrings of length 4 to 7
    substrings = set(string[4:8])

    for length in range(4, 8):
        substrings.union(set(''.join(subset)) for subset in itertools.permutations(string[4:8], length))

    # Filter out non-palindromes
    palindromes = {word for word in substrings if word.lower() == word.lower()[::-1]}

    return palindromes
