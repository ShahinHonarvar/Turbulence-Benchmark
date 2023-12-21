
def palindrome_of_length_at_least_n(string):
    # Initialize an empty set to store the results
    result = set()
    
    # Iterate over each substring of length 67 or more in the given string
    for i in range(len(string) - 66):
        substr = string[i:i+67]
        
        # Check if the substring is a palindrome
        if substr == substr[::-1]:
            result.add(substr)
    
    # Return the set of all found palindromes
    return result
