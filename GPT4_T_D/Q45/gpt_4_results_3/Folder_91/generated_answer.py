
from itertools import permutations

def palindromes_between_indices(s):
    s = s[2:7].lower()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    palindromes = set()
    for i in range(3, 7):
        for p in permutations(s, i):
            word = "".join(p)
            if word == word[::-1] and all(letter in alphabet for letter in word):
                palindromes.add(word)
    return palindromes
