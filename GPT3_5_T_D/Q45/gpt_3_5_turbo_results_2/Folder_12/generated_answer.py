
def palindromes_between_indices(string):
    import itertools
    
    substring = string[3:9].lower()
    palindromes = set()
    
    for permutation in itertools.permutations(substring, len(substring)):
        candidate = ''.join(permutation)
        if candidate == candidate[::-1] and len(candidate) >= 4:
            palindromes.add(candidate)
    
    return palindromes
