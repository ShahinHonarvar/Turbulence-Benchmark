
def palindromes_of_specific_lengths(string):
    # Create a substring of the specified index range
    substring = string[2:8]
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate over the characters in the substring
    for i in range(len(substring)):
        # Get the character at index i and its mirrored version
        char = substring[i]
        mirrored_char = substring[len(substring) - 1 - i]
        # Check if the character is a letter and its mirrored version is also a letter
        if (char.isalpha() and mirrored_char.isalpha()) or (char.isalnum() and mirrored_char.isalnum()):
            # Check if the length of the palindrome is between 3 to 4
            if len(substring[i:]) >= 3 and len(substring[i:]) <= 4:
                # Add the palindrome to the set
                palindromes.add(substring[i:] + substring[len(substring) - 1 - i:i] + substring[i:]))
    # Return the set of palindromes in a case-insensitive manner
    return {palindrome.lower() for palindrome in palindromes}
