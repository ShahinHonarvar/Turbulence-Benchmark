
def palindromes_between_indices(string):
    import itertools
    import string
    
    substr = string[2:4].lower()
    letters = [char.lower() for char in string if char in string.ascii_letters] 
    
    palindromes = set()
    for perm in itertools.permutations(letters, len(substr)):
        word = ''.join(perm)
        if word == word[::-1] and len(word) >= 3:
            palindromes.add(word)
    
    return palindromes
