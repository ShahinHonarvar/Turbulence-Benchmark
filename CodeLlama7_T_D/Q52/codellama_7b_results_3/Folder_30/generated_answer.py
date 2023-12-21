
def palindrome_of_length_n(string):
    # Remove non-alphanumeric characters from the string
    cleaned_string = ''.join([c for c in string if c.isalpha()])
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate over the length of the cleaned string
    for i in range(len(cleaned_string)):
        # Check if the substring is a palindrome
        if cleaned_string[i:] == cleaned_string[i:][::-1]:
            # Add the palindrome to the set
            palindromes.add(cleaned_string[i:])
    return palindromes
