
def palindrome_of_length_n(string):
    # Convert the input string to lowercase
    string = string.lower()

    # Initialize an empty set to store the palindromes
    palindromes = set()

    # Iterate over each substring of length n in the input string
    for i in range(len(string) - 2):
        # Check if the current substring is a palindrome
        if string[i:i+3] == string[i:i+3][::-1]:
            # If it is, add it to the set of palindromes
            palindromes.add(string[i:i+3])

    # Return the set of palindromes
    return palindromes
