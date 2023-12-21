
def palindromes_between_indices(string):
    import itertools
    string = string[1:7].lower()
    palindromes = set()
    for letters in itertools.permutations(string, len(string)):
        palindrome = ''.join(letters + letters[::-1])
        if palindrome == palindrome[::-1] and len(palindrome) >= 7:
            palindromes.add(palindrome)
    return palindromes
