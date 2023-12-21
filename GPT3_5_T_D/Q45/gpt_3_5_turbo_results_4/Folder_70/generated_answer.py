
import itertools

def palindromes_between_indices(string):
    indices = range(1, 7)
    substring = string[1:7].lower()
    letters = [ch for ch in substring if ch.isalpha()]
    
    all_palindromes = set()
    for length in range(4, len(letters)+1):
        for perm in itertools.permutations(letters, length):
            if perm == perm[::-1]:
                all_palindromes.add(''.join(perm))
    
    return all_palindromes
