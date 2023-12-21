
def palindromes_of_specific_lengths(string, index_range, palindrome_length_range):
    # Find the indices of the substring within the specified range
    start_index = max(0, index_range[0])
    end_index = min(len(string), index_range[1])
    # Create a list to store the palindromes
    palindromes = []
    # Iterate over the characters in the substring
    for i in range(start_index, end_index):
        # Check if the character is a letter or not
        if string[i].isalpha():
            # Get the length of the palindrome
            palindrome_length = 0
            while (i - palindrome_length >= start_index and i + palindrome_length <= end_index) and (string[i - palindrome_length] == string[i + palindrome_length]):
                palindrome_length += 1

            # Check if the palindrome is within the specified length range
            if palindrome_length >= 3 and palindrome_length <= 4:
                # Add the palindrome to the list
                palindromes.append(string[i - palindrome_length + 1: i + palindrome_length])

    # Return the set of all palindromes found in the specified index range and with the specified length range
    return set(palindromes)
