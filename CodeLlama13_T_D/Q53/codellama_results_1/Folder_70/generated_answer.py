
def palindrome_of_length_at_least_n(string, n):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    
    # Iterate over each substring of the given string
    for i in range(len(string)):
        for j in range(i+1, len(string)+1):
            # Check if the current substring is a palindrome
            if string[i:j] == string[i:j][::-1]:
                # Add the palindrome to the set
                palindromes.add(string[i:j])
    
    # Return the set of all palindromes found in the given string
    return palindromes
