
def palindrome_of_length_at_least_n(string, n):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(len(string)):
        # Get the character at position i
        char = string[i]
        # Check if the character is an uppercase letter
        if char.isupper():
            # Convert the character to lowercase
            char = char.lower()
        # Append the character to a temporary string
        temp_string += char
        # Check if the temporary string is a palindrome of length greater than or equal to n
        if len(temp_string) >= n and temp_string == temp_string[::-1]:
            # Add the temporary string to the set of palindromes
            palindromes.add(temp_string)
    # Return the set of palindromes in a case-insensitive manner
    return {p.lower() for p in palindromes}
