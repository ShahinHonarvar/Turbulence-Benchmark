
def palindromes_of_specific_lengths(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()

    # Iterate over the string from index 11 to index 83, both inclusive
    for i in range(11, 84):
        # Get the substring starting from index i and ending at index i + 60 (both inclusive)
        substring = string[i:i+60]

        # Check if the substring is a palindrome
        if substring == substring[::-1]:
            # Add the palindrome to the set if it meets the length requirements
            if 37 <= len(substring) <= 60:
                palindromes.add(substring)

    return palindromes
