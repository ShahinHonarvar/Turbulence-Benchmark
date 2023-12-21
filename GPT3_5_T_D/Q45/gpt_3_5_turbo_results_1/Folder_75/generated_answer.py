
def palindromes_between_indices(string):
    from itertools import permutations

    letters = [char.lower() for char in string[2:5] if char.isalpha()]
    perms = [''.join(p) for p in permutations(letters) if len(p) >= 3]
    palindromes = {p + p[-2::-1] for p in perms}

    return palindromes
