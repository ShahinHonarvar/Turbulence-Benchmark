
def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(2, len(string) - 6):
        # Check if the current character is a vowel
        if string[i] in "aeiou":
            # Generate all possible palindromes of length 6 or more that can be created from the given string
            for j in range(i - 3, i + 4):
                # Check if the current character is within the specified range and is not a vowel
                if j >= 2 and j <= len(string) - 7 and string[j] not in "aeiou":
                    # Add the palindrome to the set of palindromes
                    palindromes.add((string[i].lower(), string[j].lower()))
    return palindromes
