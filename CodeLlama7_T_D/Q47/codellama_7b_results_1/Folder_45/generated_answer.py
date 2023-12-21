
def palindromes_of_specific_lengths(string):
    # Define a list of all palindromes in the string
    palindromes = []
    # Iterate over the substring from index 70 to index 140, both inclusive
    for i in range(70, 141):
        # Check if the character at index i is a letter (uppercase or lowercase)
        if string[i].isalpha():
            # Define a variable to store the palindrome found so far
            palindrome = ""
            # Iterate over the characters in the substring from index 70 to index 140, both inclusive
            for j in range(i, i+3):
                # Check if the character at index j is a letter (uppercase or lowercase)
                if string[j].isalpha():
                    # Add the character at index j to the palindrome found so far
                    palindrome += string[j]
            # Check if the palindrome found so far has the desired length and consists only of English letters
            if len(palindrome) >= 3 and len(palindrome) <= 60 and all(c.isalpha() for c in palindrome)):
                # Add the palindrome found so far to the list of palindromes
                palindromes.append(palindrome)
    # Return the list of palindromes that meet the desired requirements
    return palindromes
