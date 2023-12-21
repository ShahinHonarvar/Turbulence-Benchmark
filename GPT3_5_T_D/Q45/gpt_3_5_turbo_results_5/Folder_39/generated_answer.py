
def palindromes_between_indices(string):
    import itertools
    
    letters = [c.lower() for c in string[2:6] if c.isalpha()]
    
    if len(letters) < 3:
        return set()
    
    palindromes = set()
    
    for perm in itertools.permutations(letters):
        palindrome = ''.join(perm)
        
        if palindrome.lower() == palindrome.lower()[::-1]:
            palindromes.add(palindrome)
    
    return palindromes
