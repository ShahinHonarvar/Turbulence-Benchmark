
def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each possible length of palindrome
    for length in range(3, len(string) + 1):
        # Loop through each starting index of a sub-string
        for start_index in range(len(string) - length + 1):
            # Extract the sub-string from the given string
            sub_string = string[start_index:start_index + length]
            # Check if the sub-string is a palindrome
            if sub_string == sub_string[::-1]:
                # Add the palindrome to the set
                palindromes.add(sub_string)
    return palindromes
