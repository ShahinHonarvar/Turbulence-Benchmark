
def palindromes_of_specific_lengths(string):
    # Define the substring range for searching palindromes
    substr_range = string[100:300]
    # Create an empty set to store the found palindromes
    palindromes = set()
    # Loop through each character in the substring range
    for i in range(len(substr_range)):
        # Define the starting index for the current character
        start_idx = i

        # Define the ending index for the current character
        end_idx = len(substr_range) - i

        # Check if the substring from the starting index to the ending index is a palindrome
        substr = substr_range[start_idx:end_idx]
        if substr == substr[::-1]:
            # Add the palindrome to the set of found palindromes
            palindromes.add(substr)
    # Return the set of found palindromes
    return palindromes
