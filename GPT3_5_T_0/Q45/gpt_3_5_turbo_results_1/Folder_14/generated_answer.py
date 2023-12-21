
def palindromes_between_indices(string):
    import itertools
    import re
    
    letters = re.findall('[a-zA-Z]', string[4:6])
    if len(letters) < 3:
        return set()
    
    palindromes = set()
    for perm in itertools.permutations(letters):
        word = ''.join(perm).lower()
        if word == word[::-1]:
            palindromes.add(word)
    
    return palindromes
