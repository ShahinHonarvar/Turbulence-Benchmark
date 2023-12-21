 def palindrome_of_length_at_least_n(string, n):
    # Convert the string to lowercase for case-insensitive comparison
    string = string.lower()
    # Initialize an empty set to store the palindromes

    palindromes = set()
    # Iterate over each character in the string

    for i in range(len(string)):
        # Check if the current character is a letter (i.e., not a whitespace or punctuation)

        if string[i].isalpha():
            # Start iterating from the next character and check for palindromes of length greater than or equal to n

            for j in range(i + 1, len(string)):
                # Check if the substring starting at index i and ending at index j is a palindrome

                if string[i:j] == string[i:j][::-1]:
                    # If the substring is a palindrome, add it to the set of palindromes

                    palindromes.add(string[i:j])
                    # Break out of the inner loop since we have found a palindrome

                    break

    # Return the set of palindromes

    return palindromes
