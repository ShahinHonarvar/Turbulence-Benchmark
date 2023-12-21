
def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each possible length of palindrome
    for length in range(4, len(string) + 1):
        # Get the starting and ending indices for the current length of palindrome
        start_index = 4
        end_index = min(start_index + length - 1, len(string))
        # Loop through each possible starting index for the current length of palindrome
        for i in range(start_index, end_index + 1):
            # Get the substring that starts at the current starting index and ends at the current ending index
            substring = string[i:end_index + 1]
            # Check if the substring is a palindrome of the specified length
            if len(substring) == length and substring == substring[::-1]:
                # Add the palindrome to the set of palindromes
                palindromes.add(substring)
    # Return the set of palindromes
    return palindromes
