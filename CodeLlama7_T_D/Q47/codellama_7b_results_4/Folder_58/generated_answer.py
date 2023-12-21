
def palindromes_of_specific_lengths(string, lengths):
    # Convert the string to lowercase for case-insensitive comparison
    string = string.lower()

    # Define a set to store the palindromes
    palindromes = set()

    # Iterate over the specified index range
    for i in range(125, 283 + 1):
        # Check if the character at position i is a letter
        if string[i].isalpha():
            # Create a substring from position i to the end of the string
            substring = string[i:]

            # Iterate over the specified lengths
            for length in lengths:
                # Check if the substring has the specified length
                if len(substring) == length:
                    # Check if the substring is a palindrome
                    if substring == substring[::-1]:
                        # Add the palindrome to the set
                        palindromes.add(substring)

            # Break out of the inner loop since we have found all possible palindromes for this length
            break

    # Return the set of palindromes
    return palindromes
