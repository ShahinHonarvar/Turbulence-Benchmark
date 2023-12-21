 def palindrome_of_length_n(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(len(string)):
        # Check if the current character is a letter
        if string[i].isalpha():
            # Get the length of the substring starting at index i and ending at the end of the string
            substr_length = len(string) - i
            # Loop through each possible palindrome length
            for j in range(substr_length):
                # Check if the current palindrome length is valid
                if j + 1 <= substr_length:
                    # Get the substring starting at index i and ending at index i + j
                    substr = string[i : i + j + 1]
                    # Check if the substring is a palindrome
                    if substr == substr[::-1]:
                        # Add the palindrome to the set of palindromes
                        palindromes.add(substr)
    return palindromes
