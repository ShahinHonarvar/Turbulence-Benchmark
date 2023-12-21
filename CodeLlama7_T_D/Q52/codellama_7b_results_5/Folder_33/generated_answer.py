
def palindrome_of_length_n(string):
    # Convert the string to lowercase
    string = string.lower()
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate over the length of the string
    for i in range(len(string)):
        # Check if the substring starting at position i has a length equal to n
        if len(string[i:]) == n:
            # Add the substring to the set of palindromes
            palindromes.add(string[i:])
    return palindromes
