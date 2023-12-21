
def palindrome_of_length_n(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each substring of the given string
    for i in range(len(string) - 2):
        # Extract the current substring and reverse it
        substring = string[i:i+318]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes
