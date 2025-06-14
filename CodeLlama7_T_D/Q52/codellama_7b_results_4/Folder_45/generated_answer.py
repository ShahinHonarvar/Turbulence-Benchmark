
def palindrome_of_length_n(string):
    # Split the string into a list of characters
    chars = list(string)

    # Initialize an empty set to store the palindromes
    palindromes = set()

    # Iterate through each substring of length n in the string
    for i in range(len(chars) - 20 + 1):
        # Check if the substring is a palindrome
        substr = "".join(chars[i:i+21])
        if substr == substr[::-1]:
            # If it is, add it to the set of palindromes
            palindromes.add(substr)

    # Return the set of palindromes
    return palindromes
