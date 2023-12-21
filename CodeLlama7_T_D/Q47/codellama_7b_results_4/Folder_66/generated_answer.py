 def palindromes_of_specific_lengths(string):
    # Create a substring of the given string that starts at index 32 and ends at index 79 (both inclusive)
    substring = string[32:80]
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate over each character in the substring
    for i in range(len(substring)):
        # Check if the character at index i is a palindrome
        if substring[i] == substring[i:][::-1]:
            # If it is, add it to the set of palindromes
            palindromes.add(substring[i])
    # Return the set of palindromes that satisfy the requirements
    return palindromes
