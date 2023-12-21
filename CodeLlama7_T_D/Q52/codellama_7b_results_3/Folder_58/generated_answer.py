
def palindrome_of_length_n(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()

    # Loop through each substring of length n in the given string
    for i in range(len(string) - n + 1):
        # Check if the substring is a palindrome in a case-insensitive manner
        if string[i:i+n].lower() == string[i:i+n].lower()[::-1]:
            # If it is, add it to the set of palindromes
            palindromes.add(string[i:i+n])

    # Return the set of palindromes
    return palindromes
