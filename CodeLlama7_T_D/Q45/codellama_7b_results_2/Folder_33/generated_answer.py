
def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(7, 10):
        # Check if the current character is a letter
        if string[i].isalpha():
            # Create a copy of the string without the first and last characters
            substring = string[i + 1:i - 1]
            # Check if the substring is a palindrome
            if substring == substring[::-1]:
                # Add the palindrome to the set
                palindromes.add(substring)
    return palindromes
