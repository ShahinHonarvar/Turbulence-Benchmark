
def palindrome_of_length_at_least_n(string, n):
    # Convert the input string to lowercase
    string = string.lower()
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate over each character in the input string
    for i in range(len(string)):
        # Check if the current character is a letter
        if string[i].isalpha():
            # Check if the current character is the same as the previous or next character
            if (i > 0 and string[i] == string[i - 1]) or (i < len(string) - 1 and string[i] == string[i + 1])):
                # If the current character is the same as the previous or next character, add it to the palindromes set
                palindromes.add(string[i])
    # Return the palindromes set
    return palindromes
