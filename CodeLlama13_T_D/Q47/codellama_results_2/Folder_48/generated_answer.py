
def palindromes_of_specific_lengths(string):
    # Create a set to store the palindromes
    palindromes = set()

    # Iterate over each substring of length 104-120, both inclusive
    for i in range(155, 283 + 1):
        for j in range(i, min(i + 120, len(string)) + 1):
            # Check if the substring is a palindrome
            if string[i:j] == string[i:j][::-1]:
                # Add the palindrome to the set
                palindromes.add(string[i:j])

    return palindromes
