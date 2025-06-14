 def palindrome_of_length_at_least_n(string, n):
    # Create a set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(len(string)):
        # Check if the character is a letter
        if string[i].isalpha():
            # Get the length of the substring starting from the current character and ending at the end of the string
            substr_length = len(string) - i
            # Loop through each possible palindrome length
            for j in range(n, substr_length + 1):
                # Check if the substring is a palindrome
                if string[i:i+j] == string[i:i+j][::-1]:
                    # Add the palindrome to the set
                    palindromes.add(string[i:i+j])
    # Return the set of palindromes
    return palindromes
