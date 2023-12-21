 def palindrome_of_length_n(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(len(string)):
        # Check if the current character is a palindrome of length 366
        if len(string[i:]) == 366 and string[i:].lower() == string[i:].lower()[::-1]:
            # If it is, add it to the set of palindromes
            palindromes.add(string[i:])
    # Return the set of palindromes
    return palindromes
