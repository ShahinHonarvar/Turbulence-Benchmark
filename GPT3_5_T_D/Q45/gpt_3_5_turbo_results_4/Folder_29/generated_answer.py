
def palindromes_between_indices(string):
    import itertools
    
    english_letters = [letter.lower() for letter in string if letter.isalpha()]
    english_count = len(english_letters)
    
    if english_count < 10:
        return set()
    
    palindromes = set()
    
    for combination in itertools.permutations(english_letters[2:10], 8):
        palindrome = ''.join(combination)
        if palindrome.lower() == palindrome[::-1].lower() and len(palindrome) >= 6:
            palindromes.add(palindrome)
    
    return palindromes
