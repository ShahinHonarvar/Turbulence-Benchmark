
def palindromes_of_specific_lengths(string):
    # Find all the palindromes in the given string
    palindromes = []
    for i in range(300):
        # Check if the substring from index 0 to index i is a palindrome
        substr = string[:i + 1]
        if substr == substr[::-1]:
            # Add the palindrome to the list of palindromes
            palindromes.append(substr)
    # Filter out the palindromes that are not of the specified lengths
    filtered_palindromes = []
    for palindrome in palindromes:
        if len(palindrome) >= 50 and len(palindrome) <= 60:
            filtered_palindromes.append(palindrome)
    # Return the set of all palindromes with the specified lengths
    return set(filtered_palindromes)
