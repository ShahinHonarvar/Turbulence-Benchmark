
def palindromes_of_specific_lengths(string):
    # Split the string into substrings of length 12
    substrings = [string[i:i+12] for i in range(len(string)-12+1)]
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate over each substring
    for substring in substrings:
        # Check if the substring is a palindrome
        if substring == substring[::-1]:
            # If it is, add it to the set of palindromes
            palindromes.add(substring)
    # Return the set of palindromes
    return palindromes
