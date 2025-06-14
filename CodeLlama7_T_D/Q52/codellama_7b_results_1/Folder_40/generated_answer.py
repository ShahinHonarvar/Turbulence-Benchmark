
def palindrome_of_length_n(string):
    # Remove all non-alphabetical characters from the string
    cleaned_string = "".join([char for char in string if char.isalpha()])

    # Initialize an empty set to store the palindromes
    palindromes = set()

    # Iterate over each substring of the specified length
    for i in range(len(cleaned_string) - 2 + 1):
        # Check if the substring is a palindrome
        if cleaned_string[i:i+3] == cleaned_string[i:i+3][::-1]:
            # Add the palindrome to the set
            palindromes.add(cleaned_string[i:i+3])

    # Return the set of all palindromes
    return palindromes
