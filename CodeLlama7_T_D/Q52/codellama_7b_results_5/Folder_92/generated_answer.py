
def palindrome_of_length_n(string):
    # Define a lambda function to check if a substring is a palindrome
    is_palindrome = lambda substr: substr == substr[::-1]
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate over the length of the string
    for i in range(len(string)):
        # Check if the substring is a palindrome
        if is_palindrome(string[i:i+10]):
            # Add the palindrome to the set
            palindromes.add(string[i:i+10])
    return palindromes
