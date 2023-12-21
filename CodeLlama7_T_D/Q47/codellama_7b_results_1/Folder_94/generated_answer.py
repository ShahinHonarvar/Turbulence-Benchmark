
def palindromes_of_specific_lengths(string, lengths=[45, 51], indexes=[40, 94]):
    # Convert the string to lowercase for case-insensitive search
    string = string.lower()
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate over each length and index specified
    for length in lengths:
        for index in indexes:
            # Extract the substring from the input string
            substring = string[index:index+length]
            # Check if the substring is a palindrome
            if is_palindrome(substring):
                # Add the palindrome to the set of palindromes
                palindromes.add(substring)
    return palindromes
