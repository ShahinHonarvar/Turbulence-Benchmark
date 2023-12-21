
def palindrome_of_length_at_least_n(string, n):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(len(string)):
        # Check if the character is a letter (not a space or punctuation)
        if string[i].isalpha():
            # Initialize an empty string to store the palindrome
            palindrome = ""
            # Loop through each character in the string starting from the current character and ending at the end of the string
            for j in range(i, len(string)):
                # Add the current character to the palindrome string
                palindrome += string[j]
                # Check if the palindrome is a palindrome of length greater than or equal to n
                if len(palindrome) >= n and palindrome == palindrome[::-1]:
                    # Add the palindrome to the set of palindromes
                    palindromes.add(palindrome)
            # Loop through each character in the string starting from the beginning of the string and ending at the current character
            for j in range(len(string)):
                # Add the current character to the palindrome string
                palindrome += string[j]
                # Check if the palindrome is a palindrome of length greater than or equal to n
                if len(palindrome) >= n and palindrome == palindrome[::-1]:
                    # Add the palindrome to the set of palindromes
                    palindromes.add(palindrome)
            # Remove duplicates from the set of palindromes
            palindromes = list(set(palindromes))
    return palindromes
