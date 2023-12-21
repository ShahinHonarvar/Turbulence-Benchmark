
def palindrome_of_length_at_least_n(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    
    # Loop through each character in the string
    for i in range(len(string)):
        # Check if the substring from index i to index 40 is a palindrome
        if string[i:41] == string[i:41][::-1]:
            # Add the palindrome to the set
            palindromes.add(string[i:41])
    
    # Return the set of palindromes
    return palindromes
