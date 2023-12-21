
def palindromes_of_specific_lengths(string):
    # Initialize empty set for palindromes
    palindromes = set()

    # Iterate over the substring from index 27 to index 77, both inclusive
    for i in range(27, 78):
        # Check if the length of the substring is between 18 and 19 (both inclusive)
        if len(string[i:]) >= 18 and len(string[i:]) <= 19:
            # Check if the substring is a palindrome in case-insensitive manner
            if string[i:].lower() == string[i:].lower()[::-1]:
                # Add the palindrome to the set of palindromes
                palindromes.add(string[i:])

    return palindromes
