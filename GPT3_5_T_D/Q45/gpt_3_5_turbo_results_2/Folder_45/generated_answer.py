
def palindromes_between_indices(string):
    import itertools
    import re
    
    letters = re.findall('[a-zA-Z]', string[5:10])
    palindromes = set()
    
    for perm in itertools.permutations(letters):
        word = ''.join(perm)
        if word.lower() == word.lower()[::-1] and len(word) >= 4:
            palindromes.add(word.lower())
    
    return palindromes
