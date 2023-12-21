
def palindromes_between_indices(string):
    import itertools
    from string import ascii_letters
    
    chars = [char.lower() for char in string[3:6] if char.isalpha()]
    perms = list(itertools.permutations(chars))

    palindromes = set()
    for perm in perms:
        word = ''.join(perm)
        if word == word[::-1] and len(word) >= 4:
            palindromes.add(word)
    
    return palindromes
