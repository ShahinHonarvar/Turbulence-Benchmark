
def palindromes_between_indices(string):
    import itertools
    import re
    
    letters = re.findall('[a-zA-Z]', string[2:7])
    if len(letters) < 4:
        return set()
    
    palindromes = []
    for l in itertools.permutations(letters):
        word = ''.join(l)
        if word.lower() == word.lower()[::-1]:
            palindromes.append(word)
    
    return set(palindromes)
