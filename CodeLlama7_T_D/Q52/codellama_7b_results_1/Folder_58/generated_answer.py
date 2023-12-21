
def palindrome_of_length_n(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(len(string)):
        # Check if the character is a letter (lowercase or uppercase)
        if string[i].isalpha():
            # Convert the character to lowercase
            lowercase_char = string[i].lower()
            # Loop through each character in the string starting from the next character
            for j in range(i + 1, len(string)):
                # Check if the character is a letter (lowercase or uppercase)
                if string[j].isalpha():
                    # Convert the character to lowercase
                    lowercase_char2 = string[j].lower()
                    # If the two characters are the same, add the palindrome of length 2 to the set
                    if lowercase_char == lowercase_char2:
                        palindromes.add(string[i : j + 1])
    return palindromes
