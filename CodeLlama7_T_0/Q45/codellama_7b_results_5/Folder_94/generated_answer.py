
def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(3, len(string)):
        # Check if the substring starting at index 3 and ending at index i is a palindrome
        if string[i] == string[i-1] and string[i-1] == string[i-2]:
            # If it is a palindrome, add it to the set of palindromes
            palindromes.add(string[i-2:i+1])
    # Return the set of palindromes
    return palindromes
