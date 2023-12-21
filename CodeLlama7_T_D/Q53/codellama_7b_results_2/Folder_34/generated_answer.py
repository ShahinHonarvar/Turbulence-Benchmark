
def palindrome_of_length_at_least_n(string, n):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(len(string)):
        # Check if the current character is a letter (a-z or A-Z)
        if string[i].isalpha():
            # Convert the current character to lowercase
            c = string[i].lower()
            # Loop through each character in the remaining part of the string
            for j in range(i + 1, len(string)):
                # Check if the current character is a letter (a-z or A-Z)
                if string[j].isalpha():
                    # Convert the current character to lowercase
                    d = string[j].lower()
                    # Check if the current character and the previous character are equal
                    if c == d:
                        # Add the palindrome to the set of palindromes
                        palindromes.add(c + d)
    # Return the set of palindromes
    return palindromes
