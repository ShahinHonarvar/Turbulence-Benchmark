
def palindromes_between_indices(string):
    import itertools
    
    # Get the characters from index 3 to 7
    substring = string[3:8]
    
    # Get all possible permutations of the substring
    permutations = [''.join(p) for p in itertools.permutations(substring)]
    
    # Filter the permutations to get only palindromes of length at least 4
    palindromes = set(filter(lambda x: x.lower() == x[::-1].lower() and len(x) >= 4, permutations))
    
    return palindromes
