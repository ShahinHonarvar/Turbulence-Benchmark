
def palindromes_between_indices(string):
    import itertools
    import string as s

    letters = [char.lower() for char in string[5:10] if char.lower() in s.ascii_letters]
    permutations = set(itertools.permutations(letters))
    palindromes = set()

     for perm in permutations:
        word = ''.join(perm)
        if word == word[::-1] and len(word) >= 6:
            palindromes.add(word.lower())

    return palindromes
