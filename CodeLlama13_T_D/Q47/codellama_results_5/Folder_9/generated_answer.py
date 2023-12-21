
def palindromes_of_specific_lengths(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()

    # Loop through each substring of length 50-60 in the given string
    for i in range(len(string) - 49):
        substr = string[i:i+60]

        # Check if the substring is a palindrome and add it to the set if it is
        if substr == substr[::-1]:
            palindromes.add(substr)

    # Return the set of palindromes
    return palindromes
