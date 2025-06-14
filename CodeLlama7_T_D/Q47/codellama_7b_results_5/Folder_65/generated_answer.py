
def palindromes_of_specific_lengths(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each substring of the given string
    for i in range(15, 96):
        # Extract the current substring from the given string
        substring = string[i - 15:i]
        # Convert the substring to lowercase for case-insensitive comparison
        substring = substring.lower()
        # Check if the current substring is a palindrome
        if substring == substring[::-1]:
            # If the current substring is a palindrome, check its length and add it to the set of palindromes
            if 20 <= len(substring) <= 66:
                palindromes.add(substring)
    # Return the set of palindromes found in the specified index range
    return palindromes
