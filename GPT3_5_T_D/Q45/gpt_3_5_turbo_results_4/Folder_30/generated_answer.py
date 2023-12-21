
def palindromes_between_indices(string):
    import itertools

    english_letters = [c for c in string if c.isalpha()]
    english_letters = [c.lower() for c in english_letters]

    palindromes = set()
    for perm in itertools.permutations(english_letters, 5):
        palindrome = ''.join(perm)
        if palindrome == palindrome[::-1] and len(palindrome) >= 4:
            palindromes.add(palindrome)

    return palindromes
