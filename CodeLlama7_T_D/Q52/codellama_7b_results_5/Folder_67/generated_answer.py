
def palindrome_of_length_n(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(len(string)):
        # Check if the character is a letter (not a digit or a symbol)
        if string[i].isalpha():
            # Create a copy of the string without the first character
            substr = string[i + 1:]
            # Loop through each character in the substring
            for j in range(len(substr)):
                # Check if the substring is a palindrome
                if substr[j:].lower() == substr[j:].lower()[::-1]:
                    # Add the palindrome to the set of palindromes
                    palindromes.add(string[i: i + j + 1])
    return palindromes
