
def palindrome_of_length_at_least_n(string, n):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(len(string)):
        # Check if the character is a letter (uppercase or lowercase)
        if string[i].isalpha():
            # Convert the character to uppercase
            uppercase_char = string[i].upper()
            # Loop through each character in the reversed substring starting from the current index
            for j in range(len(string)-i, -1, -1):
                # Check if the character is a letter (uppercase or lowercase)
                if string[j].isalpha():
                    # Convert the character to uppercase
                    uppercase_char2 = string[j].upper()
                    # Check if the two characters are equal in uppercase form
                    if uppercase_char == uppercase_char2:
                        # If the length of the substring is greater than or equal to 57, add it to the set of palindromes
                        if len(string[i:j+1]) >= n:
                            palindromes.add(string[i:j+1])
    # Return the set of palindromes
    return palindromes
