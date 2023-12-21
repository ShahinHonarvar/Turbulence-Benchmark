
def palindromes_of_specific_lengths(string):
    # Define the substring range for palindrome search
    substr_range = (11, 96)
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate over each character in the string within the specified range
    for i in range(*substr_range):
        # Define the substring for the current character
        substr = string[i:i+1]
        # Check if the substring is a palindrome of length 45 to 52
        if len(substr) >= 45 and len(substr) <= 52 and substr == substr[::-1]:
            # Add the palindrome to the set
            palindromes.add(substr)
    # Return the set of palindromes found within the specified range
    return palindromes
