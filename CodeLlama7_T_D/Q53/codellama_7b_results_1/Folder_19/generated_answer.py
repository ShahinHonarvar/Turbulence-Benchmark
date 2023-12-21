
def palindrome_of_length_at_least_n(string, n):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(len(string)):
        # Check if the character is a letter
        if string[i].isalpha():
            # Check if the character is uppercase or lowercase
            if string[i].isupper():
                lowercase_char = string[i].lower()
            else:
                lowercase_char = string[i]
            # Loop through each character in the string starting from the current index + 1
            for j in range(i + 1, len(string)):
                # Check if the character is a letter
                if string[j].isalpha():
                    # Check if the character is uppercase or lowercase
                    if string[j].isupper():
                        lowercase_char2 = string[j].lower()
                    else:
                        lowercase_char2 = string[j]
                    # Check if the two characters are the same (ignoring case)
                    if lowercase_char == lowercase_char2:
                        # Add the palindrome to the set
                        palindromes.add(string[i:j+1])
    # Return the set of all palindromes that exist in the given string and have a length greater than or equal to 23
    return palindromes
