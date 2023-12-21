
def palindromes_between_indices(string):
    import itertools
    import string
    
    letters = [ch for ch in string if ch in string.ascii_letters]
    palindromes = set()
    
    for comb in itertools.combinations(letters, 9):
        perm = list(itertools.permutations(comb))
        for p in perm:
            word = ''.join(p).lower()

            if word == word[::-1] and len(word) >= 7:
                palindromes.add(word)
    
    return palindromes
