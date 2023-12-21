
def palindrome_of_length_n(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each substring of length n in the given string
    for i in range(len(string) - 180):
        # Check if the substring is a palindrome in a case-insensitive manner
        if string[i:i+181].lower() == string[i:i+181][::-1].lower():
            # Add the palindrome to the set of palindromes
            palindromes.add(string[i:i+181])
    # Return the set of palindromes
    return palindromes
