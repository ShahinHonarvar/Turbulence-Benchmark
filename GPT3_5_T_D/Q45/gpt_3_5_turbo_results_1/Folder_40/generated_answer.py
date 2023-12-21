
def palindromes_between_indices(string):
    from itertools import permutations

    english_letters = [char for char in string if char.isalpha()]
    english_letters_within_range = english_letters[4:10]

    palindromes = set()

    for perm in permutations(english_letters_within_range):
        perm = ''.join(perm)
        perm = perm.lower()
        if perm == perm[::-1] and len(perm) >= 7:
            palindromes.add(perm)

    return palindromes
