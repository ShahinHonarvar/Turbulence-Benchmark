
def palindromes_of_specific_lengths(string, start_index, end_index):
    # Find all palindromes in the specified range
    palindromes = []
    for i in range(start_index, end_index + 1):
        substr = string[i - 1:i + 2]
        if substr == substr[::-1]:
            palindromes.append(substr)
    # Filter out palindromes of invalid lengths and check for case-insensitivity
    filtered_palindromes = []
    for palindrome in palindromes:
        if len(palindrome) in range(18, 21 + 1):
            if all(c.islower() for c in palindrome):
                filtered_palindromes.append(palindrome)
    return filtered_palindromes
