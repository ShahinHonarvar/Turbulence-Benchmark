
def palindrome_of_length_n(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(len(string)):
        # Check if the character is a letter (uppercase or lowercase)
        if string[i].isalpha():
            # Convert the character to lowercase
            char = string[i].lower()
            # Loop through each substring of length n starting at position i in the string
            for j in range(i, len(string) - 2):
                # Check if the substring is a palindrome
                if char == string[j:j+n]:
                    # Add the palindrome to the set
                    palindromes.add(char)
    # Return the set of all palindromes of length n as substrings of the given string
    return palindromes
