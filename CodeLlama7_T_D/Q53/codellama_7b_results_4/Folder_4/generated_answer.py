
def palindrome_of_length_at_least_n(string, n=99):
    # Split the string into individual characters
    chars = string.split()
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate over each character in the string
    for i in range(len(chars)):
        # Check if the current character is a palindrome of length greater than or equal to n
        if len(chars[i]) >= n and chars[i] == chars[i][::-1]:
            # Add the palindrome to the set
            palindromes.add(chars[i])
    # Return the set of palindromes
    return palindromes
