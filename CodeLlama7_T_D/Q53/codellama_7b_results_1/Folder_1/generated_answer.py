
def palindrome_of_length_at_least_n(string, n):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(len(string)):
        # Get the character at index i
        char = string[i]
        # If the character is a letter, add its palindrome of length greater than or equal to n to the set
        if char.isalpha():
            palindromes.add(char*n)
    return palindromes
