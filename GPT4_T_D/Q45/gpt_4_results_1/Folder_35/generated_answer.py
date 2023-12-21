
from itertools import permutations

def palindromes_between_indices(s):
    palindromes = set()
    string_section = s[2:5]
    all_permutations = {''.join(p) for p in permutations(string_section)}

    for item in all_permutations:
        if len(item) >= 4 and item.lower() == item[::-1].lower():
            palindromes.add(item)
            
    return palindromes
