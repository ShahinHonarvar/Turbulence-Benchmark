
def palindromes_between_indices(string):
    import itertools
    
    letters = []
    for c in string[1:9].lower():
        if c.isalpha():
            letters.append(c)
    
    permutations = set(itertools.permutations(letters))
    
    palindromes = set()
    for p in permutations:
        word = "".join(p)
        if word == word[::-1] and len(word) >= 7:
            palindromes.add(word)
    
    return palindromes
