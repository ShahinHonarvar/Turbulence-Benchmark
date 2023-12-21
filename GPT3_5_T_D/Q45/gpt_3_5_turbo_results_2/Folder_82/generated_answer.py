
import itertools

def palindromes_between_indices(string):
    english_letters = [c.lower() for c in string if c.isalpha()]
    combinations = list(itertools.permutations(english_letters, 6))
    palindromes = set()
    
    for combo in combinations:
        palindrome = ''.join(combo) + ''.join(reversed(combo))
        if len(palindrome) >= 7 and palindrome == palindrome[::-1]:
            palindromes.add(palindrome)
    
    return palindromes
