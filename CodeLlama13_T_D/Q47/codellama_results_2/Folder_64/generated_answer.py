
def palindromes_of_specific_lengths(string):
    # Create a set to store the palindromes
    palindromes = set()

    # Iterate over each substring of length 4-5 from index 0 to 7, both inclusive
    for i in range(8):
        for j in range(i+4, min(i+6, len(string))):
            # Check if the substring is a palindrome
            if string[i:j] == string[i:j][::-1]:
                # Add the palindrome to the set
                palindromes.add(string[i:j])

    return palindromes
