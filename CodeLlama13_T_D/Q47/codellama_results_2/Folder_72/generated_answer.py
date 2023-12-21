
def palindromes_of_specific_lengths(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()

    # Iterate through each substring of length 27 to 58 (both inclusive) in the given string
    for i in range(26, 91):
        for j in range(i + 26, i + 59):
            # Check if the substring is a palindrome and only consists of English letters
            if string[i:j] == string[i:j][::-1] and all(chr.isalpha() for chr in string[i:j]):
                # Add the palindrome to the set
                palindromes.add(string[i:j])

    return palindromes
