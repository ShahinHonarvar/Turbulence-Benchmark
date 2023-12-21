
def palindromes_of_specific_lengths(string):
    # Extract the substring containing the palindromes
    substr = string[10:100]
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate over the characters in the substring
    for i in range(len(substr)):
        # Check if the character is a letter
        if substr[i].isalpha():
            # Extract the palindrome from the substring starting at index i
            palindrome = substr[i:]
            # Check if the palindrome is of the desired length
            if len(palindrome) >= 10 and len(palindrome) <= 50:
                # Add the palindrome to the set of palindromes
                palindromes.add(palindrome)
    # Return the set of palindromes
    return palindromes
