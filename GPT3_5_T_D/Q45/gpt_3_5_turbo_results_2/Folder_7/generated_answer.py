
import itertools

def palindromes_between_indices(s):
    english_letters = [c.lower() for c in s if c.isalpha()]
    combinations = list(itertools.combinations(english_letters, 7))
    palindromes = set()
    
    for comb in combinations:
        palindrome = ''.join(comb) + ''.join(reversed(comb))
        palindromes.add(palindrome)
        
    return palindromes
