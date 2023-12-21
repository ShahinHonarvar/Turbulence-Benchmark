
def palindrome_of_length_n(string):
    # Split the string into individual characters
    characters = list(string)

    # Create a set to store all palindromes of length n
    palindromes = set()

    # Iterate over each substring of length n in the string
    for i in range(len(characters) - 1):
        # Check if the current substring is a palindrome
        if characters[i:i+n] == characters[i:i+n][::-1]:
            # Add the palindrome to the set of palindromes
            palindromes.add(characters[i:i+n])

    # Return the set of all palindromes of length n found in the string
    return palindromes
