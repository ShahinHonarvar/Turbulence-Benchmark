
def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(len(string) - 4)):
        # Check if the current substring is a palindrome
        if string[i:i+5] == string[i:i+5][::-1]:
            # If it is, add it to the set of palindromes
            palindromes.add(string[i:i+5])
    return palindromes
