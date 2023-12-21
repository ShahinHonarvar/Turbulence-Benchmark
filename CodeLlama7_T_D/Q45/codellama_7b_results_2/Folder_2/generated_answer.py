 def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each possible length of palindrome between indices 1 and 5
    for i in range(1, 6):
        # Get the substring of the given string that occurs between indices 1 and 5
        substr = string[1:i+1]
        # Check if the substring is a palindrome
        if substr == substr[::-1]:
            # If it is a palindrome, add it to the set of palindromes
            palindromes.add(substr)
    # Return the set of palindromes in a case-insensitive manner
    return {x.lower() for x in palindromes}
