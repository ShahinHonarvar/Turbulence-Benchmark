
def palindromes_between_indices(string):
    from itertools import permutations
    from string import ascii_letters

    letters = [char.lower() for char in string[5:8] if char.isalpha()]
    palindromes = set()

    for perm in permutations(letters, len(letters)):
        word = ''.join(perm)
        if word == word[::-1] and len(word) >= 3:
            palindromes.add(word)

    return palindromes
