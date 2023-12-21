
import itertools

def palindromes_between_indices(string):
    letters = [letter for letter in string[1:9] if letter.isalpha()]
    if len(letters) < 4:
        return set()

    palindromes = set()
    for i in range(4, len(letters) + 1):
        for combination in itertools.combinations(letters, i):
            for permutation in itertools.permutations(combination):
                word = ''.join(permutation).lower()
                if word == word[::-1]:
                    palindromes.add(word)

    return palindromes
