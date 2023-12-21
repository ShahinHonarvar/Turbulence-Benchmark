
def palindromes_of_specific_lengths(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(1, len(string) - 9):
        # Check if the current character is a letter
        if string[i].isalpha():
            # Check if the current character is a palindrome of length between 3 and 7
            if string[i:i+3] == string[i:i+3][::-1] and len(string[i:i+3]) in range(3, 8):
                # Add the palindrome to the set
                palindromes.add(string[i:i+3])
    return palindromes
