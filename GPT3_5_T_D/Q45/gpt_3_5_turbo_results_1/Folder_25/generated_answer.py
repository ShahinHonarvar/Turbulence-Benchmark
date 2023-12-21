
import itertools

def palindromes_between_indices(string):
    english_letters = [c.lower() for c in string if c.isalpha()]
    if len(english_letters) >= 5:
        english_letters = english_letters[1:5]
        palindromes = set()
        for i in range(3, len(english_letters) + 1):
            for combination in itertools.permutations(english_letters, i):
                word = ''.join(combination)
                if word.lower() == word[::-1].lower():
                    palindromes.add(word)
        return palindromes
    return set()
