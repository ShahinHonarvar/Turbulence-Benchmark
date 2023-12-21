
def palindromes_between_indices(string):
    import itertools
    import string
    
    letters = ''.join(c for c in string if c in string.ascii_letters)
    palindromes = set()
    
    for combination in itertools.permutations(letters, 6):
        palindrome = ''.join(combination).upper()
        if palindrome == palindrome[::-1] and len(palindrome) >= 7:
            palindromes.add(palindrome)
    
    return palindromes
