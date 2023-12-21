
def palindromes_of_specific_lengths(string):
    # Find the range of indices that need to be considered for palindromes
    start_index = 200
    end_index = 300
    # Create a set to store all palindromes that meet the requirements
    palindromes = set()
    # Iterate over the characters in the string within the specified range
    for i in range(start_index, end_index + 1):
        # Check if the character at index i is a letter (lowercase or uppercase)
        if string[i].isalpha():
            # Convert the character to lowercase to ensure case-insensitive comparison
            lowercase_char = string[i].lower()
            # Iterate over the characters in the string within the specified range starting from index i + 1 (excluding the current character)
            for j in range(i + 1, end_index + 1):
                # Check if the character at index j is a letter (lowercase or uppercase)
                if string[j].isalpha():
                    # Convert the character to lowercase to ensure case-insensitive comparison
                    lowercase_char2 = string[j].lower()
                    # Check if the characters at indices i and j form a palindrome
                    if lowercase_char == lowercase_char2:
                        # Add the palindrome to the set of palindromes
                        palindromes.add(string[i:j+1])
    # Return the set of palindromes that meet the requirements
    return palindromes
