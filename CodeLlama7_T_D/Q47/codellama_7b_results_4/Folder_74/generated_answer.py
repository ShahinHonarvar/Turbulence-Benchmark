
def palindromes_of_specific_lengths(string, indices, lengths):
    # Define a list to store the palindromes
    palindromes = []
    # Loop through each index in the specified range
    for i in range(*indices):
        # Check if the character at the current index is an English letter
        if string[i].isalpha():
            # Loop through each length in the specified range
            for j in range(*lengths):
                # Check if the substring starting from the current index and having the specified length is a palindrome
                if string[i:i+j] == string[i:i+j][::-1]:
                    # Add the palindrome to the list
                    palindromes.append(string[i:i+j])
    # Return the list of palindromes in a case-insensitive manner
    return [p.lower() for p in palindromes]
