
def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each possible combination of letters in the given string that occur between index 0 and index 6, both inclusive
    for i in range(len(string) - 5):
        # Check if the substring starting at position i and having a length of 7 is a palindrome
        if string[i:i+7] == string[i:i+7][::-1]:
            # If it is, add it to the set of palindromes
            palindromes.add(string[i:i+7])
    return palindromes
