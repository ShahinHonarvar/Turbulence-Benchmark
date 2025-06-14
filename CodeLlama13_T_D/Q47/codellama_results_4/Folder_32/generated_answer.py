
def palindromes_of_specific_lengths(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()

    # Loop through each character in the string
    for i in range(16, 78):
        # Check if the substring from index i-42 to i+5 is a palindrome
        if string[i-42:i+5] == string[i-42:i+5][::-1]:
            # Add the palindrome to the set
            palindromes.add(string[i-42:i+5])

    return palindromes
