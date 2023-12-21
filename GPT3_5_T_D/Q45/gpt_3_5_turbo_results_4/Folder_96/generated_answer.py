
import itertools

def palindromes_between_indices(string):
    indices = range(3, 9)
    letters = [char.lower() for char in string if char.isalpha()]
    combinations = itertools.combinations(letters, len(indices))
    palindromes = {"".join(combination) for combination in combinations if "".join(combination) == "".join(combination)[::-1]}
    return palindromes
