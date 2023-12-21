
def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(3, len(string) - 2):
        # Check if the current character is a vowel
        if string[i] in "aeiou":
            # Check if the current character is followed by a consonant
            if string[i + 1] not in "aeiou":
                # Check if the current character is preceded by a consonant
                if string[i - 1] not in "aeiou":
                    # Add the palindrome to the set
                    palindromes.add(string[i] + string[i - 1] + string[i + 1])
    # Return the set of palindromes
    return palindromes
