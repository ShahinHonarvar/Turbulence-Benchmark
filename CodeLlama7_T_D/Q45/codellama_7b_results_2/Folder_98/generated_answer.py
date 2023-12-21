
def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate over each substring of length 4 or more in the given string
    for i in range(len(string) - 3 + 1):
        # Extract the substring and convert it to lowercase
        substring = string[i:i+4].lower()
        # Check if the substring is a palindrome
        if substring == substring[::-1]:
            # If the substring is a palindrome, add it to the set of palindromes
            palindromes.add(substring)
    # Return the set of palindromes
    return palindromes
