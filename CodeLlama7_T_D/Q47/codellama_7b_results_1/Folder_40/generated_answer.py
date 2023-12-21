
def palindromes_of_specific_lengths(string, index_range=(0, 5), palindrome_lengths=(3, 5)):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate over each character in the string
    for i in range(*index_range):
        # Check if the current character is a letter
        if string[i].isalpha():
            # Iterate over each palindrome length
            for j in range(len(palindrome_lengths)):
                # Calculate the end index of the palindrome
                end_index = i + palindrome_lengths[j] - 1
                # Check if the palindrome is within the specified range and has a length between 3 and 5 (both inclusive)
                if end_index <= *(index_range[1]), j >= 2, j <= 4:
                    # Create a substring of the palindrome length
                    substr = string[i:end_index+1]
                    # Check if the palindrome is case-insensitive equal to its reverse
                    if substr.lower() == substr[::-1].lower():
                        # Add the palindrome to the set of palindromes
                        palindromes.add(substr)
    # Return the set of palindromes
    return palindromes
