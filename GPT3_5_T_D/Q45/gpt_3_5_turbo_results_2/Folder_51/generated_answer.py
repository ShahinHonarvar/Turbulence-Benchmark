
def palindromes_between_indices(string):
    import itertools
    from itertools import permutations
    
    letters = [letter for letter in string[3:6] if letter.isalpha()]
    permutations = set(itertools.permutations(letters, len(letters)))
    palindromes = set()
    
    for perm in permutations:
        word = ''.join(perm)
        if word.lower() == word.lower()[::-1] and len(word) >= 3:
            palindromes.add(word.lower())
            
    return palindromes
