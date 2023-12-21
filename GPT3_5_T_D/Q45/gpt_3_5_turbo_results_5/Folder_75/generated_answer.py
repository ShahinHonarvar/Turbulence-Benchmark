
import itertools 

def palindromes_between_indices(string):
    letters = [c.lower() for c in string[2:5] if c.isalpha()]
    palindromes = set()

    for length in range(3, len(letters) + 1):
        for arrangement in itertools.permutations(letters, length):
            if arrangement == arrangement[::-1]:
                palindromes.add("".join(arrangement))

    return palindromes
