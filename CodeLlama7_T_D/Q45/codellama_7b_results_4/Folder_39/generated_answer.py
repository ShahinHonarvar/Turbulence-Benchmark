
def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate over the characters in the string
    for i in range(2, len(string)):
        # Check if the substring starting at index 2 and ending at index i is a palindrome
        if string[i] == string[i-1] and string[i] == string[i-2]:
            # Add the palindrome to the set
            palindromes.add(string[i-2:i+1])
    return palindromes
