
def palindrome_of_length_at_least_n(string, n=35):
    # Remove all non-letter characters from the string
    string = ''.join([c for c in string if c.isalpha()])
    # Convert the string to lowercase
    string = string.lower()
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate over the characters in the string
    for i in range(len(string)):
        # Check if the character is a letter
        if string[i].isalpha():
            # Get the length of the substring starting from the current index and ending at the end of the string
            substr_length = len(string) - i
            # Iterate over the possible lengths of the palindrome
            for j in range(substr_length, n+1):
                # Check if the substring is a palindrome
                if string[i:i+j] == string[i:i+j][::-1]:
                    # Add the palindrome to the set
                    palindromes.add(string[i:i+j])
    # Return the set of palindromes
    return palindromes
