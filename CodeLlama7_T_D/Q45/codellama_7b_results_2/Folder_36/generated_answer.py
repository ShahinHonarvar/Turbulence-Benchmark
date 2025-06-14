
def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(5, len(string)):
        # Check if the substring from indices 5 to i is a palindrome
        if string[5:i+1] == string[5:i+1][::-1]:
            # Add the palindrome to the set
            palindromes.add(string[5:i+1])
    return palindromes
