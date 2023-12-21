
def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()

    # Loop through each possible substring of length 7 or more between indices 0 and 8 (both inclusive)
    for i in range(0, len(string) - 6):
        for j in range(i + 1, len(string)):
            # Check if the substring is a palindrome
            if string[i:j] == string[i:j][::-1]:
                # Add the palindrome to the set
                palindromes.add(string[i:j])

    return palindromes
