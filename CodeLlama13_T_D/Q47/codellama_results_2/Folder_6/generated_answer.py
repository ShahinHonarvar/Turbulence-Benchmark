
def palindromes_of_specific_lengths(string):
    # Set of all palindromes with the required length and index range
    palindromes = set()

    # Loop through each substring of length 40 to 47 in the given string
    for i in range(45, 98 + 1):
        for j in range(i, i + 47 - 40 + 1):
            # Check if the substring is a palindrome and consists of English letters
            if string[i:j] == string[i:j][::-1] and all(c.isalpha() for c in string[i:j]):
                # Add the palindrome to the set
                palindromes.add(string[i:j])

    return palindromes
