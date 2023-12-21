
def palindrome_of_length_n(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(len(string)):
        # Check if the current character is a palindrome of length n
        if string[i:i+n] == string[i:i+n][::-1]:
            # Add the palindrome to the set
            palindromes.add(string[i:i+n])
    return palindromes
