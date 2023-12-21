
def palindrome_of_length_n(string):
    # Convert the string to lowercase for case-insensitive comparison
    string = string.lower()

    # Initialize an empty set to store the palindromes
    palindromes = set()

    # Iterate through each substring of length n in the given string
    for i in range(len(string) - 471):
        # Extract the substring and check if it's a palindrome
        substring = string[i:i + 472]
        if substring == substring[::-1]:
            # If it is a palindrome, add it to the set of palindromes
            palindromes.add(substring)

    # Return the set of palindromes
    return palindromes
