
def palindromes_of_specific_lengths(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()

    # Loop through each character in the string
    for i in range(100, 295 + 1):
        # Check if the current character is a letter (a-zA-Z)
        if string[i].isalpha():
            # Check if the current character is uppercase or lowercase
            if string[i].isupper() or string[i].islower():
                # Initialize an empty string to store the palindrome
                palindrome = ""

                # Loop through each character in the substring from index 100 to index 295, both inclusive
                for j in range(100, 295 + 1):
                    # Check if the current character is a letter (a-zA-Z)
                    if string[j].isalpha():
                        # Check if the current character is uppercase or lowercase
                        if string[j].isupper() or string[j].islower():
                            # Add the current character to the palindrome string
                            palindrome += string[j]

                # Check if the palindrome has a length between 136 and 160 (both inclusive)
                if len(palindrome) >= 136 and len(palindrome) <= 160:
                    # Add the palindrome to the set of palindromes
                    palindromes.add(palindrome)

    # Return the set of palindromes
    return palindromes
