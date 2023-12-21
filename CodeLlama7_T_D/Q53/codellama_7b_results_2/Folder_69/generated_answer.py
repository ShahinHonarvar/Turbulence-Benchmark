
def palindrome_of_length_at_least_n(string, n):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(len(string)):
        # Get the substring starting from the current character and extending to the end of the string
        substr = string[i:]
        # Check if the substring is a palindrome
        if is_palindrome(substr):
            # Add the palindrome to the set
            palindromes.add(substr)
    # Return the set of palindromes
    return palindromes

def is_palindrome(string):
    # Check if the string is a palindrome by comparing it to its reverse
    return string == string[::-1]
