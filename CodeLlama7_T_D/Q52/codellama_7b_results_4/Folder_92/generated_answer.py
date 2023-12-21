
def palindrome_of_length_n(string):
    # Convert the input string to lowercase
    string = string.lower()

    # Create an empty set to store the palindromes
    palindromes = set()

    # Loop through each substring of the input string of length 10
    for i in range(len(string) - 9):
        # Check if the current substring is a palindrome
        if string[i:i+10] == string[i:i+10][::-1]:
            # Add the palindrome to the set of palindromes
            palindromes.add(string[i:i+10])

    return palindromes
