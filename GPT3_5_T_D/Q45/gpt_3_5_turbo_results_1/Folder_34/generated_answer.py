
def palindromes_between_indices(string):
    from itertools import permutations
    from string import ascii_letters
    
    substr = string[5:8].lower()
    palindromes = set()
    
    for perm in permutations(substr):
        word = ''.join(perm)
        if word == word[::-1] and len(word) >= 4:
            palindromes.add(word)
    
    return palindromes
