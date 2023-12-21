
import itertools

def palindromes_between_indices(string):
    letters = [char.lower() for char in string if char.isalpha()]
    palindromes = set()
    
    for length in range(5, len(letters) + 1):
        for combination in itertools.combinations(letters, length):
            permutation = itertools.permutations(combination)
            for p in permutation:
                if p == p[::-1]:
                    palindromes.add(''.join(p))
    
    return palindromes
