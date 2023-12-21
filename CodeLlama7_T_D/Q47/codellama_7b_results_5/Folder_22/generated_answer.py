 def palindromes_of_specific_lengths(string, min_len=5, max_len=10):
    # Check if the input string is a palindrome
    if string == string[::-1]:
        return {string}

    # Initialize an empty set to store the palindromes
    palindromes = set()

    # Iterate over the characters in the string
    for i in range(len(string)):
        # Check if the character is a letter (i.e., not a whitespace or punctuation)
        if string[i].isalpha():
            # Get the substring starting from the current index and ending at the end of the string
            substr = string[i:]

            # Iterate over the characters in the substring
            for j in range(len(substr)):
                # Check if the substring is a palindrome
                if substr == substr[::-1]:
                    # Add the palindrome to the set of palindromes
                    palindromes.add(substr)

                    # Break out of the inner loop since we have found a palindrome
                    break

    # Return the set of palindromes that meet the requirements
    return palindromes
