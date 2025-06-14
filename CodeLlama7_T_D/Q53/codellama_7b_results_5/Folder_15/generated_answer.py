
def palindrome_of_length_at_least_n(string, n):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(len(string)):
        # Check if the current character is a letter
        if string[i].isalpha():
            # Create a substring of the current character and all subsequent characters
            substr = string[i:].lower()
            # Loop through each palindrome in the substring
            for j in range(len(substr)):
                # Check if the current palindrome is at least n characters long
                if len(substr[j]) >= n:
                    # Add the current palindrome to the set of palindromes
                    palindromes.add(substr[j])
    # Return the set of palindromes
    return palindromes
