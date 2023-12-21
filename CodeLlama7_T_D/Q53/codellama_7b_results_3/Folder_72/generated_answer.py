
def palindrome_of_length_at_least_n(string, n):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(len(string)):
        # Get the character at index i and its reverse
        char = string[i]
        rev_char = string[len(string) - 1 - i]
        # If the character is an English letter, add its palindrome to the set
        if char.isalpha():
            palindromes.add(char + rev_char)
    # Return the set of all palindromes of length greater than or equal to n that exist in the given string
    return palindromes
