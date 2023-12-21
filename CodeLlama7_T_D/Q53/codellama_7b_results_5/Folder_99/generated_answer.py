 def palindrome_of_length_at_least_n(string, n):
    # Create a set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(len(string)):
        # Check if the character is an English letter
        if string[i].isalpha():
            # Loop through each character in the reversed substring starting at index i
            for j in range(i, len(string)):
                # Check if the character is an English letter
                if string[j].isalpha():
                    # Create a substring of length 2 starting at index i and ending at index j
                    substring = string[i:j+1]
                    # Check if the substring is a palindrome
                    if substring == substring[::-1]:
                        # Add the substring to the set of palindromes
                        palindromes.add(substring)
    # Return the set of palindromes
    return palindromes
