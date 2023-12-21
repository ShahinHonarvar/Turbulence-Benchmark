 def palindromes_of_specific_lengths(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the specified index range
    for i in range(63, 71):
        # Check if the current character is a letter (uppercase or lowercase)
        if string[i].isalpha():
            # Initialize an empty string to store the palindrome
            palindrome = ""
            # Loop through each character in the range from the current character to the end of the string
            for j in range(i, len(string)):
                # Add the current character to the palindrome string
                palindrome += string[j]
                # Check if the palindrome is a valid palindrome with the specified length
                if len(palindrome) >= 4 and len(palindrome) <= 5:
                    # Convert the palindrome to lowercase
                    palindrome = palindrome.lower()
                    # Check if the palindrome is a palindrome in a case-insensitive manner
                    if palindrome == palindrome[::-1]:
                        # Add the palindrome to the set of palindromes
                        palindromes.add(palindrome)
    # Return the set of palindromes
    return palindromes
