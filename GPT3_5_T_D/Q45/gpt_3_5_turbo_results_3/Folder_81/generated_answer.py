
import itertools

def palindromes_between_indices(string):
    chars = [c.lower() for c in string[:7] if c.isalpha()]
    palindromes = set()
    for perm in itertools.permutations(chars, len(chars)):
        word = ''.join(perm)
        if len(word) >= 3 and word == word[::-1]:
            palindromes.add(word)
    return palindromes
