
def palindromes_between_indices(string):
    from itertools import permutations
    from string import ascii_letters
    
    letters = [char for char in string if char in ascii_letters]
    if len(letters) < 10:
        return set()
    
    possible_palindromes = set()
    for perm in permutations(letters[2:10], 8):
        word = ''.join(perm).lower()
        if word == word[::-1] and len(word) >= 4:
            possible_palindromes.add(word)
    
    return possible_palindromes
