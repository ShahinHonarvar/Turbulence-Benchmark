
def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each possible subsequence of the string
    for i in range(4, len(string) - 3):
        # Check if the subsequence is a palindrome
        if string[i:i+4] == string[i:i+4][::-1]:
            # If it is, add it to the set of palindromes
            palindromes.add(string[i:i+4])
    return palindromes
