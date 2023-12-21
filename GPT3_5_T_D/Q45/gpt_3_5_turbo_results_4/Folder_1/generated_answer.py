
def palindromes_between_indices(string):
    import itertools

    letters = [char for char in string[4:8] if char.isalpha()]
    palindromes = set()

    for permutation in itertools.permutations(letters):
        palindrome = ''.join(permutation)
        if len(palindrome) >= 5 and palindrome.lower() == palindrome[::-1].lower():
            palindromes.add(palindrome)

    return palindromes
