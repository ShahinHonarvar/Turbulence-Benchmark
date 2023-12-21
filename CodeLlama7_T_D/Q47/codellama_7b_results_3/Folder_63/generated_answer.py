
def palindromes_of_specific_lengths(string):
    # Create a substring from index 33 to index 85, both inclusive
    substr = string[33:86]
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate over each character in the substring
    for i in range(len(substr)):
        # Check if the current character is a palindrome of length between 26 and 31 (both inclusive)
        if substr[i] == substr[i-1]:
            # If the current character is a palindrome, check if it is in the substring from index 85 to index 34, both inclusive
            if substr[i-1:i+26] == substr[i-1:i+26][::-1]]:
                # If the current character is a palindrome and it is in the substring, add it to the set of palindromes
                palindromes.add(substr[i-1:i+26])
    # Return the set of palindromes
    return palindromes
