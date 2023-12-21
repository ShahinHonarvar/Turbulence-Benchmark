
def palindromes_between_indices(string):
    import itertools
    from string import ascii_letters

    letters = set(ascii_letters)
    indices = range(3, 9)
    
    possible_letters = [c.lower() for c in string if c.lower() in letters]
    permutations = set(itertools.permutations(possible_letters, indices[-1] - indices[0] + 1))
    
    palindromes = set()
    
    for p in permutations:
        if p == p[::-1]:
            palindromes.add(''.join(p))
    
    return palindromes
