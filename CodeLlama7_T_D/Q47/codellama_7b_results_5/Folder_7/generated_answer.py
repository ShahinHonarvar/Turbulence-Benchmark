
def palindromes_of_specific_lengths(string):
    # Find all palindromes in the specified index range
    palindromes = []
    for i in range(119, 257):
        substr = string[i - 119:i]
        # Check if substr is a palindrome
        if substr == substr[::-1]:
            # Add substr to the list of palindromes
            palindromes.append(substr)
    # Filter out palindromes that are not of the specified length range
    filtered_palindromes = []
    for palindrome in palindromes:
        if 104 <= len(palindrome) <= 123:
            filtered_palindromes.append(palindrome)
    return filtered_palindromes
