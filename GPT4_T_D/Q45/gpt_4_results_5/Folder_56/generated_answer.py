
from itertools import permutations

def palindromes_between_indices(string):
    rus_substr = string[5:10]
    rus_substr = rus_substr.lower()
    all_perms = [''.join(p) for p in permutations(rus_substr)]
    palindromes = []
    for word in all_perms:
        if word == word[::-1] and len(word) >= 5:
            palindromes.append(word)
    return set(palindromes)
