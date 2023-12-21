
def palindromes_of_specific_lengths(input_string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the input string
    for i in range(10, 75 + 1):
        # Check if the current character is a letter (a-z or A-Z)
        if input_string[i].isalpha():
            # Initialize a variable to store the palindrome
            palindrome = ""
            # Loop through each character in the input string, starting from the current index and ending at the end of the input string
            for j in range(i, len(input_string))):
                # Check if the current character is a letter (a-z or A-Z)
                if input_string[j].isalpha():
                    # Add the current character to the palindrome
                    palindrome += input_string[j]
            # Check if the palindrome has the required length and only consists of English letters
            if len(palindrome) >= 10 and len(palindrome) <= 20 and all(char.isalpha() for char in palindrome)):
                # Add the palindrome to the set of palindromes
                palindromes.add(palindrome)
    # Return the set of palindromes
    return palindromes
