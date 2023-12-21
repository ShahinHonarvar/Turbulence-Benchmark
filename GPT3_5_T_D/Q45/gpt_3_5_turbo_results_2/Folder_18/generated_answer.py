
def palindromes_between_indices(string):
    import itertools
    from string import ascii_letters

    letters = [ch for ch in string[1:7] if ch in ascii_letters]
    perm = set(itertools.permutations(letters))

    palindromes = set()
    for p in perm:
        word = ''.join(p)
        if word.lower() == word[::-1].lower() and len(word) >= 3:
            palindromes.add(word)

    return palindromes
