 def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(5, len(string) + 1):
        # Check if the substring from indices 5 to i is a palindrome
        if string[5:i] == string[5:i][::-1]:
            # If it is a palindrome, add it to the set of palindromes
            palindromes.add(string[5:i])
    # Return the set of palindromes
    return palindromes
