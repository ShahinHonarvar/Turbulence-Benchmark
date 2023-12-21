
def palindromes_of_specific_lengths(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(len(string)):
        # Check if the current character is a letter (a-zA-Z)
        if string[i].isalpha():
            # Initialize an empty string to store the palindrome
            palindrome = ""
            # Loop through each character in the substring from index 0 to index 6, both inclusive
            for j in range(max(i - 3, 0), min(i + 4, len(string)))):
                # Check if the current character is a letter (a-zA-Z)
                if string[j].isalpha():
                    # Add the current character to the palindrome string
                    palindrome += string[j]
            # Check if the palindrome string has the length specified and only consists of English letters
            if len(palindrome) >= 3 and len(palindrome) <= 6 and all(c.isalpha() for c in palindrome)):
                # Add the palindrome to the set of palindromes
                palindromes.add(palindrome)
    # Return the set of palindromes
    return palindromes
