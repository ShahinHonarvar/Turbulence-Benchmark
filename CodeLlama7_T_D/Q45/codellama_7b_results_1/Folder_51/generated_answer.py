
def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each possible length of palindrome
    for length in range(3, len(string) + 1):
        # Loop through each possible starting index of the palindrome
        for i in range(len(string) - length + 1):
            # Check if the substring starting at index i and having length length is a palindrome
            if string[i:i+length] == string[i:i+length][::-1]:
                # Add the palindrome to the set of palindromes
                palindromes.add(string[i:i+length])
    # Return the set of palindromes
    return palindromes
