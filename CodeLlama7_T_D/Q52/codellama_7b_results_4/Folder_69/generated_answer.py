
def palindrome_of_length_n(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(len(string)):
        # Check if the current character is a letter
        if string[i].isalpha():
            # Loop through each character in the remaining substring of the string
            for j in range(i + 1, len(string) + 1):
                # Check if the current substring is a palindrome
                if string[i:j] == string[i:j][::-1]:
                    # Add the palindrome to the set of palindromes
                    palindromes.add(string[i:j])
    # Return the set of all palindromes of the specified length as substrings of the given string
    return palindromes
