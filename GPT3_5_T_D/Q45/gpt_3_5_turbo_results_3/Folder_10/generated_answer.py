
def palindromes_between_indices(string):
    import itertools
    
    letters = [ch.lower() for ch in string[:6] if ch.isalpha()]
    if len(letters) < 3:
        return set()
    
    palindromes = set()
    for subset in itertools.permutations(letters, len(letters)):
        word = ''.join(subset)
        if word == word[::-1]:
            palindromes.add(word)
    
    return palindromes
