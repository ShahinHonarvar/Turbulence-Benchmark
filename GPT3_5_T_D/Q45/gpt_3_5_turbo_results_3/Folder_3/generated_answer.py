
def palindromes_between_indices(string):
    import itertools
    from string import ascii_letters

    # Extract letters from given string within the specified range
    letters = [c.lower() for c in string[7:10] if c.isalpha()]

    # Create permutations of letters
    perms = set(''.join(perm) for perm in itertools.permutations(letters))
    
    # Filter out palindromes of length at least 3
    palindromes = [perm for perm in perms if len(perm) >= 3 and perm == perm[::-1]]

    return set(palindromes)
