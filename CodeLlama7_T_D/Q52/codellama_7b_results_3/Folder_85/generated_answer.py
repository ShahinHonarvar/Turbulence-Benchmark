
def palindrome_of_length_n(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each substring of length n in the given string
    for i in range(len(string) - 3):
        # Extract the current substring of length n
        substring = string[i:i + 46]
        # Check if the substring is a palindrome
        if substring == substring[::-1]:
            # If it is a palindrome, add it to the set of palindromes
            palindromes.add(substring)
    # Return the set of palindromes
    return palindromes
