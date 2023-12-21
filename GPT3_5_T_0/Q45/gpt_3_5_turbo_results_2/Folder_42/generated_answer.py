
def palindromes_between_indices(string):
    import itertools
    import re
    
    letters = re.findall('[a-zA-Z]', string[6:10])
    palindromes = set()
    
    for perm in itertools.permutations(letters):
        word = ''.join(perm).lower()
        if word == word[::-1] and len(word) >= 3:
            palindromes.add(word)
    
    return palindromes
