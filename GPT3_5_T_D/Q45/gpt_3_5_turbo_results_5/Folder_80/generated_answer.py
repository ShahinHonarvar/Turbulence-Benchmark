
def palindromes_between_indices(string):
    from itertools import permutations
    
    letters = [c.lower() for c in string[3:9] if c.isalpha()]
    palindromes = set()
    
    for perm in permutations(letters, len(letters)):
        word = ''.join(perm)
        if word == word[::-1] and len(word) >= 7:
            palindromes.add(word)
    
    return palindromes
