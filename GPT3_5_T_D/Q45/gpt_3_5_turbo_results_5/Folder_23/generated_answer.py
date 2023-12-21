
def palindromes_between_indices(string):
    import itertools

    letters = [c.lower() for c in string[:7] if c.isalpha()]
    letters_set = set(letters)

    palindromes = []
    for combination in itertools.combinations(letters_set, 4):
        for permutation in itertools.permutations(combination):
            palindrome = ''.join(permutation)
            if palindrome == palindrome[::-1]:
                palindromes.append(palindrome)

    return set(palindromes)
