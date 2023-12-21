
def palindrome_of_length_at_least_n(string):
    # Initialize a set to store the palindromes
    palindromes = set()

    # Iterate over each substring of the given string
    for i in range(len(string)):
        for j in range(i + 44, len(string) + 1):
            substr = string[i:j]

            # Check if the substring is a palindrome
            if substr == substr[::-1]:
                # Add the palindrome to the set
                palindromes.add(substr)

    return palindromes
