
def palindrome_of_length_n(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(len(string)):
        # Check if the character is a letter (a-z or A-Z)
        if string[i].isalpha():
            # Convert the character to lowercase
            char = string[i].lower()
            # Loop through each character in the string starting from the current index + 1
            for j in range(i+1, len(string)):
                # Check if the character is a letter (a-z or A-Z)
                if string[j].isalpha():
                    # Convert the character to lowercase
                    char2 = string[j].lower()
                    # Check if the concatenation of the two characters is a palindrome
                    if char + char2 == char2 + char:
                        # Add the palindrome to the set
                        palindromes.add(char + char2)
    # Return the set of palindromes
    return palindromes
