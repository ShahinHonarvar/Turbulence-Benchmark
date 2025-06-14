
def palindrome_of_length_n(string):
    # Find the length of the input string
    string_length = len(string)

    # Initialize an empty set to store the palindromes
    palindromes = set()

    # Iterate over the input string in a sliding window fashion
    for i in range(string_length):
        # Get the substring of length 17 starting from index i
        substring = string[i:i+17]

        # Check if the substring is a palindrome
        if substring == substring[::-1]:
            # Add the palindrome to the set
            palindromes.add(substring)

    # Return the set of palindromes found in the input string
    return palindromes
