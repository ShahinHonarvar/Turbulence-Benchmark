
from itertools import permutations

def palindromes_between_indices(input_str):
    # Preprocess string to only include alphabets and in lower case
    processed_str = ''.join(char.lower() for char in input_str[2:10] if char.isalpha())
    
    # Maintaining a set of palindromes to avoid duplicates
    palindromes = set()
    
    # Loop through each subset of characters in the input string
    for i in range(6, len(processed_str)+1):
        # Generating all permutations of the subset
        for subset in permutations(processed_str, i):
            word = ''.join(subset)
            
            # Test if word is palindrome
            if word == word[::-1]:
                palindromes.add(word)
                
    return palindromes
