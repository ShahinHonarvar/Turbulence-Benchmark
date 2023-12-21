
import re

def palindrome_of_length_n(string):
    # Convert the input string to lowercase
    string = string.lower()
    # Initialize an empty list to store the palindromes
    palindromes = []
    # Iterate over the characters in the input string
    for i in range(len(string)):
        # Check if the current character is a letter
        if re.match("[a-zA-Z]", string[i])):
            # Get the substring of the input string starting at the current character and ending at position n - 1 (where n is the length of the input string)
            sub_string = string[i:i+len(string)]
            # Check if the substring is a palindrome
            if sub_string == sub_string[::-1]:
                # Add the palindrome to the list of palindromes
                palindromes.append(sub_string)
    return set(palindromes)
