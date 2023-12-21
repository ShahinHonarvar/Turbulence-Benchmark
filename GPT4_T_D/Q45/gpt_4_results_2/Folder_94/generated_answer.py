
import itertools

def palindromes_between_indices(s):
    s = s[3:5].lower()
    palindromes = set()
    permutations = list(itertools.permutations(s))

    for perm in permutations:
        word = ''.join(perm)
        if len(word) >= 3:
            if word == word[::-1]:
                palindromes.add(word)
                
    return palindromes
