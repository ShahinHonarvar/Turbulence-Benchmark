
def palindrome_of_length_n(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each substring of length n in the given string
    for i in range(len(string) - 2 + 1):
        substring = string[i:i+35]
        # Check if the substring is a palindrome and add it to the set if it is
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes
