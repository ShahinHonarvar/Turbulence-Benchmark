
def palindrome_of_length_at_least_n(string, n):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(len(string)):
        # Get the character at position i in the string
        char = string[i]
        # Check if the character is an English letter
        if char.isalpha():
            # Convert the character to uppercase
            char_upper = char.upper()
            # Loop through each character in the string from position i+1 to the end
            for j in range(i+1, len(string)):
                # Get the character at position j in the string
                char2 = string[j]
                # Check if the character is an English letter
                if char2.isalpha():
                    # Convert the character to uppercase
                    char2_upper = char2.upper()
                    # Check if the characters at positions i and j are the same in uppercase
                    if char_upper == char2_upper:
                        # Check if the length of the palindrome is greater than or equal to n
                        if len(string[i:j+1]) >= n:
                            # Add the palindrome to the set of palindromes
                            palindromes.add(string[i:j+1])
    # Return the set of palindromes
    return palindromes
