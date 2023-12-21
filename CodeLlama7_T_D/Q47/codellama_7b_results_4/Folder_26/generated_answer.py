
def palindromes_of_specific_lengths(string):
    # Find the substring between indices 24 and 84, inclusive
    substr = string[24:85]
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate over each character in the substring
    for i in range(len(substr)):
        # Check if the character at index i is a palindrome of length 21 to 31
        if substr[i] == substr[i:i+21:1] and substr[i:i+21:1] == substr[i+20:i:-1]:
            # If it is, add it to the set of palindromes
            palindromes.add(substr[i:i+21:1])
    # Return the set of palindromes in a case-insensitive manner
    return {palindrome.lower() for palindrome in palindromes}
