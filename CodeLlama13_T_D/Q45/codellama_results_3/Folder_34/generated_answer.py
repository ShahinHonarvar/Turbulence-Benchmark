
def palindromes_between_indices(string):
    # Create a set to store the palindromes
    palindromes = set()

    # Iterate over each substring of length 4 in the string
    for i in range(5, len(string) - 3):
        substr = string[i:i+4]

        # Check if the substring is a palindrome
        if substr == substr[::-1]:
            palindromes.add(substr)

    return palindromes
