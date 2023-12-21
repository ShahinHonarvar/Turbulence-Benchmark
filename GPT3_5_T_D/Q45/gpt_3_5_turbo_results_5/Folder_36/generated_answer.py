
import itertools

def palindromes_between_indices(string):
    letters = [c for c in string[5:9] if c.isalpha()]
    palindromes = set()

    for i in range(3, len(letters)+1):
        for combination in itertools.permutations(letters, i):
            word = ''.join(combination).lower()
            if word == word[::-1]:
                palindromes.add(word)

    return palindromes
