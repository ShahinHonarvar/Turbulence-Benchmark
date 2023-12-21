
import itertools

def palindromes_between_indices(string):
    
    def is_palindrome(word):
        return word.lower() == word.lower()[::-1]
    
    letters = [c for c in string[2:6] if c.isalpha()]
    palindromes = set()
    
    for length in range(3, len(letters) + 1):
        for combination in itertools.permutations(letters, length):
            word = ''.join(combination)
            if is_palindrome(word):
                palindromes.add(word)
    
    return palindromes
