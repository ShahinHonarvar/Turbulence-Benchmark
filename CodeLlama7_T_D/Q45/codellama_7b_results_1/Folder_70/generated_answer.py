
def palindromes_between_indices(string):
    # Create a set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(1, len(string)):
        # Check if the current character is a letter
        if string[i].isalpha():
            # Get the indices of the current character in the string
            indices = [j for j, char in enumerate(string) if char == string[i]]
            # Loop through each index of the current character
            for j in indices:
                # Check if the current index is between 1 and 6 (inclusive)
                if 1 <= j <= 6:
                    # Get the substring starting from the current index to the end of the string
                    substring = string[j:]
                    # Check if the substring is a palindrome
                    if substring == substring[::-1]:
                        # Add the palindrome to the set
                        palindromes.add(substring)
    # Return the set of palindromes
    return palindromes
