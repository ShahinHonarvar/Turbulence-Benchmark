
import itertools

def palindromes_between_indices(string):
    letters = [c.lower() for c in string if c.isalpha()]
    combinations = [''.join(combo) for combo in itertools.permutations(letters, 4)]
    palindromes = set()
    for combo in combinations:
        if combo == combo[::-1]:
            palindromes.add(combo)
    return palindromes
