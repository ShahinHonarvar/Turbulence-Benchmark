
def palindromes_between_indices(string):
    from itertools import permutations

    letters = [ch for ch in string.lower() if ch.isalpha()]
    palindromes = set()

    for perm in permutations(letters[3:9], 6):
        if perm == perm[::-1]:
            palindromes.add(''.join(perm))

    return palindromes
