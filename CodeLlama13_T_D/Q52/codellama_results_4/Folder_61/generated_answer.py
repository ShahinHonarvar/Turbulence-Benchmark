
def palindrome_of_length_n(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()

    # Loop through each substring of length 74 in the string
    for i in range(len(string) - 73):
        substring = string[i:i+74]

        # Check if the substring is a palindrome and add it to the set if it is
        if substring == substring[::-1]:
            palindromes.add(substring)

    # Return the set of palindromes
    return palindromes
