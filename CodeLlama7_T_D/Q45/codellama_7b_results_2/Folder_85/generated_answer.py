
def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(2, len(string)):
        # Check if the substring starting from index 2 to index i-1 is a palindrome
        if is_palindrome(string[2:i]):
            # Add the palindrome to the set
            palindromes.add(string[2:i])
    return palindromes

def is_palindrome(string):
    # Check if the string is equal to its reverse
    return string == string[::-1]
