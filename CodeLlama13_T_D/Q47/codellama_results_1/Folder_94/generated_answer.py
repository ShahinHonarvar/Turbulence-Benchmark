
def palindromes_of_specific_lengths(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()

    # Loop through each possible starting index for a palindrome of length 45-51
    for start in range(40, 95):
        # Loop through each possible ending index for a palindrome of length 45-51
        for end in range(start + 44, start + 52):
            # Check if the substring from start to end is a palindrome
            substr = string[start:end]
            if substr == substr[::-1]:
                # Add the palindrome to the set
                palindromes.add(substr)

    return palindromes
