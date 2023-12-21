
def palindrome_of_length_at_least_n(string, n):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(len(string)):
        # Check if the character is a letter (not a space or other character)
        if string[i].isalpha():
            # Get the index of the last character in the substring starting at position i and of length n
            last_index = len(string) - 1 - (len(string) - 1) % 2
            # Check if the substring starting at position i and of length n is a palindrome
            if string[i:last_index + 1] == string[i:last_index + 1][::-1]:
                # Add the palindrome to the set of palindromes
                palindromes.add(string[i:last_index + 1])
    # Return the set of palindromes
    return palindromes
