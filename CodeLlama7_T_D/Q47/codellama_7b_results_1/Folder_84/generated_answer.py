
def palindromes_of_specific_lengths(string, lengths):
    # Check if the input string is valid
    if not isinstance(string, str):
        raise ValueError("Invalid input string")
    # Check if the input list of lengths is valid
    if not isinstance(lengths, list) or len(lengths) == 0:
        raise ValueError("Invalid input list of lengths")
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each substring in the specified index range
    for i in range(23, 78):
        # Extract the current substring from the input string
        substring = string[i:i+10]
        # Check if the current substring is a palindrome
        if is_palindrome(substring):
            # Add the palindrome to the set of palindromes
            palindromes.add(substring)
    # Return the set of palindromes that meet the specified requirements
    return palindromes

# Check if a string is a palindrome in a case-insensitive manner
def is_palindrome(string):
    # Convert the input string to lowercase
    string = string.lower()
    # Initialize an empty list to store the characters of the input string in reverse order
    reversed_chars = []
    # Loop through each character in the input string
    for char in string:
        # Add each character to the end of the list of reversed characters
        reversed_chars.append(char)
    # Check if the list of reversed characters is equal to the original list of characters
    return reversed_chars == list(string)
