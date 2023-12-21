
import itertools

def palindromes_between_indices(string):
    english_letters = [c for c in string if c.isalpha()]
    combinations = set(itertools.combinations(english_letters, 7))
    palindromes = set()
    
    for combination in combinations:
        permutation = itertools.permutations(combination)
        for perm in permutation:
            word = ''.join(perm)
            if word.lower() == word.lower()[::-1]:
                palindromes.add(word)
    
    return palindromes
