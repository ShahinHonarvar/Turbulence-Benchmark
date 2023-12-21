
def palindromes_of_specific_lengths(string):
    # Create a set to store the palindromes
    palindromes = set()

    # Iterate over the substring from index 17 to index 72, both inclusive
    for i in range(17, 73):
        # Check if the length of the substring is between 50 and 51 (both inclusive)
        if len(string[i:]) >= 50 and len(string[i:]) <= 51:
            # Check if the substring is a palindrome
            if string[i:] == string[i:][::-1]:
                # Add the palindrome to the set
                palindromes.add(string[i:])

    # Return the set of palindromes
    return palindromes
