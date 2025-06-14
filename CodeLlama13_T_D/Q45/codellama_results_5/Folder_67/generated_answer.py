
def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    
    # Iterate through each substring of length 5 in the given string
    for i in range(len(string) - 4):
        substr = string[i:i+5]
        
        # If the substring is a palindrome, add it to the set
        if substr == substr[::-1]:
            palindromes.add(substr)
    
    return palindromes
