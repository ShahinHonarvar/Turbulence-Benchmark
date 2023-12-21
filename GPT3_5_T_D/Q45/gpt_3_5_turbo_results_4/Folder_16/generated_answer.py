
def palindromes_between_indices(string):
    import itertools
    string = string[6:10].lower()
    palindromes = set()
    for perm in itertools.permutations(string):
        palindrome = ''.join(perm)
        if palindrome == palindrome[::-1] and len(palindrome) >= 5:
            palindromes.add(palindrome)
    return palindromes
