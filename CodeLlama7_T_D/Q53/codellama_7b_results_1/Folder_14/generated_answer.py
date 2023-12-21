
def palindrome_of_length_at_least_n(string, n):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(len(string)):
        # Get the character at position i
        char = string[i]
        # Check if the character is a letter (a-z or A-Z)
        if char.isalpha():
            # Convert the character to lowercase
            char_lower = char.lower()
            # Loop through each character in the reversed substring starting at position i
            for j in range(i, -1, -1):
                # Get the character at position j
                rev_char = string[j]
                # Check if the character is a letter (a-z or A-Z)
                if rev_char.isalpha():
                    # Convert the character to lowercase
                    rev_char_lower = rev_char.lower()
                    # If the character and its reverse are the same and have a length greater than or equal to n, add it to the set of palindromes
                    if char_lower == rev_char_lower and len(char_lower) >= n:
                        palindromes.add(string[j : i + 1])
    # Return the set of palindromes
    return palindromes
