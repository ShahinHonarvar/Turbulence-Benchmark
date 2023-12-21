
def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(len(string) - 1)):
        # Check if the current character is a letter
        if string[i].isalpha():
            # Check if the next character is also a letter
            if string[i + 1].isalpha():
                # Create a palindrome by reversing the order of the letters
                palindrome = string[i + 1] + string[i]
                # Add the palindrome to the set of palindromes
                palindromes.add(palindrome)
    return palindromes
