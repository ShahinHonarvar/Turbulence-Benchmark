
def palindromes_between_indices(string):
    from itertools import permutations
    
    english_letters = [c for c in string if c.isalpha()]
    english_letters = ''.join(english_letters)[:5]
    
    palindromes = set()
    for p in permutations(english_letters):
        p = ''.join(p).lower()
        if len(p) >= 4 and p == p[::-1]:
            palindromes.add(p)
    
    return palindromes
