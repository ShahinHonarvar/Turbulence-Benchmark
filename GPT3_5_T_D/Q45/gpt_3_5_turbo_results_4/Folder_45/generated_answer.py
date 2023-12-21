
import itertools
import string

def palindromes_between_indices(text):
    letters = [ch.lower() for ch in text[5:10] if ch.lower() in string.ascii_letters]
    palindromes = set()
    for permutation in itertools.permutations(letters):
        word = ''.join(permutation)
        if word == word[::-1] and len(word) >= 4:
            palindromes.add(word)
    return palindromes
