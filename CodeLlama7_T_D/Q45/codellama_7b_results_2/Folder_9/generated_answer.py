
def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each letter in the string
    for i in range(len(string)):
        # Get the substring of the string starting at index i and ending at index 6 (inclusive)
        sub_str = string[i:i+7]
        # Check if the substring is a palindrome
        if sub_str == sub_str[::-1]:
            # Add the palindrome to the set
            palindromes.add(sub_str)
    # Return the set of palindromes
    return palindromes
