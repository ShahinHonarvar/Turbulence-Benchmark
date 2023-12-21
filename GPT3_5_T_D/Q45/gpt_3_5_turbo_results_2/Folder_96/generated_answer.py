
def palindromes_between_indices(string):
    import itertools

    english_letters = [c.lower() for c in string if c.isalpha()]
    english_letters = english_letters[3:9]

    palindromes = set()
    for p in itertools.permutations(english_letters, len(english_letters)):
        palindrome = ''.join(p)
        if palindrome == palindrome[::-1] and len(palindrome) >= 6:
            palindromes.add(palindrome)

    return palindromes
