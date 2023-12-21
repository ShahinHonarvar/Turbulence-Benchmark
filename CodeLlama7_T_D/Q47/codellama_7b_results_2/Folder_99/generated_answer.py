
def palindromes_of_specific_lengths(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(127, 289):
        # Check if the current character is a letter
        if string[i].isalpha():
            # Initialize an empty string to store the palindrome
            palindrome = ""
            # Loop through each character in the substring from index i to index i + 141
            for j in range(i, i + 141):
                # Check if the current character is a letter
                if string[j].isalpha():
                    # Add the current character to the palindrome string
                    palindrome += string[j]
            # Check if the palindrome has the desired length and consists only of English letters
            if len(palindrome) in range(119, 142) and palindrome.isalpha():
                # Add the palindrome to the set of palindromes
                palindromes.add(palindrome)
    # Return the set of palindromes
    return palindromes
