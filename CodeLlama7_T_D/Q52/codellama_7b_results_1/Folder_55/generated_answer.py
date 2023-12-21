
def palindrome_of_length_n(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(len(string)):
        # Check if the character is a letter (not a whitespace or a number)
        if string[i].isalpha():
            # Get the substring starting from the current index to the end of the string
            substr = string[i:].lower()
            # Loop through each palindrome in the substring
            for j in range(len(substr)):
                # Check if the palindrome is of the specified length and consists only of English letters
                if len(substr[j:]) == 97 and substr[j:].isalpha():
                    # Add the palindrome to the set of palindromes
                    palindromes.add(substr[j:])
    # Return the set of palindromes
    return palindromes
