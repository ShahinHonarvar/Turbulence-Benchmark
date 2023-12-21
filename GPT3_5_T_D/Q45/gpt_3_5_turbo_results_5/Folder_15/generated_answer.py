
import itertools

def palindromes_between_indices(string):
    string = string.lower()
    letters = [char for char in string if char.isalpha()]
    
    palindromes = set()
    for length in range(3, len(letters) + 1):
        for comb in itertools.combinations(letters, length):
            perm = set(itertools.permutations(comb))
            for p in perm:
                if ''.join(p) == ''.join(p)[::-1]:
                    palindromes.add(''.join(p))
    
    return palindromes
