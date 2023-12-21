
def palindrome_of_length_at_least_n(string, n):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    
    # Iterate over each substring of length >= 41 in the given string
    for i in range(len(string) - 40):
        substr = string[i:i+41]
        
        # Check if the substring is a palindrome by checking if it is equal to its reverse
        if substr == substr[::-1]:
            # Add the palindrome to the set
            palindromes.add(substr)
    
    # Return the set of all palindromes found in the given string
    return palindromes
