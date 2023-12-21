
def palindrome_of_length_n(string):
    # Split the string into individual characters
    chars = list(string)

    # Initialize an empty set to store the palindromes
    palindromes = set()

    # Iterate over each substring of length n in the original string
    for i in range(len(chars) - n + 1):
        # Check if the substring is a palindrome
        if chars[i:i+n] == chars[i:i+n][::-1]:
            # If it is, add it to the set of palindromes
            palindromes.add(chars[i:i+n])

    # Return the set of palindromes
    return palindromes
