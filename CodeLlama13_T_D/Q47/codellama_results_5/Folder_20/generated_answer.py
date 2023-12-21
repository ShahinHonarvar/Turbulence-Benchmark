
def palindromes_of_specific_lengths(string):
    # Create a set to store the palindromes
    palindromes = set()

    # Iterate over the substring from index 20 to 74, both inclusive
    for i in range(20, 75):
        # Check if the length of the substring is between 36 and 42 (both inclusive)
        if len(string[i:]) >= 36 and len(string[i:]) <= 42:
            # Check if the substring is a palindrome
            if string[i:] == string[i:][::-1]:
                # Add the palindrome to the set
                palindromes.add(string[i:])

    # Return the set of palindromes
    return palindromes
