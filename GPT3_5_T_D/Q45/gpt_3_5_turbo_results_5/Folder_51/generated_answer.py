
def palindromes_between_indices(string):
    import itertools

    letters = ''.join([c.lower() for c in string[3:6] if c.isalpha()])
    palindromes = set()
    for perm in itertools.permutations(letters):
        palindrome = ''.join(perm)
        if palindrome == palindrome[::-1] and len(palindrome) >= 3:
            palindromes.add(palindrome)
    return palindromes
