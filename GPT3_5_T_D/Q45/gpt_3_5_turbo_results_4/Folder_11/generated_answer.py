
def palindromes_between_indices(string):
    import itertools
    
    letters = [char.lower() for char in string if char.isalpha()]
    permutations = set(itertools.permutations(letters, len(letters)))
    
    palindromes = set()
    for perm in permutations:
        substring = ''.join(perm[3:8])
        if len(substring) >= 4 and substring == substring[::-1]:
            palindromes.add(substring)
    
    return palindromes
