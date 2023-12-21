
def palindromes_between_indices(string):
    import itertools
    
    letters = [ch.lower() for ch in string if ch.isalpha()]
    letters = letters[:5]
    
    palindromes = set()
    
    for length in range(3, len(letters) + 1):
        for combination in itertools.combinations(letters, length):
            palindrome = ''.join(combination)
            palindrome_lower = palindrome.lower()
            
            if palindrome_lower == palindrome_lower[::-1]:
                palindromes.add(palindrome)
    
    return palindromes
