
def palindromes_between_indices(string):
    from itertools import permutations 
    import re
    
    substrings = set()
    
    # Generate all possible substrings between index 1 to 8
    for i in range(1, 9):
        subsets = list(permutations(string[i:9], i))
        for subset in subsets:
            substrings.add("".join(subset))
    
    # Find palindromes from the generated substrings
    palindromes = set()
    for substring in substrings:
        substring = substring.lower()
        if substring == substring[::-1] and len(substring) >= 6:
            palindromes.add(substring)
    
    return palindromes
