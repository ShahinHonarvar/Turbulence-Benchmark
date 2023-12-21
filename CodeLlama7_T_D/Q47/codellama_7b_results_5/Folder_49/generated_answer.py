
def palindromes_of_specific_lengths(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate over the substring of the given string from index 10 to index 100 (both inclusive)
    for i in range(10, 100 + 1):
        # Check if the substring starting at index i and ending at index i + 9 (since we want a length of 10) is a palindrome
        if string[i:i + 10] == string[i:i + 10][::-1]:
            # If it is, add it to the set of palindromes
            palindromes.add(string[i:i + 10])
    return palindromes
