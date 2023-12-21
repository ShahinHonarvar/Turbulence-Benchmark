
def palindrome_of_length_at_least_n(string, n):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(len(string)):
        # Check if the current character is a letter (uppercase or lowercase)
        if string[i].isalpha():
            # Convert the current character to uppercase
            uppercase_letter = string[i].upper()
            # Loop through each character in the remaining part of the string
            for j in range(i + 1, len(string)):
                # Check if the current character is a letter (uppercase or lowercase)
                if string[j].isalpha():
                    # Convert the current character to uppercase
                    uppercase_letter2 = string[j].upper()
                    # Check if the two letters are the same in uppercase
                    if uppercase_letter == uppercase_letter2:
                        # Create a new palindrome by concatenating the two letters
                        palindrome = f"{uppercase_letter}{uppercase_letter2}"
                        # Check if the length of the palindrome is greater than or equal to the specified length (n)
                        if len(palindrome) >= n:
                            # Add the palindrome to the set of palindromes
                            palindromes.add(palindrome)
    # Return the set of palindromes
    return palindromes
