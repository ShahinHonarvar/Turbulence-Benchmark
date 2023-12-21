
import itertools

def palindromes_between_indices(string):
    letters = [char.lower() for char in string[1:9] if char.isalpha()]
    permutations = [''.join(permutation) for permutation in itertools.permutations(letters)]
    palindromes = {permutation for permutation in permutations if len(permutation) >= 7 and permutation == permutation[::-1]}
    return palindromes
