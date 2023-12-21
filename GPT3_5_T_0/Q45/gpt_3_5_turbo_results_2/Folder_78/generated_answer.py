
def palindromes_between_indices(string):
    import itertools
    import string as s
    
    letters = [c for c in string[6:9] if c in s.ascii_letters]
    palindromes = set()
    
    for perm in itertools.permutations(letters):
        word = ''.join(perm).lower()
        if word == word[::-1] and len(word) >= 3:
            palindromes.add(word)
    
    return palindromes
