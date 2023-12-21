
def palindromes_between_indices(string):
    import itertools
    
    english_letters = [c for c in string if c.isalpha()]
    english_letters = ''.join(english_letters)
    
    if len(english_letters) < 6:
        return set()
    
    palindromes = set()
    for combination in itertools.permutations(english_letters[3:9], 6):
        palindrome = ''.join(combination)
        if palindrome.lower() == palindrome.lower()[::-1]:
            palindromes.add(palindrome)
    
    return palindromes
