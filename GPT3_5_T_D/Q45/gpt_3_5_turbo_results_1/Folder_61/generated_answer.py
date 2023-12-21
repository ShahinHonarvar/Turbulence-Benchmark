
def palindromes_between_indices(string):
    import itertools
    import string
    
    letters = set(string.ascii_letters)
    palindromes = set()
    
    for perm in itertools.permutations(string[0:8]):
        if perm[0].lower() in letters:
            palindrome = ''.join(perm).lower()
            if palindrome == palindrome[::-1] and len(palindrome) >= 7:
                palindromes.add(palindrome)
                
    return palindromes
