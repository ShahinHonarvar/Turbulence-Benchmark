
from itertools import permutations

def palindromes_between_indices(s):
    s = s[1:7].lower()
    letters = ''.join(filter(str.isalpha, s))
    palindromes = set()

    for i in range(7, len(letters) + 1):
        for p in permutations(letters, i):
            word = ''.join(p)
            if word == word[::-1]:
                palindromes.add(word)
                
    return palindromes
