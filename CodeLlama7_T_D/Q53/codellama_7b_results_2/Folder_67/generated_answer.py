
def palindrome_of_length_at_least_n(string, n):
    # Convert the input string to lowercase
    string = string.lower()
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the input string
    for i in range(len(string)):
        # Check if the current character is a letter
        if string[i].isalpha():
            # Loop through each character in the rest of the input string
            for j in range(i + 1, len(string) + 1):
                # Check if the substring starting at the current character and ending at the next character is a palindrome
                if string[i:j] == string[i:j][::-1]:
                    # Add the palindrome to the set of palindromes
                    palindromes.add(string[i:j])
    # Return the set of palindromes
    return palindromes
