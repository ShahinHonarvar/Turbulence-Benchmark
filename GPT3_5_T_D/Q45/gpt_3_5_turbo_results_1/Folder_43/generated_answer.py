
import itertools

def palindromes_between_indices(string):
    letters = [ch.lower() for ch in string if ch.isalpha()]
    arranged_letters = set(itertools.permutations(letters, 4))
    palindromes = set()
    
    for arr in arranged_letters:
        if arr == arr[::-1]:
            palindromes.add("".join(arr))
    
    return palindromes
