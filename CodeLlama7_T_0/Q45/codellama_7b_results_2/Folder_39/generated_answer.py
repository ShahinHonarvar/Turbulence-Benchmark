
def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(2, len(string)):
        # Check if the substring starting at index 2 and ending at index i is a palindrome
        if string[i] == string[i-1]:
            # If it is a palindrome, add it to the set of palindromes
            palindromes.add(string[i-1:i+1])
    return palindromes
