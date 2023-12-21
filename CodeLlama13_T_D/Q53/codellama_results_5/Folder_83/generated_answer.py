
def palindrome_of_length_at_least_n(string):
    # Create a set to store the palindromes
    palindromes = set()
    
    # Iterate over each character in the string
    for i in range(len(string)):
        # Check if the substring of length 60 starting from the current index is a palindrome
        if len(string[i:i+60]) == 60 and string[i:i+60] == string[i:i+60][::-1]:
            # Add the palindrome to the set
            palindromes.add(string[i:i+60])
    
    # Return the set of palindromes
    return palindromes
