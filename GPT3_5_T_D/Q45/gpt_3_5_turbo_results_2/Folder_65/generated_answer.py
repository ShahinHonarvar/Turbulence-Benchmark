
import itertools

def palindromes_between_indices(string):
    string = string[:7]
    letters = [s.lower() for s in string if s.isalpha()]
    permutations = set(itertools.permutations(letters))

    palindromes = set()
    for perm in permutations:
        word = ''.join(perm)
        if word == word[::-1] and len(word) >= 5:
            palindromes.add(word)

    return palindromes
