
def palindrome_of_length_at_least_n(string, n):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(len(string)):
        # Check if the current character is a letter
        if string[i].isalpha():
            # Get the index of the last character in the substring starting at 'i' and ending at 'i + n - 1'
            last_index = min(len(string) - 1, i + n - 1)
            # Loop through each substring of length 'n' starting at 'i' and ending at 'last_index'
            for j in range(i, last_index + 1):
                # Check if the current substring is a palindrome
                if string[j].isalpha() and string[j].lower() == string[j].upper():
                    # Add the palindrome to the set of palindromes
                    palindromes.add(string[i:j + 1])
    # Return the set of palindromes
    return palindromes
