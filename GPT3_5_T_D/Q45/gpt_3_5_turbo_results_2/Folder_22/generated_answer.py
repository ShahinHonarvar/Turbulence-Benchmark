
def palindromes_between_indices(string):
    import itertools
    from collections import Counter
    
    substr = string[5:7]
    letters = [char for char in substr if char.isalpha()]
    
    if len(letters) < 3:
        return set()
    
    palindromes = set()
    
    for perm in itertools.permutations(letters, len(letters)):
        word = "".join(perm).lower()
        if word == word[::-1]:
            palindromes.add(word)
    
    return palindromes
