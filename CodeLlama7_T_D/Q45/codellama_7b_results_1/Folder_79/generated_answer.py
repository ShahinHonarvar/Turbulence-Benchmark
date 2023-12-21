
def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each possible length of palindrome
    for length in range(3, len(string) + 1):
        # Loop through each possible starting index of the palindrome
        for start_index in range(len(string) - length + 1):
            # Initialize an empty string to store the palindrome
            palindrome = ""
            # Loop through each character in the palindrome
            for i in range(length):
                # Add the character to the end of the palindrome
                palindrome += string[start_index + i]
            # If the palindrome is at least 3 characters long and is a valid palindrome, add it to the set of palindromes
            if length >= 3 and palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    # Return the set of palindromes
    return palindromes
