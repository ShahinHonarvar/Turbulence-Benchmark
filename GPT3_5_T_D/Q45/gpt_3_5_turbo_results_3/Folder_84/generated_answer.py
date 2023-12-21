
import itertools

def palindromes_between_indices(string):
    letters = [char.lower() for char in string[4:10] if char.isalpha()]
    palindromes = set()
    for perm in itertools.permutations(letters):
        word = "".join(perm)
        if word == word[::-1] and len(word) >= 3:
            palindromes.add(word)
    return palindromes
