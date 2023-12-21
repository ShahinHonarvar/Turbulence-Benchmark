
def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each possible length of palindrome
    for length in range(3, len(string) + 1):
        # Loop through each possible starting index of the palindrome
        for start_index in range(len(string) - length + 1):
            # Check if the substring starting at the current index is a palindrome
            if string[start_index:start_index + length] == string[start_index:start_index + length][::-1]:
                # Add the palindrome to the set
                palindromes.add(string[start_index:start_index + length])
    return palindromes
