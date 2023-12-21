
def palindromes_between_indices(string):
    import itertools
    from collections import Counter

    # filter only English letters in the specified range
    letters = [c.lower() for c in string[4:8] if c.isalpha()]

    # count occurrences of each letter
    letter_counts = Counter(letters)

    # generate all possible permutations of the letters
    permutations = set(itertools.permutations(letters))

    # iterate over permutations and check for palindromes
    palindromes = set()
    for permutation in permutations:
        if permutation == permutation[::-1]:
            palindrome = ''.join(permutation)
            palindromes.add(palindrome)

    # filter palindromes with length at least 4
    palindromes = {p for p in palindromes if len(p) >= 4}

    return palindromes
