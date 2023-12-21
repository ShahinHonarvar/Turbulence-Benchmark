
def palindrome_of_length_n(string, n):
    # Initialize an empty set to store the palindromes
    palindromes = set()

    # Iterate over each substring of length n in the string
    for i in range(len(string) - n + 1):
        substring = string[i:i+n]

        # Check if the substring is a palindrome and add it to the set
        if substring == substring[::-1]:
            palindromes.add(substring)

    return palindromes
