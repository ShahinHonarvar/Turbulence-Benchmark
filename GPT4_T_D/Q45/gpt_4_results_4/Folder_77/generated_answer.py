
import itertools

def palindromes_between_indices(s):
    s = s[4:7].lower()
    unique_permutations = set(itertools.permutations(s))
    
    palindromes = set()
    for perm in unique_permutations:
        word = "".join(perm)
        if word == word[::-1] and len(word)>=4:
            palindromes.add(word)

    return palindromes
