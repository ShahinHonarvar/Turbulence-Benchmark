
def palindromes_of_specific_lengths(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()

    # Iterate over each substring of length 17 to 66 (both inclusive) in the specified index range
    for i in range(12, 93):
        for j in range(i + 17, i + 67):
            # Check if the substring is a palindrome
            if string[i:j] == string[i:j][::-1]:
                # Add the palindrome to the set
                palindromes.add(string[i:j])

    return palindromes
