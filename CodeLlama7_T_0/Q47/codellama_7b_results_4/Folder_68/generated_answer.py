
def palindromes_of_specific_lengths(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each substring of length between 50 and 100 (both inclusive)
    for i in range(50, len(string), 2):
        # Check if the substring is a palindrome
        if string[i:i+1] == string[i:i+1][::-1]:
            # Add the palindrome to the set
            palindromes.add(string[i:i+1])
    return palindromes
