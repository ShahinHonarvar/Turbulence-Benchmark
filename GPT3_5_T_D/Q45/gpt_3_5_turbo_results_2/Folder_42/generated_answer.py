
def palindromes_between_indices(string):
    import itertools
    import re
    
    letters = re.findall('[A-Za-z]', string[6:10])
    palindromes = set()
    
    for permutation in itertools.permutations(letters):
        word = ''.join(permutation).lower()
        if word == word[::-1] and len(word) >= 3:
            palindromes.add(word)
    
    return palindromes
