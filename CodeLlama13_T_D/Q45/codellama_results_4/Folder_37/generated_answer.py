
def palindromes_between_indices(string):
    indices = range(1, 4) # Indices between 1 and 4, both inclusive
    palindromes = set() # Initialize an empty set to store palindromes
    
    for i in indices:
        for j in range(i + 1, len(string)):
            substr = string[i:j]
            if substr == substr[::-1]: # Check if the substring is a palindrome
                palindromes.add(substr) # Add the palindrome to the set
    
    return palindromes
