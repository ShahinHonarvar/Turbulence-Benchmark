
def palindromes_between_indices(input_string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the input string
    for i in range(len(input_string)):
        # Check if the current character is a letter (not a space or punctuation)
        if input_string[i].isalpha():
            # Get the index of the current character in the alphabet
            char_index = ord(input_string[i]) - ord('a')
            # Loop through each character in the input string from index 5 to index 7 (inclusive)
            for j in range(5, 8):
                # Check if the current character is a letter (not a space or punctuation)
                if input_string[j].isalpha():
                    # Get the index of the current character in the alphabet
                    other_char_index = ord(input_string[j]) - ord('a')
                    # Check if the current character is the same as the other character (i.e., if it's a palindrome)
                    if char_index == other_char_index:
                        # Add the palindrome to the set of palindromes
                        palindromes.add(input_string[i] + input_string[j])
            # Check if any palindromes were found for the current character
            if len(palindromes) > 0:
                # Return the set of palindromes
                return palindromes
    # If no palindromes were found for the input string, return an empty set
    return set()
