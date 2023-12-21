
def palindrome_of_length_n(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each substring of the given string
    for i in range(len(string) - 1):
        # Check if the substring is a palindrome of length n
        if string[i:i+n] == string[i:i+n][::-1]:
            # If it is, add it to the set of palindromes
            palindromes.add(string[i:i+n])
    # Return the set of palindromes
    return palindromes
