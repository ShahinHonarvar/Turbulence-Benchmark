
def palindromes_between_indices(string):
    import itertools
    import string
    
    string = string[0:6]
    letters = [char for char in string.lower() if char in string.ascii_lowercase]
    palindromes = set()
    
    for comb in itertools.permutations(letters, 5):
        word = ''.join(comb)
        if word == word[::-1]:
            palindromes.add(word)
    
    return palindromes
