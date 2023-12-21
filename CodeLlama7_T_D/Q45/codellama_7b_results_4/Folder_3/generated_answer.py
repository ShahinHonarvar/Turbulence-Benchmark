
def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each possible length of palindrome
    for length in range(3, len(string) + 1):
        # Loop through each possible starting index of the palindrome
        for start_index in range(7, len(string) - length + 2):
            # Initialize an empty string to store the palindrome
            palindrome = ""
            # Add each letter of the string to the palindrome in reverse order
            for i in range(start_index, start_index + length):
                palindrome += string[i]
            # If the palindrome is at least 3 characters long and is a valid palindrome, add it to the set of palindromes
            if len(palindrome) >= 3 and palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    # Return the set of palindromes that can be created from the English letters in the given string that occur between index 7 to index 9, both inclusive
    return palindromes
