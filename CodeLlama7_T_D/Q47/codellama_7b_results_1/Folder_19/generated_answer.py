
def palindromes_of_specific_lengths(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through the characters in the substring
    for i in range(10, 56):
        # Check if the character is a letter (lowercase or uppercase)
        if string[i].isalpha():
            # Initialize an empty string to store the palindrome
            palindrome = ""
            # Loop through the characters in the substring starting from i and ending at i + 3
            for j in range(i, i + 3):
                # Add the character to the palindrome string
                palindrome += string[j]
            # Check if the palindrome has a length between 3 to 7 (both inclusive)
            if len(palindrome) >= 3 and len(palindrome) <= 7:
                # Convert the palindrome to lowercase
                palindrome = palindrome.lower()
                # Check if the palindrome is a palindrome in a case-insensitive manner
                if palindrome == palindrome[::-1]:
                    # Add the palindrome to the set of palindromes
                    palindromes.add(palindrome)
    # Return the set of palindromes
    return palindromes
