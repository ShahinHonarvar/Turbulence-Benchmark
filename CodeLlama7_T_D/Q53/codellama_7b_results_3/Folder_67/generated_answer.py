
def palindrome_of_length_at_least_n(string, n):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(len(string)):
        # Check if the current character is a letter (a-z or A-Z)
        if string[i].isalpha():
            # Check if the current character is the same as the last character of the string
            if string[i].lower() == string[-i-1].lower():
                # Initialize an empty string to store the palindrome
                palindrome = ""

                # Add the first half of the palindrome (from the current character to the end of the string) to the palindrome string
                for j in range(i, len(string)):
                    palindrome += string[j]

                # Check if the length of the palindrome is greater than or equal to the required minimum length (n)
                if len(palindrome) >= n:
                    # Add the palindrome to the set of palindromes
                    palindromes.add(palindrome)

            # Check if the current character is the same as the second-to-last character of the string
            elif string[i].lower() == string[-i-2].lower():
                # Initialize an empty string to store the palindrome
                palindrome = ""

                # Add the first half of the palindrome (from the current character to the end of the string) to the palindrome string
                for j in range(i, len(string)):
                    palindrome += string[j]

                # Check if the length of the palindrome is greater than or equal to the required minimum length (n)
                if len(palindrome) >= n:
                    # Add the palindrome to the set of palindromes
                    palindromes.add(palindrome)

    # Return the set of palindromes
    return palindromes
