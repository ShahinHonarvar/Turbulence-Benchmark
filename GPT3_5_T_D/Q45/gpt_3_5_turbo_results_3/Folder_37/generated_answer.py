
import itertools
import re

def palindromes_between_indices(string):
    letters = set(re.findall(r'[a-zA-Z]', string))
    combinations = [''.join(comb) for comb in itertools.permutations(letters, 4) if len(comb) == len(set(comb))]
    palindromes = set()
    
    for comb in combinations:
        palindrome = comb + comb[::-1]
        if palindrome.lower() == palindrome[::-1].lower():
            palindromes.add(palindrome)
    
    return palindromes
