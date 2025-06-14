
def palindrome_of_length_n(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(len(string)):
        # Check if the character is a letter (uppercase or lowercase)
        if string[i].isalpha():
            # Convert the character to uppercase
            char_upper = string[i].upper()
            # Loop through each character in the string starting from the current index + 1
            for j in range(i + 1, len(string)):
                # Check if the character is a letter (uppercase or lowercase)
                if string[j].isalpha():
                    # Convert the character to uppercase
                    char_lower = string[j].upper()
                    # If the current character and the previous character are the same, add the palindrome to the set
                    if char_upper == char_lower:
                        palindromes.add(string[i:j + 1])
    return palindromes
