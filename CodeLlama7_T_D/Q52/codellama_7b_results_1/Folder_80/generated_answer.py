
def palindrome_of_length_n(string):
    # Convert the string to lowercase for case-insensitive matching
    string = string.lower()

    # Initialize an empty set to store the palindromes

    palindromes = set()

    # Iterate through each substring of the given string

    for i in range(len(string) - 276 + 1):

        # Check if the current substring is a palindrome

        sub_str = string[i:i+276]

        if sub_str == sub_str[::-1]:

            # If it is, add it to the set of palindromes

            palindromes.add(sub_str)

    # Return the set of palindromes

    return palindromes
