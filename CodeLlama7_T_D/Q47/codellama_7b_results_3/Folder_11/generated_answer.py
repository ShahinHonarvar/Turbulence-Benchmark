
def palindromes_of_specific_lengths(string):
    # Define the range of indices for the substring search
    start_index = 24
    end_index = 97
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate over each character in the string within the specified index range
    for i in range(start_index, end_index + 1):
        # Define the substring containing the current character
        substr = string[i - 24:i + 1]
        # Check if the substring is a palindrome
        if substr == substr[::-1]:
            # Add the palindrome to the set
            palindromes.add(substr)
    return palindromes
