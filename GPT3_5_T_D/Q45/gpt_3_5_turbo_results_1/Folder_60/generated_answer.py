
def palindromes_between_indices(string):
    import itertools
    import re
    
    chars = re.findall('[a-zA-Z]', string[3:7])
    palindromes = set()
    
    for perm in itertools.permutations(chars):
        pal = ''.join(perm).lower()
        if pal == pal[::-1] and len(pal) >= 4:
            palindromes.add(pal)
    
    return palindromes
