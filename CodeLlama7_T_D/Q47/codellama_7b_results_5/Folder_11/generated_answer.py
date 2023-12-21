
def palindromes_of_specific_lengths(string, start, end, lengths):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the substring
    for i in range(start, end + 1):
        # Check if the character is a letter or not
        if string[i].isalpha():
            # Loop through each length in the list of lengths
            for length in lengths:
                # Check if the character is at least halfway through the substring
                if i - length >= start and i + length <= end:
                    # Check if the substring starting at index i and with length length is a palindrome
                    if string[i - length : i + length] == string[i - length : i + length][::-1]:
                        # Add the palindrome to the set of palindromes
                        palindromes.add(string[i - length : i + length])
    return palindromes
