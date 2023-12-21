
def palindrome_of_length_n(string):
    # Convert the string to lowercase for case-insensitive comparison
    string = string.lower()
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate over each substring of length n in the string
    for i in range(len(string) - 1):
        # Check if the substring is a palindrome
        if string[i:i+n] == string[i:i+n][::-1]:
            # Add the palindrome to the set of palindromes
            palindromes.add(string[i:i+n])
    return palindromes
