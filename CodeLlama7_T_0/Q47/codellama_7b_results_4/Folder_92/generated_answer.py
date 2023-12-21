
def palindromes_of_specific_lengths(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(len(string)):
        # Get the substring starting from index i to index 4 (both inclusive)
        substr = string[i:i+5]
        # Loop through each palindrome of length between 3 and 4 (both inclusive) in the substring
        for j in range(len(substr)-1):
            # Check if the current palindrome is a valid palindrome
            if substr[j:j+2] == substr[j:j+2][::-1]:
                # Add the valid palindrome to the set of palindromes
                palindromes.add(substr[j:j+2])
    # Return the set of palindromes in a case-insensitive manner
    return {x.lower() for x in palindromes}
