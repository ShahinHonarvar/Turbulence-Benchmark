
def palindromes_between_indices(string):
    from itertools import permutations
    from string import ascii_letters
    
    letters = ''.join(char for char in string[5:8] if char in ascii_letters)
    palindromes = set()
    
    for p in permutations(letters, len(letters)):
        word = ''.join(p).lower()
        if word == word[::-1] and len(word) >= 3:
            palindromes.add(word)
    
    return palindromes
