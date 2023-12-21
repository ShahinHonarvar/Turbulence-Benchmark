
import itertools

def palindromes_between_indices(s):
    english_letters = [c.lower() for c in s if c.isalpha()]
    palindromes = set()
    for p in itertools.permutations(english_letters[2:9], 7):
        word = ''.join(p)
        if word.lower() == word.lower()[::-1]:
            palindromes.add(word)
    return palindromes
