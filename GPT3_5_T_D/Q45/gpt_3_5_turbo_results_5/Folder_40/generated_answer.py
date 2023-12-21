
import itertools

def palindromes_between_indices(string):
    alphabet = [chr(i) for i in range(ord('a'), ord('z')+1)]
    indices = range(4, 10)

    letters = [char.lower() for char in string if char.isalpha()]
    letters = [char for char in letters if char in alphabet]

    if len(letters) < 7:
        return set()

    palindromes = set()
    for combination in itertools.combinations(letters, 6):
        for permutation in itertools.permutations(combination):
            word = "".join(permutation)
            if word.lower() == word.lower()[::-1]:
                palindromes.add(word)

    return palindromes
