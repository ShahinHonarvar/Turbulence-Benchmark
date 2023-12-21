
def palindromes_between_indices(string):
    import itertools
    
    letters = [ch for ch in string[6:10] if ch.isalpha()]
    if len(letters) < 3:
        return set()
    
    palindromes = set()
    for permutation in itertools.permutations(letters):
        word = ''.join(permutation).lower()
        if word == word[::-1]:
            palindromes.add(word)
    
    return palindromes
