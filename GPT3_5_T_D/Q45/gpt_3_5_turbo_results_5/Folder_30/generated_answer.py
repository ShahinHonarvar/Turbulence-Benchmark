
def palindromes_between_indices(string):
    from itertools import permutations
    from string import ascii_letters
    
    english_letters = set(ascii_letters)
    english_letters_string = ''.join(english_letters)
    
    valid_palindromes = set()
    
    for permutation in permutations(english_letters_string, 5):
        substring = ''.join(permutation).lower()
        if substring == substring[::-1]:
            valid_palindromes.add(substring)
    
    return valid_palindromes
