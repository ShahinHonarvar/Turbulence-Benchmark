
def palindromes_of_specific_lengths(string):
    # Define the range of lengths to consider
    min_len = 37
    max_len = 60
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate over the characters in the string
    for i in range(11, 84):
        # Get the substring starting at index i and ending at index i + max_len - 1
        substr = string[i:i+max_len-1]
        # Check if the substring is a palindrome
        if substr == substr[::-1]:
            # Add the palindrome to the set
            palindromes.add(substr)
    return palindromes
