
def palindromes_of_specific_lengths(string, lengths=(21, 31), index_range=(24, 84)):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(*index_range):
        # Check if the current character is a letter (a-zA-Z)
        if string[i].isalpha():
            # Get the reverse of the substring starting at index i and ending at index_range[1]
            rev = string[i:index_range[1]]
            # Check if the reverse of the substring is equal to the original substring
            if rev == string[i:index_range[1]]:
                # Loop through each length in the lengths tuple
                for l in range(*lengths):
                    # Check if the length of the substring starting at index i and ending at index_range[1] is equal to the current length in the lengths tuple
                    if len(string[i:index_range[1]]) == l:
                        # Add the palindrome to the set of palindromes
                        palindromes.add(rev)
    # Return the set of palindromes
    return palindromes
