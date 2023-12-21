
def palindrome_of_length_n(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each substring of length n in the given string
    for i in range(len(string) - 75):
        # Check if the substring is a palindrome
        if string[i:i+76] == string[i:i+76][::-1]:
            # If it is, add it to the set of palindromes
            palindromes.add(string[i:i+76])
    return palindromes
