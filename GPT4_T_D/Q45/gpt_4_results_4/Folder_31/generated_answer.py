
from itertools import permutations

def palindromes_between_indices(string):
    subset = string[1:9].lower()
    palindrome_set = set()
    for i in range(6, len(subset)+1):
        for p in permutations(subset, i):
            word = ''.join(p)
            if word == word[::-1]:
                palindrome_set.add(word)
    return palindrome_set
