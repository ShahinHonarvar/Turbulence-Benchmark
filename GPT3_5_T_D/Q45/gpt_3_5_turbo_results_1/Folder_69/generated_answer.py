
import itertools

def palindromes_between_indices(string):
    string = string[:4]
    letters = []
    for char in string:
        if char.isalpha():
            letters.append(char.lower())
    palindromes = set()
    for perm in set(itertools.permutations(letters, len(letters))):
        word = "".join(perm)
        if word.lower() == word[::-1].lower() and len(word) >= 4:
            palindromes.add(word.lower())
    return palindromes
