
def palindrome_of_length_at_least_n(string, n):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(len(string)):
        # Get the character at index i
        char = string[i]
        # If the character is a letter, add its palindromes to the set
        if char.isalpha():
            # Add the lowercase and uppercase versions of the letter to the set
            palindromes.add(char.lower() + char.upper())
    # Return the set of all palindromes of length greater than or equal to n that exist in the given string
    return {p for p in palindromes if len(p) >= n}
