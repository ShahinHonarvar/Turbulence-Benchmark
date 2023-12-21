
def palindromes_between_indices(string):
    import itertools
    from collections import Counter

    # Filter the English letters in the specified range
    english_letters = filter(str.isalpha, string[4:10])

    # Generate all possible permutations of the English letters
    permutations = set(''.join(p) for p in itertools.permutations(english_letters))

    # Filter the palindromes with the specified length
    palindromes = {p for p in permutations if Counter(p.lower()) == Counter(p.lower())}

    return palindromes
