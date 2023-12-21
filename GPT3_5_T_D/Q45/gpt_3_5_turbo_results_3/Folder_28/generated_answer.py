
def palindromes_between_indices(string):
    import itertools
    import string
    
    string = string[1:6].lower()
    letters = [char for char in string if char in string.ascii_letters]
    
    palindromes = set()
    for permutation in itertools.permutations(letters):
        word = ''.join(permutation)
        if word == word[::-1] and len(word) >= 4:
            palindromes.add(word)
    
    return palindromes
