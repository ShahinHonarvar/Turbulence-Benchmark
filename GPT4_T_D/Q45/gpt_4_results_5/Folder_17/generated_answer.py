
from itertools import permutations

def palindromes_between_indices(string):
    trimmed_string = string[2:7].lower()
    palindrome_set = set()
    for i in range(4, len(trimmed_string) + 1):
        perms = set(permutations(trimmed_string, i))
        perms = [''.join(perms[i]) for i in range(len(perms))]
        for word in perms:
            if word == word[::-1]:
                palindrome_set.add(word)
    return palindrome_set
