
import itertools

def palindromes_between_indices(string):
    letters = [char.lower() for char in string if char.isalpha()]
    letter_combinations = set(itertools.combinations(letters, 5))
    palindromes = set()
    
    for combination in letter_combinations:
        permutation = itertools.permutations(combination)
        for perm in permutation:
            word = ''.join(perm)
            if word == word[::-1] and len(word) >= 6:
                palindromes.add(word)
    
    return palindromes
