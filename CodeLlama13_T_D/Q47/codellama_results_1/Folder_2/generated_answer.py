
def palindromes_of_specific_lengths(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    
    # Loop through each character in the string
    for i in range(10, 60):
        # Check if the substring from index 10 to index 59 is a palindrome
        substr = string[i:i+18]
        if len(substr) == 18 and substr == substr[::-1]:
            # Add the palindrome to the set
            palindromes.add(substr)
    
    return palindromes
