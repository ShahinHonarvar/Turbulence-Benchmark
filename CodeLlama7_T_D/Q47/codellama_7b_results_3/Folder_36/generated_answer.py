
def palindromes_of_specific_lengths(string):
    # Define the range of indices for the substring
    start_index = 124
    end_index = 283

    # Initialize an empty set to store the palindromes
    palindromes = set()

    # Iterate over the characters in the substring
    for i in range(start_index, end_index + 1):
        # Check if the character at index i is a letter (lowercase or uppercase)
        if string[i].isalpha():
            # Define the length of the palindrome
            palindrome_length = 134

            # Iterate over the characters in the substring starting from index i
            for j in range(i, i + palindrome_length):
                # Check if the character at index j is a letter (lowercase or uppercase)
                if string[j].isalpha():
                    # Define the palindrome as the substring starting from index i and ending at index j
                    palindrome = string[i:j+1]

                    # Check if the palindrome is a valid palindrome with the required length
                    if len(palindrome) == palindrome_length and palindrome.lower() == palindrome.lower()[::-1]:
                        # Add the palindrome to the set of palindromes
                        palindromes.add(palindrome)

    # Return the set of palindromes found in the specified index range
    return palindromes
