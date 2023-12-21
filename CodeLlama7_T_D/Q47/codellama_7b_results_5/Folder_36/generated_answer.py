
def palindromes_of_specific_lengths(string, lengths):
    # Create a list to store the palindromes
    palindromes = []
    # Iterate over each length in the specified range
    for length in lengths:
        # Get the substring of the specified length from the input string
        substring = string[124:length]
        # Check if the substring is a palindrome
        if is_palindrome(substring):
            # Add the palindrome to the list
            palindromes.append(substring)
    return set(palindromes)
