
import itertools

def palindromes_between_indices(s):
    english_letters = [c.lower() for c in s if c.isalpha()]
    palindromes = set()
    
    for combination in itertools.combinations(english_letters, 7):
        permutation = itertools.permutations(combination)
        for perm in permutation:
            word = ''.join(perm)
            if word == word[::-1]:
                palindromes.add(word)
    
    return palindromes
