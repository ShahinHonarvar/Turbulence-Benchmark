
def palindromes_between_indices(s):
    import itertools
    import string
    palindromes = set()
    letters = [c.lower() for c in s[:5] if c.isalpha()]
    for perm in itertools.permutations(letters, len(letters)):
        palindrome = ''.join(perm)
        if palindrome == palindrome[::-1] and len(palindrome) >= 3:
            palindromes.add(palindrome)
    return palindromes
