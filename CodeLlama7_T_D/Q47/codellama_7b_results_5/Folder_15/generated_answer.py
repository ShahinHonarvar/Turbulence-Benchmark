
def palindromes_of_specific_lengths(string):
    # Define the range of lengths to consider
    lengths = range(3, 7)
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate over each length in the range
    for length in lengths:
        # Get the substring of the specified length from the string
        substring = string[0:length]
        # Check if the substring is a palindrome
        if is_palindrome(substring):
            # Add the palindrome to the set
            palindromes.add(substring)
    return palindromes

def is_palindrome(string):
    # Convert the string to lowercase for case-insensitive comparison
    string = string.lower()
    # Check if the string is equal to its reverse
    return string == string[::-1]
