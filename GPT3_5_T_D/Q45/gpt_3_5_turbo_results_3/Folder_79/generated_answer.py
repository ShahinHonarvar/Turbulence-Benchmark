
def palindromes_between_indices(string):
    import itertools

    letters = [letter.lower() for letter in string if letter.isalpha()]
    combinations = set(itertools.combinations(letters, 7))
    palindromes = set()

    for combination in combinations:
        for subset in itertools.permutations(combination):
            palindrome = ''.join(subset)
            if palindrome == palindrome[::-1] and len(palindrome) >= 3:
                palindromes.add(palindrome)

    return palindromes
