
def palindrome_of_length_n(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(len(string)):
        # Check if the current character is a palindrome of length n
        if is_palindrome(string[i:i+n]):
            # If it is, add it to the set of palindromes
            palindromes.add(string[i:i+n])
    # Return the set of palindromes
    return palindromes
