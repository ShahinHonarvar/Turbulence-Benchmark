
def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each possible length of palindrome
    for length in range(4, len(string) + 1):
        # Loop through each possible starting index of the palindrome
        for start_index in range(3, len(string) - length + 2):
            # Check if the substring starting at the current index and having the current length is a palindrome
            if string[start_index:start_index + length] == string[start_index:start_index + length][::-1]:
                # Add the palindrome to the set of palindromes
                palindromes.add(string[start_index:start_index + length])
    # Return the set of palindromes
    return palindromes
