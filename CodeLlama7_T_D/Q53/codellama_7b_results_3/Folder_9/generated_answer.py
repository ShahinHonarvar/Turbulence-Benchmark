
def palindrome_of_length_at_least_n(string, n):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(len(string)):
        # Get the character at index i
        char = string[i]
        # If the character is a letter, check if it forms a palindrome of length greater than or equal to n
        if char.isalpha():
            substr = string[i:].lower()
            for j in range(len(substr) - n + 1):
                substr_j = substr[j:j + n]
                # If the substring forms a palindrome, add it to the set of palindromes
                if substr_j == substr_j[::-1]:
                    palindromes.add(substr_j)
    # Return the set of palindromes
    return palindromes
