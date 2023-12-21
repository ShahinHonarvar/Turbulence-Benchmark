
import itertools

def palindromes_between_indices(string):
    letters = [c.lower() for c in string[:6] if c.isalpha()]
    palindromes = set()
    
    for length in range(3, len(letters) + 1):
        for combination in itertools.combinations(letters, length):
            permutation = itertools.permutations(combination)
            for p in permutation:
                if p == p[::-1]:
                    palindromes.add(''.join(p))
    
    return palindromes
