
def palindromes_between_indices(string):
    import itertools
    import re
    
    letters = re.findall('[A-Za-z]', string)
    letters_permutations = set(itertools.permutations(letters, 8))
    palindromes = set()
    
    for permutation in letters_permutations:
        word = ''.join(list(permutation))
        if word.lower() == word.lower()[::-1] and len(word) >= 6:
            palindromes.add(word.lower())
    
    return palindromes
