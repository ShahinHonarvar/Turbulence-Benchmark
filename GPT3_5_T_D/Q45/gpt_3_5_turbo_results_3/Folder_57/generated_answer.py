
import itertools

def palindromes_between_indices(s):
    english_letters = [c for c in s if c.isalpha()]
    english_letters = map(str.lower, english_letters)
    english_letters = set(english_letters)
    palindromes = set()
    
    for combination in itertools.combinations(english_letters, 4):
        permutations = itertools.permutations(combination)
        for perm in permutations:
            word = ''.join(perm)
            if word == word[::-1] and len(word) >= 5:
                palindromes.add(word)
    
    return palindromes
