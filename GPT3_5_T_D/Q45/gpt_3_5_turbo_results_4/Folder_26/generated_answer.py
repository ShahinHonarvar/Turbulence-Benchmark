
def palindromes_between_indices(string):
    letters = [c.lower() for c in string[4:7] if c.isalpha()]
    palindromes = set()
    
    def is_palindrome(word):
        return word.lower() == word.lower()[::-1]
    
    if len(letters) >= 3:
        from itertools import permutations
        
        for perm in permutations(letters):
            word = ''.join(perm)
            if is_palindrome(word):
                palindromes.add(word)
    
    return palindromes
