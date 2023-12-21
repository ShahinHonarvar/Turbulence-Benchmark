
import itertools

def palindromes_between_indices(s):
    letters = [ch.lower() for ch in s[3:10] if ch.isalpha()]
    palindromes = set()
    for perm in itertools.permutations(letters):
        word = ''.join(perm)
        if word == word[::-1] and len(word) >= 3:
            palindromes.add(word)
    return palindromes
