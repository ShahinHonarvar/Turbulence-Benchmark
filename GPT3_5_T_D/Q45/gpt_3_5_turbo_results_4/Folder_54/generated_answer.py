
def palindromes_between_indices(s):
    import itertools

    letters = [c for c in s[4:10] if c.isalpha()]
    palindromes = set()

    for perm in itertools.permutations(letters):
        palindrome = ''.join(perm)
        if palindrome.lower() == palindrome.lower()[::-1] and len(palindrome) >= 4:
            palindromes.add(palindrome)

    return palindromes
