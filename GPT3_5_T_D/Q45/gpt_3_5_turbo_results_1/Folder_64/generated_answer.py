
import itertools

def palindromes_between_indices(string):
    string = string.lower()
    letters = [char for char in string if char.isalpha()]

    if len(letters) >= 10:
        letters = letters[4:10]
        palindromes = set()
        for perm in itertools.permutations(letters):
            word = ''.join(perm)
            if word == word[::-1] and len(word) >= 5:
                palindromes.add(word)
        return palindromes
    else:
        return set()
