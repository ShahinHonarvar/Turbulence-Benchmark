
def palindromes_of_specific_lengths(string):
    # Define the range of lengths for palindromes
    min_length = 5
    max_length = 80
    # Create an empty set to store the palindromes
    palindromes = set()
    # Iterate over the characters in the string
    for i in range(len(string)):
        # Get the substring starting from index i
        substring = string[i:]
        # Iterate over the lengths of palindromes to check
        for length in range(min_length, max_length + 1):
            # Get the palindrome with the specified length
            palindrome = substring[:length]
            # Check if the palindrome is a valid palindrome
            if len(palindrome) == length and palindrome == palindrome[::-1]:
                # Add the palindrome to the set of palindromes
                palindromes.add(palindrome)
    # Return the set of palindromes
    return palindromes
