
def palindromes_between_indices(string):
    import itertools
    import re
    
    letters = re.findall('(?i)[a-z]', string[6:10])
    palindromes = set()
    
    for permutation in itertools.permutations(letters):
        word = ''.join(permutation)
        if word == word[::-1] and len(word) >= 4:
            palindromes.add(word.lower())
    
    return palindromes
