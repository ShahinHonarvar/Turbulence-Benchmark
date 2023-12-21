
def palindromes_of_specific_lengths(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    
    # Loop through each character in the string
    for i in range(18, 99):
        # Check if the substring from index i-18 to i+1 is a palindrome
        if string[i-18:i+2] == string[i-18:i+2][::-1]:
            # If it is a palindrome, add it to the set of palindromes
            palindromes.add(string[i-18:i+2])
    
    # Return the set of palindromes
    return palindromes
