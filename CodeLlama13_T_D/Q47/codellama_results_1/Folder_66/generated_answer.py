
def palindromes_of_specific_lengths(string):
    # Create a set to store the palindromes
    palindromes = set()

    # Loop through each substring of length 41
    for i in range(32, 79 + 1):
        for j in range(i, min(i + 7, len(string))):
            # Check if the substring is a palindrome
            if string[i:j] == string[i:j][::-1]:
                # Add the palindrome to the set
                palindromes.add(string[i:j])

    return palindromes
