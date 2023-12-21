
def palindrome_of_length_at_least_n(string, n):
    # Create a set to store the palindromes
    palindromes = set()

    # Iterate over each substring of length 34 or more in the string
    for i in range(len(string) - 33):
        substring = string[i:i + 34]

        # Check if the substring is a palindrome
        if substring == substring[::-1]:
            # Add the palindrome to the set
            palindromes.add(substring)

    return palindromes
