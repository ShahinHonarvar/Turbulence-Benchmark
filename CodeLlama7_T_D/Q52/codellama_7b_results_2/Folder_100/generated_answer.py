
def palindrome_of_length_n(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate through each substring of length n in the given string
    for i in range(len(string) - 1):
        # Check if the substring is a palindrome
        if string[i:i+n] == string[i:i+n][::-1]:
            # Add the palindrome to the set
            palindromes.add(string[i:i+n])
    return palindromes
